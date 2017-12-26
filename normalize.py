import sys
line1 = True
max_dict = {}
min_dict = {}
with open(sys.argv[1]) as f:
    next(f)
    for line in f:
        row = line.strip().split(",")
        print(1)
        for i in range(len(row[-1])):
            if i in min_dict:
                if float(min_dict[i]) > row[i]:
                    float(min_dict[i]) = row[i]
            else:
                float(min_dict[i]) = row[i]
            if i in max_dict:
                if float(max_dict[i]) < row[i]:
                    float(max_dict[i]) = row[i]
                else:
                    float(max_dict[i]) = row[i]

print(min_dict)
print(max_dict)
