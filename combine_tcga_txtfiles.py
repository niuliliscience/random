#! /usr/bin/python
## Created by Lili Niu (lili.niu.ln1@roche.com)
## Created on 09/06/18
## this scripts is to combine TCGA maf.txt files in all cancer folders

import re
import glob, os
import sys
from sys import argv

usage = "\nusage:\t./combine_tcga_files.py [cosmic folder]\n"

## this scripts is to combine TCGA maf.txt files in all cancer folders

if len(argv) ==2:
    script, tcga_folder =argv
else:
    print (usage)
    quit()
    
merge_txt =[]
for root, dirs, files in os.walk(tcga_folder):
    print(root)
    file_list = glob.glob(os.path.join(os.getcwd(),root, "*.txt"))

    for file_path in file_list:
        with open(file_path) as f_input:
            lines = f_input.read().splitlines()
            for line in lines:
                merge_txt.append(line)

print merge_txt
