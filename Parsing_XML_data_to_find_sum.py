import urllib
import xml.etree.ElementTree as ET

url = "http://python-data.dr-chuck.net/comments_200826.xml"


data = urllib.urlopen(url).read()
#print data
extract = ET.fromstring(data)
	
x = extract.findall("comments/comment/count")
b =[]
for i in x:
	a = int(i.text)
	b.append(a)

print sum(b)

