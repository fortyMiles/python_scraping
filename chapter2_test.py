from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"
html = urlopen(url)
bsObj = BeautifulSoup(html)

name_list = bsObj.find_all("span", {"class": "green"})
for name in name_list:
    print(name.get_text())
