#! /usr/bin/python

import re
import glob, os
import sys
from sys import argv

usage = "\nusage:\t./ZerobasedBed_To_VCF.py [0_based.bed]\n"

## This script is to take 0-based BED file, creat g dot as output

if len(argv) ==2:
    script, bed_file =argv
else:
    print (usage)
    quit()

output_line = "ID\tGdot\n"
for line in open (bed_file):
    line = line.rstrip('\n')
    line = line.replace('\n','').replace('\r','')
    cols = line.split('\t')
    col_num = len(cols)
    left = str(int(cols[1])-1)
    start = str(int(cols[1])+1)
    end = cols[2]
    seq = cols[0]
    ref = cols[3]
    alt = cols[4]
    id = cols[5].replace(' ','_')
    diff = len(ref)-len(alt)
    ## For deletion variant type
    if (alt =='.'):
        gdot =seq+':g.'+start+'_'+end+'del'
    ## For deletion and then insertion
    elif (diff >0):
        gdot =seq+':g.'+start+'_'+end+'delins'+alt
    ## For SNP
    elif (len(ref)==1 and len(alt)==1):
        gdot =seq+':g.'+start+ref+'>'+alt
    ## For deltion and insertion substitution with same length
    elif (diff ==0 and len(ref)>1):
        gdot =seq+':g.'+start+'_'+end+'delins'+alt
    ## For insertion
    elif (diff <0):
        alt  = alt[1:]
        gdot = seq+':g.'+start+'ins'+alt

    output_line = (output_line+id+'\t'+gdot+"\n")
output_line =output_line.rstrip('\n')
print (output_line)
