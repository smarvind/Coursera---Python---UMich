import urllib
import json

url = urllib.urlopen("http://python-data.dr-chuck.net/comments_200830.json").read()

js = json.loads(url)
x = []
for i in js["comments"]:
	b = int(i["count"])
	x.append(b)
print sum(x)


