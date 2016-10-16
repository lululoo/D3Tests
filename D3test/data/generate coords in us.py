import random
import sys

westOffset = 30; #irvine 30,-91 ; nj 40, -74
northOffset = -91;

def randomLatLng():
	rLat = random.random() * 10 + westOffset;
	rLng = random.random() * 17 + northOffset;	
	return [rLat,rLng];


if (len(sys.argv) > 1):
	for i in range(0, int(sys.argv[1])):
		coord = randomLatLng();
		print str(coord[0]) + ', ' + str(coord[1])
else:
	print randomLatLng();