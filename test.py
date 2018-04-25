import csv

cr = csv.reader(open("train.csv","rb"))
li=[]
flag=True
for row in cr:
    if flag:
        for n in range(0,len(row)):
            li.append([])
        flag=False
    for n in range(0,len(row)):
        li[n].append(row[n])

