#!/bin/bash

# ========== Usage ==========
# bash run_haddock3.sh protein.pdb rna.pdb
# This script creates a docking folder, builds HADDOCK3 config, and runs docking via Docker
# ===========================

protein_file="$1"
rna_file="$2"

# ======= Check input =======
if [[ ! -f "$protein_file" || ! -f "$rna_file" ]]; then
    echo "[ERROR] Input PDB files not found!"
    echo "Usage: $0 protein.pdb rna.pdb"
    exit 1
fi

# ======= Parse names =======
protein_base=$(basename "$protein_file")
rna_base=$(basename "$rna_file")
protein_name="${protein_base%%.*}"
target_dir="docking_${protein_name}"

# ======= Create directory and copy files =======
mkdir -p "$target_dir/data"
cp "$protein_file" "$target_dir/data/$protein_base"
cp "$rna_file" "$target_dir/data/$rna_base"

# ======= Create HADDOCK3 config file =======
cat > "$target_dir/cas-crrna-docking.cfg" <<EOF
run_dir = "run_${protein_name}"
mode = "local"
ncores = 40

molecules = [
    "data/${protein_base}",
    "data/${rna_base}"
]

[topoaa]
autohis = false

[flexref]
sampling_factor = 20
tolerance = 20

[emref]
tolerance = 20

[clustfcc]
min_population = 1

[seletopclusts]
top_models = 4
EOF

# ======= Run HADDOCK3 via Docker =======
echo "Running HADDOCK3 for ${protein_base} and ${rna_base}"
docker run --rm \
  -u $(id -u):$(id -g) \
  -v "$(pwd)/$target_dir":/data \
  haddock3 /data/cas-crrna-docking.cfg
