from itertools import groupby
import sys


def fasta_iter(fasta_name):
    fh = open(fasta_name)
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        headerStr = header.__next__()[1:].strip().split()[0]#Entire line, add .split[0] for just first column
        seq = "".join(s.strip() for s in faiter.__next__())
        yield (headerStr, seq)


aa_descript = {
"A":{3:True,4:True,7:True},
"C":{3:True,4:True},
"D":{2:True,9:True,11:True,12:True},
"E":{2:True,9:True,11:True,12:True},
"F":{3:True,4:True,6:True},
"G":{3:True,4:True,7:True},
"H":{3:True,6:True,9:True,10:True,12:True},
"I":{2:True,4:True,9:True,10:True,12:True},
"K":{3:True,4:True,5:True},
"L":{3:True,4:True,5:True},
"M":{3:True,4:True,8:True},
"N":{2:True,8:True,12:True,13:True},
"P":{2:True,8:True},
"Q":{2:True,8:True,12:True,13:True},
"R":{2:True,9:True,10:True,12:True},
"S":{2:True,4:True,7:True,12:True},
"T":{3:True,8:True,12:True},
"V":{3:True,4:True,5:True},
"W":{3:True,4:True,6:True,12:True},
"Y":{3:True,6:True,12:True}

}
# print(aa_descript)

# protein = "MENDEL"

def makeFactors(seq):
    line2write = ""
    header2write = ""
    quarter_len = int(len(seq)/4)
    factor_dict = {}
    #NOTE 6-71 deal with 2
    current_number = 2
    for feature in range(2,14):
        for i in range(1,67):
            num = (i+5)
            if (num <17 or num >19):
                current_factor = (   (66*(feature - 1)) - 66  ) +(i+5)
                current_class = feature

                # print(i,current_class,current_factor)
                if i==1:
                    #total number of current_class
                    tot_num = 0
                    for i in seq:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",tot_num)
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)) +","

                    # None
                if i==2:
                    tot_num = 0
                    for i in seq:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num)/len(seq))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)/len(seq)) +","
                if i==3:
                    tot_num = 0
                    seq_q1 = seq[0:quarter_len]
                    for i in seq_q1:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)) +","
                if i==4:
                    tot_num = 0
                    seq_q2 = seq[quarter_len:2*quarter_len]
                    for i in seq_q2:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)) +","
                if i==5:
                    tot_num = 0
                    seq_q3 = seq[2*quarter_len:3*quarter_len]
                    for i in seq_q3:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)) +","
                if i==6:
                    tot_num = 0
                    seq_q4 = seq[3*quarter_len:]
                    for i in seq_q4:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)) +","
                if i==7:
                    tot_num = 0
                    seq_q1 = seq[0:quarter_len]
                    for i in seq_q1:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num)/len(seq))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)/len(seq)) +","
                if i==8:
                    tot_num = 0
                    seq_q2 = seq[quarter_len:2*quarter_len]
                    for i in seq_q2:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num)/len(seq))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)/len(seq)) +","
                if i==9:
                    tot_num = 0
                    seq_q3 = seq[2*quarter_len:3*quarter_len]
                    for i in seq_q3:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num)/len(seq))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)/len(seq)) +","
                if i==10:
                    tot_num = 0
                    seq_q4 = seq[3*quarter_len:]
                    for i in seq_q4:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num)/len(seq))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)/len(seq)) +","
                if i==11:
                    q1_num = 0
                    seq_q1 = seq[0:quarter_len]
                    for i in seq_q1:
                        if current_class in aa_descript[i]:
                            q1_num+=1
                    tot_num = 0
                    for i in seq:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    if tot_num == 0:
                        # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",0.0)
                        header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                        line2write+=str(0.0) +","
                    else:
                        # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",q1_num/tot_num)
                        header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                        line2write+=str(float(q1_num)/tot_num) +","
                # if i==12:
                #     # print("@@@@@@@@@@@@@@@@@")
                # if i==13:
                #     # print("@@@@@@@@@@@@@@@@@")
                # if i==14:
                    # print("@@@@@@@@@@@@@@@@@")
                if i==15:
                    tot_num = 0
                    seq_half1 = seq[0:2*quarter_len]
                    for i in seq_half1:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)) +","
                if i==16:
                    tot_num = 0
                    seq_q1_3 = seq[0:3*quarter_len]
                    for i in seq_q1_3:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)) +","
                if i==17:
                    tot_num = 0
                    seq_q2_3 = seq[quarter_len:3*quarter_len]
                    for i in seq_q2_3:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)) +","
                if i==18:
                    tot_num = 0
                    seq_half2 = seq[2*quarter_len:]
                    for i in seq_half2:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)) +","
                if i==19:
                    tot_num = 0
                    seq_half1 = seq[0:2*quarter_len]
                    for i in seq_half1:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num)/len(seq))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)/len(seq)) +","
                if i==20:
                    tot_num = 0
                    seq_q1_3 = seq[0:3*quarter_len]
                    for i in seq_q1_3:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num)/len(seq))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)/len(seq)) +","
                if i==21:
                    tot_num = 0
                    seq_q2_3 = seq[quarter_len:3*quarter_len]
                    for i in seq_q2_3:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num)/len(seq))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)/len(seq)) +","
                if i==22:
                    tot_num = 0
                    seq_half2 = seq[2*quarter_len:]
                    for i in seq_half2:
                        if current_class in aa_descript[i]:
                            tot_num+=1
                    # print("FACTOR:",current_factor,"CLASS:",current_class,"is:",float(tot_num)/len(seq))
                    header2write+="f"+str(current_factor)+"c"+str(current_class)+","
                    line2write+=str(float(tot_num)/len(seq)) +","

    # print(header2write[:-1])
    return line2write[:-1]




            # print(feature,(i+5)*(feature-1),i+71,(   (66*(feature - 1)) - 66  ) +(i+5) )



input_file = sys.argv[1]
# input_fasta = fasta_iter(sys.argv[1])
input_fasta = fasta_iter(input_file)

with open(input_file+".shahib.csv","w") as out:
    for ff in input_fasta:
        headerStr, seq = ff
        out.write(makeFactors(seq)+","+sys.argv[2]+"\n")
