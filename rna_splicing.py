"""This script outputs a translated CDS following splicing.  

It assumes the first line in the FASTA is the transcript and the remaining 
lines are introns. 
"""
from Bio import SeqIO
from Bio.Seq import Seq

records=[]
for record in SeqIO.parse("data/rosalind_splc.fasta","fasta"):
    records.append(str(record.seq))
cds=records[0]
introns=records[1::]
for intron in introns:
    cds=cds.replace(intron,'')
print(str(Seq(cds).translate()).strip('*'))
