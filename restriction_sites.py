"""This script finds all putative restriction sites length 4 to 12.

It assumes that all palindromic sequences are candidate restriction sites.

[Alternative]: As written, the script checks for palindromes of the required length
at each base.  This is 5 checks per base, so it might be faster to enumerate
all possible restriction sites (there are only 5456 of the specified length) 
and just search for them (especially as the input string gets longer.) 
"""
from Bio.Seq import Seq
from Bio import SeqIO

for record in SeqIO.parse("data/rosalind_revp.fasta","fasta"):
    seq=str(record.seq)
for index in range(len(seq)):
    for size_try in range(4,13,2):
        substring=seq[index:(index+size_try)]
        if len(substring)==size_try:
            rev_substring=str(Seq(substring).reverse_complement())
            if substring==rev_substring:
                print(f"{index+1} {size_try}")

## Enumerate the restriction sites first
# nucs=['A','C','T','G']
# r4=[i+j+str(Seq(i+j).reverse_complement()) for i in nucs for j in nucs]
# r6=[i+j+k+str(Seq(i+j+k).reverse_complement()) for i in nucs for j in nucs for
#     k in nucs]
# r8=[i+j+k+l+str(Seq(i+j+k+l).reverse_complement()) for i in nucs for j in nucs
#     for k in nucs for l in nucs]
# r10=[i+j+k+l+m+str(Seq(i+j+k+l+m).reverse_complement()) for i in nucs for j in
#     nucs for k in nucs for l in nucs for m in nucs]
# r12=[i+j+k+l+m+n+str(Seq(i+j+k+l+m+n).reverse_complement()) for i in nucs for
#     j in nucs for k in nucs for l in nucs for m in nucs for n in nucs]
# sites=r4+r6+r8+r10+r12
# print(r4)
# for site in sites:
#     length=len(site)
#     tempseq=seq
#     while tempseq.find(site)>=0:
#         pos=tempseq.find(site)+1
#         tempseq=tempseq[0:pos-1]+tempseq[pos-1].lower()+tempseq[pos:]
#         print(f"{pos} {length}")
