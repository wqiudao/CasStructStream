# CRISPRCasStream

CRISPRCasStream simplifies both installation and usage, enabling the rapid identification of CRISPR-Cas systems directly from assembled genomic data while providing graphical representations. Compared to similar tools, CRISPRCasStream offers a fivefold increase in identification speed, making it a highly efficient solution for CRISPR-Cas analysis.

usage: CRISPRCasStream.py [-h] {sCas,rna,msa} ...

A tool for designed for Streamlining identification of CRISPR-Cas systems

positional arguments:
  {sCas,rna,msa}  Subcommands
    sCas          Streamlined Scanning of CRISPR-Cas Systems.
    rna           Draw RNA secondary structure.
    msa           Run protein multiple sequence alignment.

options:
  -h, --help      show this help message and exit




## install
conda create --name crisprcasstream -y

conda activate crisprcasstream

conda install anaconda::pyqt  -y

pip install matplotlib
