"""This script finds open reading frames in a string of DNA.

The script assumes ORFs can be on either the 5' or the 3' strand.
"""
import re
from Bio.Seq import Seq
from Bio import SeqIO

for record in SeqIO.parse("/Users/Ankur/work/Rosalind/data/rosalind_orf.fasta", "fasta"):
    sequence=str(record.seq)

orfsaa=[]
# Check all possible frames on the forward strand.
for i in range(3):
    seq=sequence[i::]
    orfs=[seq,seq[0:-1],seq[0:-2]]
    # Find the frame that has length divisible by 3.
    modcheck=[len(x)/3%1 for x in orfs]
    cds=Seq(orfs[modcheck.index(min(modcheck))])
    aa=str(cds.translate()).replace('*','_')  # Remove * so we can use regex
    matches=re.finditer(r"(?=(M.*?_))",aa)
    for match in matches:
        orfsaa.append(match.group(1))
# Reverse complement the sequence
# my_dna=sequence.lower()
# rev_dna=my_dna[::-1]
# rev_dna_1=rev_dna.replace("a","T")
# rev_dna_2=rev_dna_1.replace("t","A")
# rev_dna_3=rev_dna_2.replace("c","G")
# sequence=rev_dna_3.replace("g","C")
sequence=str(Seq(sequence).reverse_complement())
# Check all possible reading frames on the reverse strand
for i in range(3):
    seq=sequence[i::]
    orfs=[seq,seq[0:-1],seq[0:-2]]
    modcheck=[len(x)/3%1 for x in orfs]
    cds=Seq(orfs[modcheck.index(min(modcheck))])
    aa=str(cds.translate()).replace('*','_')
    matches=re.finditer(r"(?=(M.*?_))",aa)
    for match in matches:
        orfsaa.append(match.group(1))
orfsaa=[x.replace('_','') for x in orfsaa]
unique_orfsaa=list(set(orfsaa))
for i in unique_orfsaa:
    print(i)
