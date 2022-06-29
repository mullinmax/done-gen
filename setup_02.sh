#!/bin/bash

echo 'creating conda enviroment'
conda create -n done_gen python=3.10
source activate done_gen
conda install --file requirements.txt