import urllib
from BeautifulSoup import *
import re 

url = "http://python-data.dr-chuck.net/comments_200829.html"
data = urllib.urlopen(url).read()
s = BeautifulSoup(data)
y = []
tags = s('span')
#print tags
for i in tags:
	print 'TAG:',i
   	x  = int(i.contents[0])
	y.append(x)
	#print sum(y)
  
print sum(y)   	



