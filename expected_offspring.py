"""A script to find the expected number of offspring with a dominant allele.

This function takes as input a string denoting the number of adult pairs for
each possible allele.  It assumes that each pair has 2 children. The 
probability of each pair having an offspring with the dominant allele is:
AA-AA: 1
AA-Aa: 1
AA-aa: 1
Aa-Aa: .75
Aa-aa: .5
aa-aa: 0
"""
import argparse

parser=argparse.ArgumentParser(description="A function to find the expected"
    "number of offspring with a dominant allele. This function takes as input"
    "a string denoting the number of adult pairs for each possible allele.")
parser.add_argument('-v',nargs='+',help="The number of each allele pair.  "
    "Order is AA-AA AA-Aa AA-aa Aa-Aa Aa-aa aa-aa")
args=parser.parse_args()
population=args.v
population=[int(x) for x in population]
hdhd=population[0]
hdh=population[1]
hdhr=population[2]
hh=population[3]
hhr=population[4]
hrhr=population[5]

print((hdhd+hdh+hdhr+hh*(3/4)+hhr*(1/2))*2)
