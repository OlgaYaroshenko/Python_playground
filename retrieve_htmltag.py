
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
content = 0
for tag in tags:
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    #print 'Contents:',int(tag.contents[0])
    #print 'Attrs:',tag.attrs
    count = count + 1
    content = content + int(tag.contents[0])

print "Count ",count
print "Sum ",content