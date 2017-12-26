import sys
line1 = True
max_dict = {}
min_dict = {}
with open(sys.argv[1]) as f:

    for line in f:
        if line1:
            line1 == False
            continue
        row = line.strip().split(",")
        for i in range(len(row[-1])):
            if i in min_dict:
                if min_dict[i] > row[i]:
                    min_dict[i] = row[i]
            else:
                min_dict = row[i]
            if i in max_dict:
                if max_dict[i] < row[i]:
                    max_dict[i] = row[i]
                else:
                    max_dict = row[i]

print(min_dict)
print(max_dict)
