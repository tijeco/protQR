# import PIL.ImageDraw as ImageDraw,PIL.Image as Image, PIL.ImageShow as ImageShow
import random
sequence = "CRREEQLRIQRSELLEGRNPRGVKMRWLLGIFLIALLACASAKKIPQAEDTEKDQLDLIEEDDNLNEVESNDDVASNEVAGGYTPDPCLKVRCGAGRVCEVNDKGEGECVCIPECPQETDDRRKVCSNHNETWNSDCEVYQMRCYCAEDTEECKTKTYKHVHVDYYGECRDIPKCSEEEMEDFPRRMREWLFNIMQDLAQRSELDDPYLELEKEAERDLAKKWSNAVIWKFCDLDSHPFDRSVSRHELFPIRAPLLAMEHCIAPFLDKCDADDDHRISLKEWGLCLGLKENEIEDKCSAIRDNQ"
sequence1 = "KGDLACYFFHLIPFVCEICHCKSSKMAPPCFTELGKDAKDIFSKGYNFSLVKLDCKTKTRGGMEFTVSGSSNTESGKVSSSLETKYKVPEYGMTLKEKWTTDNVLSTEVAVEDKLIKGSKFSFNGTFVPLTGKKSGVLKSAFKAENVHLNADVDLDMKGPLIHCASVLGLKGWLFGAQSSFDTCKSKVSRCNFALGYSTDDFVLHTNVNDGQEFGAAIYQKVDSNLETGVQLGWAAGNNATAFGLGCVYSLDKDTSLRAKINNTSQIGLGITHKLRDGIKLTLSAMIDGRSFNQGGHKLGIGLDLEA"
rando = ""
sequence2 = "AAACCCCA"
aminoAcids = "ACDEFGHIKLMNPQRSTVWY"
for i in range(300):
    rando += random.choice(aminoAcids)
#print(rando)
number = 0
aa2merPos = {}
for row in aminoAcids:
    for column in aminoAcids:
        # print(row,column, number)
        aa2merPos[row+column]=number
        number+=1

# print(aa2merPos)

def makeKmers(st,k):
    kmerList = []
    for i in range(len(st)-k+1):
        kmer = st[i:i+k]
        kmerList.append(kmer)
        # if kmer not in kmerDict:
        #     kmerDict[kmer] = 1
        # else:
        #     kmerDict[kmer]+=1
    return kmerList
# print(makeKmers(sequence2,3))
pairs = {}
def kBreuin(st,n):
    print("BEGIN")
    dt = makeKmers(st,n)
    for i in dt:
        # print(i,n)
        print(makeKmers(i,n-1))


        if(n-1>=3):
            kBreuin(i,n-1)
        else:
            print(i,"FAIL",makeKmers(i,n-1))
            dupley = (makeKmers(i,n-1)[0],makeKmers(i,n-1)[1])
            print(dupley)
            print(dupley in pairs)
            try:
                pairs[dupley]+=1
            except:
                pairs[dupley]=1
        print(pairs)
            # try:
            #     pairs((makeKmers(i,n-1)[0],makeKmers(i,n-1)[1]))+=1
            # except:
            #     pairs((makeKmers(i,n-1)[0],makeKmers(i,n-1)[1]))=1

        # try:
        #     print(kBreuin(i,n-1))
        # except:
        #     print(makeKmers(i,n-1))
            # try:
            #     # pairs[makeKmers(i,n-1)] = 1
            # except:

                # pairs[makeKmers(i,n-1)] += 1
    # return pairs

# def deBleh(st,k):
#     dt = makeKmers(st,k)
#     deBruignGraph = {}
#     for i in dt:
#         # nextDownMer = makeKmers(i,k-1)
#         nextMerPair = (i[0:2],i[1:3])
#         if nextMerPair not in deBruignGraph:
#             deBruignGraph[nextMerPair] = 1
#         else:
#             deBruignGraph[nextMerPair] += 1
#     return deBruignGraph
print(sequence2)
print(makeKmers(sequence2,3))
print(kBreuin(sequence2,6))
# print(deBleh(sequence2,3))
# print(deBleh(sequence2,3))
# seqDeBleh = deBleh(rando,3)
# im = Image.new("RGB", (400,400))
# draw = ImageDraw.Draw(im)
# draw.rectangle ((0, 400, 400, 0), (95,215,214))
# for i in seqDeBleh.keys():
#     print(aa2merPos[i[0]],aa2merPos[i[1]],seqDeBleh[i])
#
#
#
#
#     draw.point((aa2merPos[i[0]],aa2merPos[i[1]]))

#Background & Island

# draw.ellipse ((50, 170, 350, 250), (29,108,29))
# draw.ellipse ((300, 30, 360, 90), (245,245,89))
# draw.rectangle ((0, 300, 400, 200), (15,16,134))


# im.show()
