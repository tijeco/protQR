import sys
from itertools import groupby

def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue

if "-d" in sys.argv:
    pepFile = getOptionValue("-d")
else:
    # input_directory = "data/"
    print("\nplease specify input directory name using -d <file_name> \n")
    sys.exit()

def fasta_iter(fasta_name):
    fh = open(fasta_name)
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        headerStr = header.__next__()[1:].strip().split()[0]#Entire line, add .split[0] for just first column
        seq = "".join(s.strip() for s in faiter.__next__())
        yield (headerStr, seq)

aminoAcids = "A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y"
aaList = aminoAcids.split(',')
def aafreq(sequence):
    length = float(len(sequence))
    freqList = ""
    for i in range(len(aaList)):
        freqList += str(sequence.count(aaList[i])/length)+","

    return freqList[:-1]

title = "label,"+ aminoAcids
sequence_iterator = fasta_iter(pepFile)
with open("out.csv","w") as out:
    out.write(title+"\n") 
    for ff in sequence_iterator:
        headerStr, seq = ff
        out.write(headerStr+","+aafreq(seq)+"\n")
