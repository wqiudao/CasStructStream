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


## error 

Qt: Session management error: None of the authentication protocols specified are supported.

A: This error can be safely ignored as it does not impact the execution or functionality of the program.

This error is related to session management within the Qt library and typically does not affect the actual functionality or performance of the program. While the message indicates an issue with specific authentication protocols, it poses no threat to core operations. Therefore, no special handling is required, and the message can be safely ignored as the application continues to function normally.










https://genome.jgi.doe.gov/portal/714PHBRim19094_FD/714PHBRim19094_FD.info.html





