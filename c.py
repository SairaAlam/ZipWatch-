import csv
import sys

with open ('C://testcsv.csv',newline='')as f:
    rowcount=0
    sum=0
    average=0
    reader=csv.reader(f)
    for row in reader:
         n=float(column)
        sum+=n
            rowcount+=1
        average=sum/len(column)
        print(average)