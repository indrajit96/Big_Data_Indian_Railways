import csv

ifile  = open('data1.csv', "rb")
reader = csv.reader(ifile)
cnt=0
rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
        	if header[colnum]=='station Code':
        		cnt += 1	
           colnum += 1
            
    rownum += 1
print cnt;
ifile.close()
