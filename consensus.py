"""Find the consensus sequence of equal-length DNA strings.
"""

import pandas as pd
from Bio import SeqIO

# We use a dataframe with one row for each nucleotide and one column for each
# position in the strings.  The count for each nucleotide+position is updated
# by scanning each sequence.

init=0
for record in SeqIO.parse("data/rosalind_cons.fasta","fasta"):
    TEMP=str(record.seq)
    if init==0:
        df=pd.DataFrame(0,index=['A:','C:','G:','T:'],
            columns=range(len(TEMP)))
        init=init+1
    col=0
    for base in TEMP:
        if base=="A":
            df.loc['A:',col]+=1
        if base=="C":
            df.loc['C:',col]+=1
        if base=="T":
            df.loc['T:',col]+=1
        if base=="G":
            df.loc['G:',col]+=1
        col+=1

# Find the maximum row index in each column.  Note that this will take the
# first index if there is a tie.  Then build the consensus sequence using
# the maximum row indices.

cons=df.idxmax(axis='rows')
consensus=""
for pos,base in enumerate(cons):
    consensus=consensus+base
print(consensus.replace(":",""))
print(df.to_string(header=False))
