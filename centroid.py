#!/usr/bin/env python

# conda execute
# env:
#  - python >=3
#  - numpy
#  - scipy
#  - matplotlib

"""
conda install conda-execute --channel=conda-forge
conda execute -v my_script.py


"""

import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np
from scipy import ndimage



import sys
from itertools import groupby

def fasta_iter(fasta_name):
    fh = open(fasta_name)
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        headerStr = header.__next__()[1:].strip().split()[0]#Entire line, add .split[0] for just first column
        seq = "".join(s.strip() for s in faiter.__next__())
        yield (headerStr, seq)

def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue

if "-not" in sys.argv:
    inFile = getOptionValue("-not")
    prefix = "noLen.csv"
elif "-with" in sys.argv:
    inFile = getOptionValue("-with")
    prefix = "witLen.csv"



else:
    # input_directory = "data/"
    print("\nplease specify input file name using -not or -with <file_name> \n")
    # sys.exit()


factors = pd.read_csv("factors.csv",header='infer').as_matrix()
factors_dict = {}
for i in factors:
    # print(i[0])
    factors_dict[i[0]] = i[1:6]

def randProt(n,seq):
    prot=""
    for i in range(n):
        prot+=random.choice(seq)
    return prot

def seqMatrixWitLen(seq):
    a = np.empty(shape=(len(seq),6))
    for i in range(len(seq)):
        a[i][0] = np.arcsin(np.sqrt((i+1.0)/len(seq)))*len(seq)
        a[i][1:6] = factors_dict[seq[i]]
    return a
def seqMatrixNoLen(seq):
    a = np.empty(shape=(len(seq),5))
    for i in range(len(seq)):
        a[i] = factors_dict[seq[i]]
    return a
with open(inFile.strip().split(".")[0]+"_"+prefix,"w") as out:
    sequence_iterator = fasta_iter(inFile)
    for ff in sequence_iterator:
        seq, headerStr = ff
        line2write = ""
        if prefix == "noLen.csv"
            try:
                centroid = seqMatrixNoLen(seq).mean(axis=0)
                for i in centroid:
                    line2write+= i+","
            except:
                print("error with" +seq)
        elif prefix == "witLen.csv":
            try:
                centroid = seqMatrixWitLen(seq).mean(axis=0)
                for i in centroid:
                    line2write+= i+","
            except:
                print("error with" +seq)
        out.write(line2write[:-1]+'\n')


# aa1 = "IIII"
# aa2 = "IIILLLLL"
# seq1=seqMatrixWitLen(aa1)
# seq2 = seqMatrixWitLen(aa2)
# seq3 = seqMatrixNoLen(aa1)
# seq4 = seqMatrixNoLen(aa2)
#
#
# # print(randMat.shape[1])
# mean1 = seq1.mean(axis=0)
# mean2 = seq2.mean(axis=0)
# mean3 = seq3.mean(axis=0)
# mean4 = seq4.mean(axis=0)
#
#
# dist1 = np.linalg.norm(mean1-mean2)
# # dist2 = np.linalg.norm(mean3,mean4)
# # print(np.linalg.norm(mean3-mean4))
# dist2 = np.linalg.norm(mean3-mean4)
# print(dist1)
# print(dist2)
# # print(dist2)
