#! /usr/bin/python

import re
import glob, os
import sys
from sys import argv

usage = "\nusage:\t./ZerobasedBed_To_VCF.py [0_based.bed] [genome.2bit file]\n"

## This script is to take 0-based BED file, creat VCF file format as output
## For deletion variant type, add the previous base in front of Ref., and add the previous base as Alt.
## For substitution and the Ref is longer tha Alt, add the previous base in front of Ref., and add the previous base in front of Alt.
## For SNP,do nothing to Ref and Alt
## For insertion, do nothing to Ref and Alt

if len(argv) ==3:
    script, bed_file, genome2bit =argv
else:
    print (usage)
    quit()

output_line ="##fileformat=VCFv4.2\n#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n"
for line in open (bed_file):
    line = line.rstrip('\n')
    line = line.replace('\n','').replace('\r','')
    cols = line.split('\t')
    col_num = len(cols)
    left = str(int(cols[1])-1)
    pos = str(int(cols[1])+1)
    end = cols[2]
    seq = cols[0]
    ref = cols[3]
    alt = cols[4]
    id = cols[5].replace(' ','_')
    diff = len(ref)-len(alt)
    twobit='./twoBitToFa '+genome2bit+' tmp.fa -seq='+seq+' -start='+left+' -end='+cols[1]
    #print (twobit)
    os.system(twobit)
    f=open('tmp.fa')
    lines=f.readlines()
    left_base=lines[1].rstrip('\n')
    header=lines[0].rstrip('\n')
    ## For deletion variant type, add the previous base in front of Ref, and add the previous base as Alt.
    if (alt =='.'):
        ref =left_base+ref
        alt = left_base
        pos = str(int(pos)-1)
    ## For substitution and the Ref is shorter tha Alt, add the previous base in front of Ref., and add the previous base in front Alt.
    elif (diff >0):
        ref =left_base+ref
        alt = left_base+alt
        pos = str(int(pos)-1)
           
    output_line = (output_line+seq+'\t'+pos+'\t'+id+'\t'+ref+'\t'+alt+'\t.\t.\t\n')
output_line =output_line.rstrip('\n')
print (output_line)
