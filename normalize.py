import sys
line1 = True
max_dict = {}
min_dict = {}
with open(sys.argv[1]) as f:

    for line in f:
        if line1:
            line1=False
            continue

        row = line.strip().split(",")
        for i in range(len(row[:-1])):
            if i in max_dict:
                if max_dict[i] < float(row[i]):
                    max_dict[i] = float(row[i])
            else:
                max_dict[i] = float(row[i])
            if i in min_dict:
                if min_dict[i] > float(row[i]):
                    min_dict[i] = float(row[i])
            else:
                min_dict[i] = float(row[i])
# normalized = (x-min(x))/(max(x)-min(x))
# print(min_dict)
# print(max_dict)
line1=True
with open(sys.argv[1].replace("csv","norm.csv"),"w") as out:
    with open(sys.argv[1]) as f:

        for line in f:
            if line1:
                # print(line)
                out.write(line)
                line1=False
                continue

            row = line.strip().split(",")
            line2write=""
            for i in range(len(row[:-1])):
                # 2* (x-min)/(max)
                line2write+=str( 2.0*(float(row[i]) - min_dict[i]) / (max_dict[i]-min_dict[i]) -1.0)+","
                # print(str( 2.0*(float(row[i]) - min_dict[i]) / (max_dict[i]-min_dict[i])),min_dict[i],max_dict[i],row[i])
            # if row[-1] == "0":
            #     line2write += "1\n"
            # if row[-1] == "1":
            #     line2write += "0\n"



            line2write+=(row[-1]+"\n")
            out.write(line2write)
