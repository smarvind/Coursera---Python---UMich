import urllib
import json

url = "http://python-data.dr-chuck.net/geojson?"
n = 0 
while (n < 1):
	x = "Universidad Nacional Autonoma de Mexico"
	n += 1
	url1 = url + urllib.urlencode({'sensor' : 'false', 'address' : x})
	w = urllib.urlopen(url1)
	y = w.read()
	js = json.loads(str(y))

	print js['results'][0]['place_id']
		

	#print "place_id", js['results'][0]
	
