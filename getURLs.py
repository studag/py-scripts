import urllib.request, re

source = urllib.request.urlopen('http://www.alamy.com/stock-photography/592ECF6A-DB00-4E26-A6D1-A23694301F1C/1/Stuart%20Dagnall.html').read()
#source = 'bob.png wdw dwdwdwdwdwd w wdwdwdw d.png'
#print (source)
## every image name is an abbreviation composed by capital letters, so...
#for link in re.findall('\S*.jpg', source.decode('utf-8')):
for link in re.findall('http\S*.jpg', source.decode('utf-8')):
  print (link)
