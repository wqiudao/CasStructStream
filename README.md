# CRISPRCasStream

CRISPRCasStream simplifies both installation and usage, enabling the rapid identification of CRISPR-Cas systems directly from assembled genomic data while providing graphical representations. Compared to similar tools, CRISPRCasStream offers a fivefold increase in identification speed, making it a highly efficient solution for CRISPR-Cas analysis.

```bash
(crisprcasstream) [miniconda3@localhost CRISPRCasStream]$ crisprcasstream 
usage: crisprcasstream [-h] {sCas,rna,msa} ...

A tool for designed for Streamlining identification of CRISPR-Cas systems

positional arguments:
  {sCas,rna,msa}  Subcommands
    sCas          Streamlined Scanning of CRISPR-Cas Systems.
    rna           Draw RNA secondary structure.
    msa           Run protein multiple sequence alignment.

options:
  -h, --help      show this help message and exit

```

## install
```
conda create -n crisprcasstream python=3.12  -y
conda activate crisprcasstream

pip install matplotlib
conda install anaconda::pyqt -y
conda install bioconda::piler-cr -y
conda install bioconda::prodigal -y
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

```
crisprcasstream sCas 714PHBRim19094_FD_assembly.contigs.fasta 
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

## rna: Draw RNA secondary structure.
The input file is in FASTA format, containing sequences for RNA secondary structure prediction.
crisprcasstream_results/DR.fasta
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















