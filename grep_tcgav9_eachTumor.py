#! /usr/bin/python
## Created by Lili Niu (lili.niu.ln1@roche.com)
## Created on 09/07/18
## this scripts is to grep chr, match ref and alt, count TCGA hit in each tumor mutect file

import re
import glob, os
import sys
from sys import argv
import gzip

usage = "\nusage:\t./grep_each.py [gid file] [TCGA_folder]\n"

if len(argv) ==3:
    script, gid_file, tcga_folder =argv
else:
    print (usage)
    quit()
tumor_list=[]
for root, dirs, files in os.walk(tcga_folder):
    file_list = glob.glob(os.path.join(os.getcwd(),root, "TCGA*mutect*maf*.gz"))
    for file_path in file_list:
        folders=file_path.split('/')
        fname=folders[len(folders)-1]
        cols=fname.split('.')
        tumor_list.append(cols[1])

print ("ID\t"+str(tumor_list))

with open(gid_file) as f_input:
    lines = f_input.read().splitlines()
    for line in lines:
        line=line.rstrip("\n")
        item=(re.split('\.',line))
        item1=(re.split('>', item[1]))
        chr= item1[0].replace("A","")
        chr= chr.replace("T","")
        chr= chr.replace("C","")
        chr= chr.replace("G","")
        tcga_count =[]
        for root, dirs, files in os.walk(tcga_folder):
            file_list = glob.glob(os.path.join(os.getcwd(),root, "TCGA*mutect*maf*.gz"))
            for file_path in file_list:
                #grep chr location first
                grep_s ="zgrep "+chr+" "+file_path+">tmp.txt"
                os.system(grep_s)
                hit=0
                tmp_file="tmp.txt"
                with open(tmp_file) as match_input:
                    rows=match_input.read().splitlines()
                    for row in rows:
                        arr=row.split('\t')
                        gid=arr[4]+":g."+arr[5]+arr[11]+">"+arr[12]
                        if(gid == line):
                            hit=hit+1
                tcga_count.append(hit)
        print (line+"\t"+str(tcga_count))
