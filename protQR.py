# import PIL.ImageDraw as ImageDraw,PIL.Image as Image, PIL.ImageShow as ImageShow
import random
import numpy as np

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

if "-i" in sys.argv:
    inFile = getOptionValue("-i")
else:
    # input_directory = "data/"
    print("\nplease specify input file name using -i <file_name> \n")
    sys.exit()

if "-o" in sys.argv:
    outFile = getOptionValue("-o")
else:
    # input_directory = "data/"
    print("\nplease specify output file name using -o <file_name> \n")
    sys.exit()


sequence = "CRREEQLRIQRSELLEGRNPRGVKMRWLLGIFLIALLACASAKKIPQAEDTEKDQLDLIEEDDNLNEVESNDDVASNEVAGGYTPDPCLKVRCGAGRVCEVNDKGEGECVCIPECPQETDDRRKVCSNHNETWNSDCEVYQMRCYCAEDTEECKTKTYKHVHVDYYGECRDIPKCSEEEMEDFPRRMREWLFNIMQDLAQRSELDDPYLELEKEAERDLAKKWSNAVIWKFCDLDSHPFDRSVSRHELFPIRAPLLAMEHCIAPFLDKCDADDDHRISLKEWGLCLGLKENEIEDKCSAIRDNQ"
sequence1 = "KGDLACYFFHLIPFVCEICHCKSSKMAPPCFTELGKDAKDIFSKGYNFSLVKLDCKTKTRGGMEFTVSGSSNTESGKVSSSLETKYKVPEYGMTLKEKWTTDNVLSTEVAVEDKLIKGSKFSFNGTFVPLTGKKSGVLKSAFKAENVHLNADVDLDMKGPLIHCASVLGLKGWLFGAQSSFDTCKSKVSRCNFALGYSTDDFVLHTNVNDGQEFGAAIYQKVDSNLETGVQLGWAAGNNATAFGLGCVYSLDKDTSLRAKINNTSQIGLGITHKLRDGIKLTLSAMIDGRSFNQGGHKLGIGLDLEA"
sequence2 = "AAACCCCA"


def makeKmers(st,k):
    kmerList = []
    for i in range(len(st)-k+1):
        kmer = st[i:i+k]
        kmerList.append(kmer)
    return kmerList

def kBreuin(st,n):
    kGraph = {}
    nmers = makeKmers(st,n)
    for i in nmers:
        minus1mers = makeKmers(i,n-1)
        merPair = (minus1mers[0],minus1mers[1])
        if merPair not in kGraph:
            kGraph[merPair] = 1
        else:
            kGraph[merPair] +=1
    return kGraph

def printMe(st):
    aminoAcids = "ACDEFGHIKLMNPQRSTVWYXBZ"
    number = 0
    aa2merPos = {}
    line2print = ""

    #NOTE this can also be generalized if number of loops is indicated by k in kmer, makes huge list though as k goes up
    for row in aminoAcids:
        for column in aminoAcids:
            aa2merPos[row+column]=number
            number+=1
    kB = kBreuin(st,2)
    kList =  np.zeros((len(aa2merPos)))
    # print(len(aa2merPos))
    for i in kB:
        pair = i[0]+i[1]
        kList[aa2merPos[pair]]=kB[i]
    for i in kList:
        line2print+=str(i)+","
    # print(line2print)
    return line2print[:-1]
# print(printMe(sequence))
titleList = [None]*529
aa2merPos = {}
line2print = ""

#NOTE this can also be generalized if number of loops is indicated by k in kmer, makes huge list though as k goes up
aminoAcids = "ACDEFGHIKLMNPQRSTVWYXBZ"
number = 0
aa2merPos = {}
for row in aminoAcids:
    for column in aminoAcids:
        aa2merPos[row+column]=number
        number+=1
for i in aa2merPos:
    titleList[aa2merPos[i]] = i
    # print(aa2merPos[i],i,titleList[aa2merPos[i]])
title = ""
for i in titleList:

    title += str(i)+","
# print(title[:-1])

with open(outFile,"w") as out:
    out.write("label,"+title[:-1]+"\n")
    sequence_iterator = fasta_iter(inFile)
    for ff in sequence_iterator:
        headerStr, seq = ff
        out.write(headerStr+","+printMe(seq)+"\n")
