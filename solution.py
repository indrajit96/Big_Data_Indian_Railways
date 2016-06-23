from __future__ import division

import csv
import sys
import json

ifile  = open('data1.csv', "rb")
reader = csv.reader(ifile)
cnt=0
cnt2=0
rownum = 0
max1=0
stations = []
lf = {'station':'load'}
for row in reader:
    if row[4] in stations:
        lf[row[4]] += 1
        if lf[row[4]] > max1:
        	max1=lf[row[4]]
    else:
        stations.append(row[4])
        cnt2 += 1
        lf[row[4]] = 1


with open('output11.txt', "a") as input_file:
        for k, v in lf.items():
            line = '{}, {}'.format(k, v) 
            print(line, file = input_file)

ifile.close()
        
        
