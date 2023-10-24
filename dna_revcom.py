"""A script to get the reverse complement of a DNA string.
"""
import argparse

# We use string replacement, one nucleotide at a time to get the desired result.
# To avoid overwriting results, we change the case each time a letter is
# replaced.

parser=argparse.ArgumentParser()
parser.add_argument("seq",type=str)
args=parser.parse_args()
DNA_DICT={"a":"T",
    "t":"A",
    "c":"G",
    "g":"C"}
MY_DNA=str(args.seq.lower())
rev_dna=MY_DNA[::-1]
for i, (k, v) in enumerate(DNA_DICT.items()):
    rev_dna=rev_dna.replace(k,v)

print(rev_dna)
