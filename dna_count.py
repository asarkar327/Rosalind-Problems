"""A counter that returns the count of each nucleotide in a sequence.
"""
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("seq",type=str)
args=parser.parse_args()
MY_DNA=str(args.seq.upper())
A_COUNT=MY_DNA.count("A")
C_COUNT=MY_DNA.count("C")
G_COUNT=MY_DNA.count("G")
T_COUNT=MY_DNA.count("T")
print(f"{A_COUNT} {C_COUNT} {G_COUNT} {T_COUNT}")