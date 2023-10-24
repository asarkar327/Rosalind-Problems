"""A script that computes the % GC content of a sequence
"""
from Bio import SeqIO

records=list(SeqIO.parse("/Users/Ankur/Downloads/rosalind_gc.fasta","fasta"))
gc_content=[(str(x.seq).count("G")+str(x.seq).count("C"))/len(x.seq)*100 for x in records]
max_gc=max(gc_content)
max_idx=gc_content.index(max_gc)
print(records[max_idx].id)
print(gc_content[max_idx])
