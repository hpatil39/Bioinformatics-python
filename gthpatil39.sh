#!/bin/bash

query_seqs="$1"
genome_assembly="$2"
outfile="$4"

tblastn \
        -query $query_seqs \
        -subject $genome_assembly \
        -outfmt '6 std qlen sstart send' \
        -task tblastn\
| awk '$3>30 && $4>0.9*$13' > Hos.txt
echo "$(wc -l Hos.txt | cut -d' ' -f1) matches found in $genome_assembly"

bedfile="$3"

while read -r _ a b c _; do 
	awk -v start="$b" -v end="$c" '$2 >= start && $3 <= end {print $4}' Hos.txt > $outfile
done < "$bedfile"

echo "Gene names predicted HK domains have been written to $4"
match=$(sort -u $outfile | wc -l )
echo "$match2"
