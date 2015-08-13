from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
else:
    bsObj = BeautifulSoup(html.read())
    print('*'*8)
    print(dir(bsObj))

try:
    content = bsObj.h1
except AttributeError as e:
    print('Tag was not found')
else:
    print(content)
