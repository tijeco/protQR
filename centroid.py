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


if "-not" in sys.argv:
    # inFile = getOptionValue("-not")
    prefix = "noLen.csv"
elif "-with" in sys.argv:
    # inFile = getOptionValue("-with")
    prefix = "witLen.csv"
elif "-with2" in sys.argv:
    # inFile = getOptionValue("-with2")
    prefix = "witLen2.csv"


else:
    print("\nplease specify input file name using -not or -with <file_name> \n")
    sys.exit()
# if "-num" in sys.argv:
#     label = getOptionValue("-num")
# else:
#     print("\nplease specify label using -num <int>\n")
#     sys.exit()

if "-o" in sys.argv:
    output = getOptionValue("-o")+prefix
else:
    print("\nplease specify output using -o <int>\n")
    sys.exit()

if "-pos" in sys.argv:
    positive = getOptionValue("-pos")+prefix
else:
    print("\nplease specify positive using -pos <int>\n")
    sys.exit()

if "-neg" in sys.argv:
    negative = getOptionValue("-neg")+prefix
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





with open("train_"+output,"w") as train_out:
    with open("test_"+output,"w") as test_out:
        pos_iterator = fasta_iter(positive)
        neg_iterator = fasta_iter(negative)

        for ff in pos_iterator:
            headerStr, seq = ff
            if random.choice("AAAT") == "A":
                seqLength = len(seq)
                # print(range(ksize))
                for i in range(ksize):
                    line2write = ""
                    if i != 0:
                        print(seq[i:seqLength])
                        print(seq[0:-i])
                        centroid = seqMatrixWitLen(seq[i:seqLength]).mean(axis=0)
                        # print(centroid)
                        for i in centroid:
                            line2write+= str(i)+","
                        line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq[i:seqLength]))[0])+','
                        line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq[i:seqLength]))[1])+','
                        totDot=[]
                        totDistance = []
                        for i in range(len(seqMatrixWitLen(seq[i:seqLength]))-1):
                            # print(totDot,totDistance)
                            totDot.append(multi_dot([seqMatrixWitLen(seq[i:seqLength])[i], seqMatrixWitLen(seq[i:seqLength])[i+1]]))
                            totDistance.append(np.linalg.norm(seqMatrixWitLen(seq[i:seqLength])[i]-seqMatrixWitLen(seq[i:seqLength])[i+1]))

                        line2write+=str(sum(totDot))+','+str(sum(totDistance))

                        try:
                            train_out.write(line2write[:-1]+","+"1"+'\n')
                        except:
                            0
                    else:
                        centroid = seqMatrixWitLen(seq).mean(axis=0)
                        # print(centroid)
                        for i in centroid:
                            line2write+= str(i)+","
                        line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[0])+','
                        line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[1])+','
                        totDot=[]
                        totDistance = []
                        for i in range(len(seqMatrixWitLen(seq))-1):
                            # print(totDot,totDistance)
                            totDot.append(multi_dot([seqMatrixWitLen(seq)[i], seqMatrixWitLen(seq)[i+1]]))
                            totDistance.append(np.linalg.norm(seqMatrixWitLen(seq)[i]-seqMatrixWitLen(seq)[i+1]))

                        line2write+=str(sum(totDot))+','+str(sum(totDistance))
                        try:
                            train_out.write(line2write[:-1]+","+"1"+'\n')
                        except:
                            0
            else:
                line2write=""
                centroid = seqMatrixWitLen(seq).mean(axis=0)
                # print(centroid)
                for i in centroid:
                    line2write+= str(i)+","
                line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[0])+','
                line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[1])+','
                totDot=[]
                totDistance = []
                for i in range(len(seqMatrixWitLen(seq))-1):
                    # print(totDot,totDistance)
                    totDot.append(multi_dot([seqMatrixWitLen(seq)[i], seqMatrixWitLen(seq)[i+1]]))
                    totDistance.append(np.linalg.norm(seqMatrixWitLen(seq)[i]-seqMatrixWitLen(seq)[i+1]))

                line2write+=str(sum(totDot))+','+str(sum(totDistance))
                try:
                    test_out.write(line2write[:-1]+","+"1"+'\n')
                except:
                    0


        for ff in neg_iterator:
            headerStr, seq = ff
            if random.choice("AAAT") == "A":
                seqLength = len(seq)
                # print(range(ksize))
                for i in range(ksize):
                    line2write = ""
                    if i != 0:
                        # print(seq[i:seqLength])
                        # print(seq[0:-i])
                        centroid = seqMatrixWitLen(seq[i:seqLength]).mean(axis=0)
                        # print(centroid)
                        for i in centroid:
                            line2write+= str(i)+","
                        line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq[i:seqLength]))[0])+','
                        line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq[i:seqLength]))[1])+','
                        totDot=[]
                        totDistance = []
                        for i in range(len(seqMatrixWitLen(seq[i:seqLength]))-1):
                            # print(totDot,totDistance)
                            totDot.append(multi_dot([seqMatrixWitLen(seq[i:seqLength])[i], seqMatrixWitLen(seq[i:seqLength])[i+1]]))
                            totDistance.append(np.linalg.norm(seqMatrixWitLen(seq[i:seqLength])[i]-seqMatrixWitLen(seq[i:seqLength])[i+1]))

                        line2write+=str(sum(totDot))+','+str(sum(totDistance))

                        try:
                            train_out.write(line2write[:-1]+","+"0"+'\n')
                        except:
                            0
                    else:
                        centroid = seqMatrixWitLen(seq).mean(axis=0)
                        # print(centroid)
                        for i in centroid:
                            line2write+= str(i)+","
                        line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[0])+','
                        line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[1])+','
                        totDot=[]
                        totDistance = []
                        for i in range(len(seqMatrixWitLen(seq))-1):
                            # print(totDot,totDistance)
                            totDot.append(multi_dot([seqMatrixWitLen(seq)[i], seqMatrixWitLen(seq)[i+1]]))
                            totDistance.append(np.linalg.norm(seqMatrixWitLen(seq)[i]-seqMatrixWitLen(seq)[i+1]))

                        line2write+=str(sum(totDot))+','+str(sum(totDistance))
                        try:
                            train_out.write(line2write[:-1]+","+"0"+'\n')
                        except:
                            0
            else:
                line2write=""
                centroid = seqMatrixWitLen(seq).mean(axis=0)
                # print(centroid)
                for i in centroid:
                    line2write+= str(i)+","
                line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[0])+','
                line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[1])+','
                totDot=[]
                totDistance = []
                for i in range(len(seqMatrixWitLen(seq))-1):
                    # print(totDot,totDistance)
                    totDot.append(multi_dot([seqMatrixWitLen(seq)[i], seqMatrixWitLen(seq)[i+1]]))
                    totDistance.append(np.linalg.norm(seqMatrixWitLen(seq)[i]-seqMatrixWitLen(seq)[i+1]))

                line2write+=str(sum(totDot))+','+str(sum(totDistance))
                try:
                    test_out.write(line2write[:-1]+","+"0"+'\n')
                except:
                    0



# with open(output,"w") as out:
#     # if prefix == "noLen.csv":
#     #     out.write("label,f1,f2,f3,f4,f5\n")
#     # elif "wit" in prefix:
#     #     0
#         # out.write("label,pos,f1,f2,f3,f4,f5\n")
#     sequence_iterator = fasta_iter(inFile)
#     for ff in sequence_iterator:
#         headerStr, seq = ff
#         # print(seq)
#         line2write = ""
#         # line2write2 = ""
#         # if prefix == "noLen.csv":
#         #
#         #     try:
#         #         centroid = seqMatrixNoLen(seq).mean(axis=0)
#         #
#         #         for i in centroid:
#         #
#         #             line2write+= str(i)+","
#         #         # print("writing stuff")
#         #         out.write(line2write[:-1]+'\n')
#         #     except:
#         #         0
#         #         # print("error with" +seq)
#         elif prefix == "witLen.csv":
#             # out.writ("label,pos,f1,f2,f3,f4,f5")
#             try:
#                 centroid = seqMatrixWitLen(seq).mean(axis=0)
#                 # print(centroid)
#                 for i in centroid:
#                     line2write+= str(i)+","
#                 line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[0])+','
#                 line2write+=str(ndimage.measurements.center_of_mass(seqMatrixWitLen(seq))[1])+','
#                 totDot=[]
#                 totDistance = []
#                 for i in range(len(seqMatrixWitLen(seq))-1):
#                     # print(totDot,totDistance)
#                     totDot.append(multi_dot([seqMatrixWitLen(seq)[i], seqMatrixWitLen(seq)[i+1]]))
#                     totDistance.append(np.linalg.norm(seqMatrixWitLen(seq)[i]-seqMatrixWitLen(seq)[i+1]))
#
#                 line2write+=str(sum(totDot))+','+str(sum(totDistance))
#
#                 # print(line2write+','+label)
#                 try:
#                     out.write(line2write[:-1]+","+label+'\n')
#                 except:
#                     print("error")
#             except:
#                 0
#         # elif prefix == "witLen2.csv":
#         #     try:
#         #         centroid = seqMatrixWitLen2(seq).mean(axis=0)
#         #         # centroid2 = seqMatrixWitLen2(seq[::-1]).mean(axis=0)
#         #
#         #         for i in centroid:
#         #             line2write+= str(i)+","
#         #         # for i in centroid2:
#         #             # line2write2 += str(i)+","
#         #         print("writing stuff",line2write)
#         #         out.write(line2write[:-1]+","+label+'\n')
#         #         # out.write(line2write2[:-1]+'\n')
#         #     except:
#         #         0
#
#                 # print("error with" +seq)
