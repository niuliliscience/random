#! /usr/bin/python
## Created by Lili Niu (lili.niu.ln1@roche.com)
## Created on 09/06/18
## this scripts is to grep each gid in a large file

import re
import glob, os
import sys
from sys import argv

usage = "\nusage:\t./grep_each.py [gid file] [large file]\n"

if len(argv) ==3:
    script, gid_file, large_file =argv
else:
    print (usage)
    quit()
    
with open(gid_file) as f_input:
    lines = f_input.read().splitlines()
    for line in lines:
        item=(re.split('\.',line))
        item1=(re.split('>', item[1]))
        chr= item1[0].replace("A","")
        chr= chr.replace("T","")
        chr= chr.replace("C","")
        chr= chr.replace("G","")
        grep_s ="grep "+chr+" "+large_file
        print grep_s
        os.system(grep_s)
