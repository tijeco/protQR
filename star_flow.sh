ls

which python
python3 fasta2tab.py $1
python star.py $1.txt
# gcut -f1-3 --complement   $1.txt |perl -lpe 's///g; s/^|$//g; s/\t/,/g' > $1.csv
gcut -f1-3 --complement $1.txt.star.txt | perl -lpe 's///g; s/^|$//g; s/\t/,/g' > $1.csv
cut -f1-3 --complement $1.txt.star.txt | perl -lpe 's///g; s/^|$//g; s/\t/,/g' > $1.csv
