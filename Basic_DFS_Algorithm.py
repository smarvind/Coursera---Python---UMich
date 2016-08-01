import urllib
from BeautifulSoup import *
import pdb

url = raw_input(" Enter URL: ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
y =[]
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
	#pdb.set_trace()
	a = str(tag.get('href', None))
	#pdb.set_trace()
	y.append(a)
w = y[17]
print "Enter count: 7"
print "Enter position: 18"
print "Retrieving:", url
print "Retrieving:",  w
n = 0
while n<6:
	html1 = urllib.urlopen(w).read()
	#print html1
	soup1 = BeautifulSoup(html1)
	r =[]
	# Retrieve all of the anchor tags
	tags1 = soup1('a')
	for tag1 in tags1:
        	#pdb.set_trace()
		#print tag1
        	v = str(tag1.get('href', None))
        	#pdb.set_trace()
        	r.append(v)
	w = r[17]
	print "Retrieving:",w
	n += 1
	


