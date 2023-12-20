#!/usr/bin/env python3
import sys
blast = sys.argv[1]
mg = set()
bf = sys.argv[2]
outp = sys.argv[3]

with open(blast, 'r') as ney:
    for line in ney:
        filtered_bl = line.strip().split("\t")
        seq = filtered_bl[1]
        begin, end = int(filtered_bl[8]), int(filtered_bl[9])
        
        if float(filtered_bl[2]) > 30 and int(filtered_bl[3]) >= 0.9 * int(filtered_bl[12]):
           
            with open(bf, 'r') as bedf:
                for line1 in bedf:
                    bed = line1.strip().split("\t")
                    seqid = bed[0]
                    name= bed[3]
                    seqstartn, sendn = int(bed[1]), int(bed[2])
                    if seq == seqid:
                        if begin >= seqstartn and end <= sendn:
                            mg.add(name)
                    
with open(outp, 'w') as ny:
    ny.write('\n'.join(mg))
    print(f"Number of matched genes: {len(mg)}")