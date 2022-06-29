#!/bin/bash

echo 'installing mini conda'
curl https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh -s --output miniconda_installer.sh
chmod +x miniconda_installer.sh
./miniconda_installer.sh -u
rm miniconda_installer
echo 'restart your shell then run setup_02.sh'
# echo 'setting up conda enviroment'
# conda create env -n done-gen python=3
# source activate done-gen
# conda install -r requirements.txt