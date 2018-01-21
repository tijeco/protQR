from itertools import groupby
import sys


def fasta_iter(fasta_name):
    fh = open(fasta_name)
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        headerStr = header.__next__()[1:].strip().split()[0]#Entire line, add .split[0] for just first column
        seq = "".join(s.strip() for s in faiter.__next__())
        yield (headerStr, seq)
input_file = sys.argv[1]
# input_fasta = fasta_iter(sys.argv[1])
input_fasta = fasta_iter(input_file)
with open(input_file+".txt","w") as out:
    for ff in input_fasta:
        headerStr, seq = ff
        out.write(headerStr+"\tblank\t"+seq+"\n")
