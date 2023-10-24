"""This script finds the longest shared motif in a set of DNA sequences.

It works by taking the first sequence and, at each position:
    1. Create a substring of length 1
    2. Check if that substring is in every other sequence
    3. If 2 is true, create a substring that is one base longer

The program stores the identity of the longest substring starting at each 
position and then prints the sequence of the longest one.

This could be made faster by:
    1. Using the shortest sequence rather than the first sequence.
    2. Terminating the program once the longest substring found is longer
    than the remaining positions to be scanned.
"""
from Bio import SeqIO

records=[]
for record in SeqIO.parse("data/ssm2.fasta","fasta"):
    records.append(str(record.seq))
REF=str(records[0])
substrings={}
index=0
# Use this flag to have the program proceed to the next index if it finds a
# common substring at the end of the reference
uncommon_flag=0
# loop through the entire reference; it is probably more efficient to stop
# when we have found a common substring longer than the number of remaining
# reference bases to scan
while index<=(len(REF)-1):
    temp_ss=""
    short_ref=REF[index::]
    uncommon_flag=0
    for base in short_ref:
        temp_ss=temp_ss+base
        #make a list of strings that share the motif
        matches=[match for match in records if temp_ss in match]
        if len(matches)==len(records):
            #update the dictionary with the new longest motif starting at the
            # current index
            substrings[index]=temp_ss
        else:
            #the current motif is not in every record, so exit the loop and
            # move the starting base over by 1
            index+=1
            uncommon_flag=1
            break
    if uncommon_flag==0:
        #need this in case we get to the end of the reference sequence and
        # still have a common motif
        index+=1
print(max(substrings.values(),key=len))
