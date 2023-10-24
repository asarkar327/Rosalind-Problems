"""A script to compute the hamming distance between two sequences.
"""
import argparse

parser=argparse.ArgumentParser(description="A function to compute the hamming "
    "distance between two sequences.  The sequences must be the same length")
parser.add_argument("seq1",type=str)
parser.add_argument("seq2",type=str)
args=parser.parse_args()
SEQ1=str(args.seq1)
SEQ2=str(args.seq2)
LENGTH=len(SEQ1)
hd=0
for base in range(LENGTH):
    if SEQ1[base]!=SEQ2[base]:
        hd+=1

print(hd)
