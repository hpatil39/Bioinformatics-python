#!/usr/bin/env python3
fasta = []
fna = ''

with open('aligned.fna', 'r') as virat:
    for line in virat:
        line = line.strip()
        
        if not line.startswith('>'):
            fasta.append(line)
     
print(fasta[0])
dna = ['|' if a == b else ' ' for a, b in zip(fasta[0], fasta[1])]
vk = ''.join(dna)
print(vk)
print(fasta[1])