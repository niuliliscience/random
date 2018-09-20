#! /usr/bin/env bash
## Created by Lili Niu (lili.niu.ln1@roche.come)
## Created on 9/18/18
## This script is to dedup jax.variant.alltrans.txt file based on g.name (2nd column), merge dup's jax_ID (4th column) 
## Input file columns are: gene:p.name, g.name, all tx, jax_ID, jax_gname

filename="$1"
declare -A gname_jak
while read -r line
do
    rows=(${line///})
    gname=${rows[1]}
    jax_id=${rows[3]}
    dup_id=${gname_jak[$gname]}
    if ! [[ $dup_id =~ $jax_id ]];then
	gname_jak[$gname]=$dup_id","$jax_id
    fi
done <"$filename"
while read -r line
do
    rows=(${line///})
    gname=${rows[1]}
    jax_list=${gname_jak[$gname]}
    jax_list=${jax_list:1}
    echo -e ${rows[0]}"\t"$gname"\t"${rows[2]}"\t"$jax_list"\t"${rows[4]}
done <"$filename"
