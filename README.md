# CasStructStream
<pre>
usage: casstructstream [-h]
                       {sCas,rna,msa,pdb2dalidb,pdb_folder2dalidb,structmap,makedalidb,scatter,extract_af3_results,create_run_af3_from_csv_sh}
                       ...

A tool for designed for Streamlining identification of CRISPR-Cas systems

positional arguments:
  {sCas,rna,msa,pdb2dalidb,pdb_folder2dalidb,structmap,makedalidb,scatter,extract_af3_results,create_run_af3_from_csv_sh}
                        Subcommands
    sCas                Streamlined Scanning of CRISPR-Cas Systems.
    rna                 Draw RNA secondary structure.
    msa                 Run protein multiple sequence alignment.
    pdb2dalidb          Compare a PDB file with DALI database.
    structcompare       Compare predicted PDB structures against a reference fold database to identify structural similarity.
    structmap           Generate structural comparison matrix and clustering tree from a folder of PDB files.
    makedalidb          Create DALI database: Converts a set of PDB files to DALI format numbers for subsequent
                        structural searches.
    scatter             Generate scatter plots from a CSV file
    extract_af3_results
                        Extract AF3 prediction results and summary.
    create_run_af3_from_csv_sh
                        Create the run_af3_from_csv.sh shell script.

options:
  -h, --help            show this help message and exit

</pre>

## install
```
dnf install compat-libgfortran-48.x86_64       # requires root privileges

conda create -n casstructstream python=3.12  -y
conda activate casstructstream 

pip install gemmi
pip install matplotlib
pip install PyQt5
pip install pandas
pip install scipy
conda install conda-forge::perl  -y
conda install anaconda::pyqt -y
conda install bioconda::piler-cr -y
conda install bioconda::prodigal -y
conda install bioconda::hmmer  -y
conda install wqiudao::casstructstream  -y

```
[optional]
```
dnf install epel-release

sudo dnf install  https://www.itzgeek.com/msttcore-fonts-2.0-3.noarch.rpm

sudo fc-cache -fv
```


error [optional]
<pre>
Qt: Session management error: None of the authentication protocols specified are supported.

A: This error can be safely ignored as it does not impact the execution or functionality of the program.

This error is related to session management within the Qt library and typically does not affect the actual functionality or performance of the program. While the message indicates an issue with specific authentication protocols, it poses no threat to core operations. Therefore, no special handling is required, and the message can be safely ignored as the application continues to function normally.
</pre>


## Test Data Preparation
The assembled genome used was obtained from the JGI database.

![assemble](https://github.com/wqiudao/CRISPRCasStream/blob/main/img/crispr_cas_data.png)
*
https://genome.jgi.doe.gov/portal/714PHBRim19094_FD/714PHBRim19094_FD.info.html


## sCas: Streamlined Scanning of CRISPR-Cas Systems.
Use the sCas function with the file `714PHBRim19094_FD_assembly.contigs.fasta` to identify CRISPR-Cas systems.
All results are saved in the `crisprcasstream_results` directory.
  1. crisprcasstream_results/CRISPRCasStream_714PHBRim19094_FD_assembly_2024-11-17_21-01-10.csv
  2. crisprcasstream_results/sCas_scan_2024-11-17_21-01-25_page_1.pdf
  3. crisprcasstream_results/RNA_Struct_DR_714PHBRim19094_FD_assembly_2024-11-22_15-51-38.pdf
```
usage: casstructstream sCas [-h] [--genome_size GENOME_SIZE] [--flanking_length FLANKING_LENGTH] [--cas_min CAS_MIN] [--cas_max CAS_MAX]
                            [--motif MOTIF]
                            assembly_file

positional arguments:
  assembly_file         Input assembly file in FASTA format.

options:
  -h, --help            show this help message and exit
  --genome_size GENOME_SIZE
                        The minimum scaffold length for genome assembly. Scaffolds shorter than this value will be excluded from the
                        assembly. [def. 3000]
  --flanking_length FLANKING_LENGTH
                        The length of the genomic DNA sequence flanking each side of the CRISPR array. [def. 12000]
  --cas_min CAS_MIN     The minimum length of candidate Cas proteins. Proteins shorter than this value will be excluded from
                        consideration. [def. 400]
  --cas_max CAS_MAX     The max length of candidate Cas proteins. Proteins longer than this value will be excluded from consideration.
                        [def. 1000]
  --motif MOTIF         Specify the motif pattern to search for in the protein sequence. The motif should be a string where uppercase
                        letters represent fixed amino acids, and lowercase 'x' represents any amino acid or character. For example,
                        'RxxxxH' will match any sequence where 'R' is followed by four arbitrary amino acids and ending with 'H'. The 'x'
                        can match any character, including non-amino acid characters. [def. RxxxxH]

```
```
casstructstream  sCas 714PHBRim19094_FD_assembly.contigs.fasta
# or
casstructstream  sCas 714PHBRim19094_FD_assembly.contigs.fasta --motif RxxxxH
```
<pre>
  2024-11-17_21-01-10
  crispr scanning...
  Finished processing 1_pilercr_3000_0
  crispr done...
  prodigal running...
  prodigal done...
  parsing and visualization...
  Done...
</pre>
![sCas](https://github.com/wqiudao/CRISPRCasStream/blob/main/img/crisprcasstream2.png)
![sCas](https://github.com/wqiudao/CRISPRCasStream/blob/main/img/crisprcasstream3.png)
![sCas](https://github.com/wqiudao/CRISPRCasStream/blob/main/img/crisprcasstream4.png)
![sCas](https://github.com/wqiudao/CRISPRCasStream/blob/main/img/crisprcasstream13.png)


## rna: Draw RNA secondary structure.
The input file is in FASTA format, containing sequences for RNA secondary structure prediction.
`  crisprcasstream_results/DR.fasta
`  crisprcasstream_results/DR_RNA_Struct.pdf

<pre> DR.fasta
  >scaffold_782_c1	
  GTCGCCCTCTTCACAGGGGGCGTGGATTGAAA
  >scaffold_1146_c1	
  GTTTCAATCCACGCCCCCTGTGAAGAGGGCGAC
  >scaffold_2788_c1	
  CAATCCACGCCCCCTGTGAAGAGGGCGAC
  >scaffold_4033_c1	
  GTCACATCCCCCGCACGCGCGGGGATTGAAAC
  >scaffold_25_c1	
  GTTTCAGAGAGTCCCTCGATAAAATGAGGATTGAAAG
  >scaffold_1323_c1	
  GCTTCAATTGGGCCGCGGTCTTTCAACCGCGGAAAC
  >scaffold_3557_c1	
  GTTATACAATACCCCTAAATTA
</pre>
```
casstructstream  rna DR.fasta
```
<pre>
    1 GTCGCCCTCTTCACAGGGGGCGTGGATTGAAA scaffold_782_c1
    2 GTTTCAATCCACGCCCCCTGTGAAGAGGGCGAC scaffold_1146_c1
    3 CAATCCACGCCCCCTGTGAAGAGGGCGAC scaffold_2788_c1
    4 GTCACATCCCCCGCACGCGCGGGGATTGAAAC scaffold_4033_c1
    5 GTTTCAGAGAGTCCCTCGATAAAATGAGGATTGAAAG scaffold_25_c1
    6 GCTTCAATTGGGCCGCGGTCTTTCAACCGCGGAAAC scaffold_1323_c1
    7 GTTATACAATACCCCTAAATTA scaffold_3557_c1
</pre>
![rna](https://github.com/wqiudao/CRISPRCasStream/blob/main/img/crisprcasstream5.png)
![rna](https://github.com/wqiudao/CRISPRCasStream/blob/main/img/crisprcasstream6.png)
![rna](https://github.com/wqiudao/CRISPRCasStream/blob/main/img/crisprcasstream7.png)

## msa: Run protein multiple sequence alignment
The input file is in FASTA format, containing protein sequences for multiple sequence alignment.
<pre>
input:
  crisprcasstream_results/protein.fasta
output:
  crisprcasstream_results/protein_MSA_TREE.pdf
  crisprcasstream_results/protein_MSA.pdf
</pre>
```
casstructstream  msa protein.fasta
```
<pre>
  Check for duplicates in FASTA headers and replace invalid characters....
  ...Begin to run muscle...
  ...Begin to run FastTree...
  ...Generating PDF with ete3...
  Done....
</pre>
![rna](https://github.com/wqiudao/CRISPRCasStream/blob/main/img/crisprcasstream8.png)
![rna](https://github.com/wqiudao/CRISPRCasStream/blob/main/img/crisprcasstream12.png)




### pdb2dalidb
Use the built-in CAS core library to perform structural comparisons.
```
casstructstream  pdb2dalidb test.pdb
casstructstream  pdb2dalidb test.cif
```
### makedalidb
Use the subcommand `makedalidb` to create a custom reference structure database.

```
casstructstream makedalidb HEPN_REF_PDB_Cas13_abdhx
casstructstream pdb2dalidb --dali_database  HEPN_REF_PDB_Cas13_abdhx_dali test.pdb 
```
### pdb_folder2dalidb
Compare a folder of PDB files against the DALI structural database.

```
usage: casstructstream pdb_folder2dalidb [-h] [--dali_database DALI_DATABASE] [--ymax YMAX] [--threads THREADS] pdb_folder

positional arguments:
  pdb_folder            The name of the folder containing PDB files to be compared.

options:
  -h, --help            show this help message and exit
  --dali_database DALI_DATABASE
                        Provide a custom database path if needed. By default, uses its built-in core database with experimentally determined
                        CRISPR-Cas structures.
  --ymax YMAX           Set the maximum value for the y-axis in the output plot (default: 20).
  --threads THREADS     Number of threads to use for parallel processing (default: use all available CPU cores).


casstructstream pdb_folder2dalidb pdb_folder
```


![pdb_folder](https://github.com/wqiudao/CRISPRCasStream/blob/main/img/pdb_Folder.png)



### structmap           
Generate structural comparison matrix and clustering tree from a folder of PDB files.
```
usage: casstructstream structmap [-h] [--threads THREADS] [--width WIDTH] [--inner_width INNER_WIDTH] [--inner_height INNER_HEIGHT] pdb_folder

positional arguments:
  pdb_folder            Folder containing PDB files to be structurally compared.

options:
  -h, --help            show this help message and exit
  --threads THREADS     Number of threads to use for structural comparisons (default: all CPU cores).
  --width WIDTH         Width (in pixels) of the output ETE3 tree image (default: 800).
  --inner_width INNER_WIDTH
                        Width (in inches) of the combined heatmap/dendrogram/tree figure (default: 28).
  --inner_height INNER_HEIGHT
                        Height (in inches) of the combined heatmap/dendrogram/tree figure (default: 8).


casstructstream structmap pdb_folder
```
![pdb_folder](https://github.com/wqiudao/CRISPRCasStream/blob/main/img/structmap.png)


# References/Citations
CasStructStream: A Software Solution for Accelerating Cas System Discovery and Structural Comparison













