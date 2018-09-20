# Random scripts writen
## ZerobasedBed_to_VCF.py
* Input: Zero based BED file with: chr, start, end, ref allele, variant allele
* Output file: VCF format
```
/path/to/ZerobasedBed_To_VCF.py <zero_based_BED file>
```

## ZerobasedBed_to_gdot.py
* Input: Zero based BED file with: chr, start, end, ref allele, variant allele
* Output file: g.name in each line
```
/path/to/ZerobasedBed_To_gdot.py <zero_based_BED file>
```

## grep_tcgav9_eachTumor.py
* Input: 
1. file with g.name in each line
1.  TCGA folder
* Output: g.name with TCGA hit in each cancer
```
/path/to/grep_tcgav9_eachTumor.py <g.name file> <path to TCGA>
```