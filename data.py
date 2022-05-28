import pandas as pd 
import csv

file1="bright_stars.csv"
file2="dwarf_stars.csv"

d1=[]
d2=[]

with open(file1, "r") as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        d1.append(i)

with open(file2, "r") as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        d2.append(i)

h1=d1[0]
h2=d2[0]
p_d1=d1[1:]
d_d2=d2[1:]
h=h1+h2
p_d=[]

for i in p_d1:
    p_d.append(i)

for j in p_d2:
    p_d.append(j)

with open("scrapper_2.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(p_d)
