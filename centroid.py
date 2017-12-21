#!/usr/bin/env python

# conda execute
# env:
#  - python >=3
#  - numpy
#  - scipy
#  - matplotlib
#  - pandas

"""
conda install conda-execute --channel=conda-forge
conda execute -v my_script.py


"""

# import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np
from scipy import ndimage
import sys
from itertools import groupby
from numpy.linalg import multi_dot

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
factors = pd.read_csv("factors.csv",header='infer').as_matrix()
factors_dict = {}
for i in factors:
    # print(i[0])
    factors_dict[i[0]] = i[1:6]

def seqMatrixWitLen(seq):
    a = np.empty(shape=(len(seq),6))
    for i in range(len(seq)):
        a[i][0] = np.arcsin(np.sqrt((i+1.0)/len(seq)))*len(seq)
        a[i][1:6] = factors_dict[seq[i]]
    return a


def seqMatrixWitLen2(seq):
    a = np.empty(shape=(len(seq),6))
    for i in range(len(seq)):
        a[i][0] = np.arcsin(np.sqrt((i+1.0)/len(seq)))*len(seq)
        for j in range(len(factors_dict[seq[i]])):
            a[i][j+1] = factors_dict[seq[i]][j] * np.arcsin(np.sqrt((i+1.0)/len(seq)))

    return a


def seqMatrixNoLen(seq):
    a = np.empty(shape=(len(seq),5))
    for i in range(len(seq)):
        a[i] = factors_dict[seq[i]]
    return a


# if "-not" in sys.argv:
#     # inFile = getOptionValue("-not")
#     prefix = "noLen.csv"
# elif "-with" in sys.argv:
#     # inFile = getOptionValue("-with")
#     prefix = "witLen.csv"
# elif "-with2" in sys.argv:
#     # inFile = getOptionValue("-with2")
#     prefix = "witLen2.csv"


# else:
#     print("\nplease specify input file name using -not or -with <file_name> \n")
#     sys.exit()
# if "-num" in sys.argv:
#     label = getOptionValue("-num")
# else:
#     print("\nplease specify label using -num <int>\n")
#     sys.exit()

if "-o" in sys.argv:
    output = getOptionValue("-o")
else:
    print("\nplease specify output using -o <int>\n")
    sys.exit()

if "-pos" in sys.argv:
    positive = getOptionValue("-pos")
else:
    print("\nplease specify positive using -pos <int>\n")
    sys.exit()

if "-neg" in sys.argv:
    negative = getOptionValue("-neg")
else:
    print("\nplease specify negative using -neg <int>\n")
    sys.exit()

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

def Dolots(seq,outFile,label):
    try:
        ksize=5
        seqLength = len(seq)
        # print(range(ksize))
        for i in range(ksize):
            seq_1 = seq[i:seqLength]
            seq_2 = seq[0:-i]
            line2write = ""
            if i != 0:
                # print(seq[i:seqLength])
                # print(seq[0:-i])

                centroid_1 = seqMatrixWitLen(seq_1).mean(axis=0)
                centroid_2 = seqMatrixWitLen(seq_2).mean(axis=0)
                # print(centroid)
                for i in centroid_1:
                    line2write+= str(i)+","
                line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq_1))[0])+','
                line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq_1))[1])+','
                try:
                    outFile.write(line2write[:-1]+","+label+'\n')
                except:
                    0

                line2write = ""
                for i in centroid_2:
                    line2write+= str(i)+","
                line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq_2))[0])+','
                line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq_2))[1])+','


                try:
                    outFile.write(line2write[:-1]+","+label+'\n')
                except:
                    0
            else:
                centroid = seqMatrixWitLen(seq).mean(axis=0)
                # print(centroid)
                for i in centroid:
                    line2write+= str(i)+","
                line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[0])+','
                line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[1])+','


                try:
                    outFile.write(line2write[:-1]+","+label+'\n')
                except:
                    0

    except:
        0
def doless(seq,outFile,label):
    try:
        line2write=""
        centroid = seqMatrixWitLen(seq).mean(axis=0)
        # print(centroid)
        for i in centroid:
            line2write+= str(i)+","
        line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[0])+','
        line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[1])+','

        try:
            outFile.write(line2write[:-1]+","+label+'\n')
        except:
            0
    except:
        0


with open("train_"+output,"w") as train_out:
    with open("test_"+output,"w") as test_out:
        pos_iterator = fasta_iter(positive)
        neg_iterator = fasta_iter(negative)

        for ff in pos_iterator:
            headerStr, seq = ff
            if random.choice("AAAT") == "A":
                Dolots(seq,train_out,"1")
            else:
                doless(seq,test_out,"1")


        for gg in neg_iterator:
            headerStr, seq = gg
            if random.choice("AAAT") == "A":
                Dolots(seq,train_out,"0")
            else:
                doless(seq,test_out,"0")
