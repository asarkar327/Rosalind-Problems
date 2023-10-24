"""A script to determine how many mRNAs could produce a given protein.
"""
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("seq",type=str, help="an amino acid sequence")
args=parser.parse_args()
AASEQ=str(args.seq)
# print(aaseq)

codon_count={
    'M':1,
    'A':4,
    'R':6,
    'N':2,
    'D':2,
    'C':2,
    'Q':2,
    'E':2,
    'G':4,
    'H':2,
    'I':3,
    'L':6,
    'K':2,
    'F':2,
    'P':4,
    'S':6,
    'T':4,
    'W':1,
    'Y':2,
    'V':4
}
mrnas=3
for res in AASEQ:
    mrnas=mrnas*codon_count[res] % 1e6
print(int(mrnas))
