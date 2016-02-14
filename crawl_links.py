
import urllib
from BeautifulSoup import *


url = raw_input('Enter - ')
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))

def getlink(url, position):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    return tags[position-1]

for i in xrange(count):
    tag = getlink(url,position)
    url = tag.get('href')
    print url


print tag.contents[0]
