import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_42.xml'
count = 0
sum = 0


address = raw_input('Enter location: ')
if len(address) < 1 :
    url = serviceurl
else:      
    url = address

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

counts = tree.findall('.//count')
for one in counts:
    count = count + 1
    sum = sum + int(one.text)

print "Count: ",count
print "Sum: ",sum





