import json
import csv
from geopy.geocoders import Nominatim
def convert(fname):
	f1 = open(fname)
	x = json.load(f1)
	f1.close()
	k = x.keys()
	v = x.values()

	f2 = csv.writer(open('out.csv', 'wb+'))
	geolocator = Nominatim()

	f2.writerow(['station', 'load','latitude','longitude'])

	for i in range(len(k)):
		location = geolocator.geocode(k[i])
		f2.writerow([k[i], int(v[i])],location.latitude,location.longitude)
		

if __name__ == '__main__':
	convert('out.json')
