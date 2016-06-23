import json
import csv

def convert(fname):
	f1 = open(fname)
	x = json.load(f1)
	f1.close()
	k = x.keys()
	v = x.values()

	f2 = csv.writer(open('outnew.csv', 'wb+'))
	f2.writerow(['station', 'load'])

	for i in range(len(k)):
		f2.writerow([k[i], int(v[i])])

if __name__ == '__main__':
	convert('out.json')
