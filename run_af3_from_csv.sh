#!/bin/bash

# ========== Usage ========== 
# bash run_af3_from_csv.sh input.csv [--id_col N] [--protein_col N] [--rna_col N]
# All column indexes start from 1
# Defaults: --id_col 1 --protein_col 2 --rna_col not used
# ============================

csv_file="$1"

# Default column numbers
id_col=1
protein_col=2
rna_col=""

# Parse optional arguments
shift
while [[ $# -gt 0 ]]; do
    case "$1" in
        --id_col)
            id_col="$2"
            shift 2
            ;;
        --protein_col)
            protein_col="$2"
            shift 2
            ;;
        --rna_col)
            rna_col="$2"
            shift 2
            ;;
        *)
            echo "[ERROR] Unknown option: $1"
            exit 1
            ;;
    esac
done

# Check file existence
if [ ! -f "$csv_file" ]; then
    echo "[ERROR] File not found: $csv_file"
    exit 1
fi

echo "========== AF3 Batch Runner =========="
echo "[INFO] Input file    : $csv_file"
echo "[INFO] ID column     : $id_col"
echo "[INFO] Protein column: $protein_col"
echo "[INFO] RNA column    : ${rna_col:-None}"
echo "======================================"

# Remove invalid characters from protein sequence
sanitize_protein_sequence() {
    local sequence="$1"
    echo "$sequence" | tr -d -c 'ACDEFGHIKLMNPQRSTVWY'
}

# Convert DNA sequence to RNA sequence
convert_dna_to_rna() {
    local sequence="$1"
    sequence="${sequence%%;*}"
    echo "$sequence" | tr 'Tt' 'Uu'
}

# Run AlphaFold3 prediction
run_af3() {
    local protein_id="$1"
    local protein_sequence="$2"
    local rna_sequence="$3"

    protein_sequence=$(sanitize_protein_sequence "$protein_sequence")

    if [[ -n "$rna_sequence" && "$rna_sequence" != "null" ]]; then
        rna_sequence="${rna_sequence%%;*}"
        rna_sequence=$(convert_dna_to_rna "$rna_sequence")
    else
        rna_sequence="null"
    fi

    mkdir -p "$protein_id"

    local json_output=$(cat <<EOF
{
  "name": "$protein_id",
  "modelSeeds": [1,2],
  "sequences": [
    {
      "protein": {
        "id": "A",
        "sequence": "$protein_sequence"
      }
    }$([[ "$rna_sequence" != "null" ]] && echo ",")$([[ "$rna_sequence" != "null" ]] && echo '
    {
      "rna": {
        "id": "B",
        "sequence": "'"$rna_sequence"'"
      }
    }')
  ],
  "dialect": "alphafold3",
  "version": 1
}
EOF
)

    echo "$json_output" > "$protein_id/fold_input.json"
    echo "[INFO] JSON saved: $protein_id/fold_input.json"

    local total_cpus=$(nproc)
    local half_cpus=$((total_cpus / 1))

    docker run   -u $(id -u):$(id -g) \
        --volume "$PWD/$protein_id:/root/af_input" \
        --volume "$PWD/$protein_id:/root/af_output" \
        --volume /data3/Downloads/af3_db:/root/public_databases \
        --gpus all \
        alphafold3 \
        python run_alphafold.py --nhmmer_n_cpu "$half_cpus" \
            --json_path=/root/af_input/fold_input.json \
            --model_dir=/root/public_databases \
            --output_dir=/root/af_output
}

# ===== Keep the first line, no skipping =====
awk -F',' -v id_col="$id_col" -v protein_col="$protein_col" -v rna_col="$rna_col" '{
    gsub(/ /, "", $id_col)
    gsub(/ /, "", $protein_col)
    if (rna_col != "") gsub(/ /, "", $rna_col)
    print $id_col "\t" $protein_col "\t" (rna_col != "" ? $rna_col : "null")
}' "$csv_file" | while IFS=$'\t' read -r protein_id protein_sequence rna_sequence; do
    if [[ -z "$protein_id" || -z "$protein_sequence" ]]; then
        continue
    fi
    if [[ ${#protein_sequence} -lt 400 ]]; then
        continue
    fi
    if [[ ! "$rna_sequence" =~ ^[AUGCTtaugc\;]+$ ]]; then
        rna_sequence="null"
    fi
    run_af3 "$protein_id" "$protein_sequence" "$rna_sequence"
done

