from pyprocessing import *
import math
import sys
from itertools import groupby

from itertools import groupby

def fasta_iter(fasta_name):
    """
    given a fasta file. yield tuples of header, sequence
    """
    fh = open(fasta_name)
    # ditch the boolean (x[0]) and just keep the header or sequence since
    # we know they alternate.
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        # drop the ">"
        header = header.next()[1:].strip().split()[0]
        # join all sequence lines to one.
        seq = "".join(s.strip() for s in faiter.next())
        yield header, seq

pi = math.pi
seqDict = {"A":(0,(2*pi)*0.05),
    "C":((2*pi)*0.10,(2*pi)*0.05),
    "D":((2*pi)*0.10,(2*pi)*0.15),
    "E":((2*pi)*0.20,(2*pi)*0.15),
    "F":((2*pi)*0.20,(2*pi)*0.25),
    "G":((2*pi)*0.30,(2*pi)*0.25),
    "H":((2*pi)*0.30,(2*pi)*0.35),
    "I":((2*pi)*0.40,(2*pi)*0.35),
    "K":((2*pi)*0.40,(2*pi)*0.45),
    "L":((2*pi)*0.50,(2*pi)*0.45),
    "M":((2*pi)*0.50,(2*pi)*0.55),
    "N":((2*pi)*0.60,(2*pi)*0.55),
    "P":((2*pi)*0.60,(2*pi)*0.65),
    "Q":((2*pi)*0.70,(2*pi)*0.65),
    "R":((2*pi)*0.70,(2*pi)*0.75),
    "S":((2*pi)*0.80,(2*pi)*0.75),
    "T":((2*pi)*0.80,(2*pi)*0.85),
    "V":((2*pi)*0.90,(2*pi)*0.85),
    "W":((2*pi)*0.90,(2*pi)*0.95),
    "Y":(2*pi,(2*pi)*0.95)
    }
num = 500
size(num,num)


def make_circle(seq,head):
    arc(num/2, num/2, num, num, 0, 2*pi);


    length = len(seq)
    for i in range(len(seq)):
        print(num/2,num/2,(num-2)*(float(i)/float(length)),(num-2)*(float(i)/float(length)),seqDict[seq[i]][0], seqDict[seq[i]][1])
        arc(num/2,num/2,(num-2)*(float(i)/float(length)),(num-2)*(float(i)/float(length)),seqDict[seq[i]][0], seqDict[seq[i]][1]);
        noFill();
    save(sys.argv[1].strip().split("/")[0]+"/"+head+".png");
    fill(255)

sequence_iterator = fasta_iter(sys.argv[1])
for ff in sequence_iterator:
    headerStr, seq = ff
    try:
        make_circle(seq,headerStr)
    except:
        0
        

sys.exit()
