 !/usr/local/bin/python3

'''
Test of six degree
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())


def get_links(articl_url):
    html = urlopen('http://en.wikipedia.org' + articl_url)
    bs_obj = BeautifulSoup(html)
    return bs_obj.find('div', {'id': 'bodyContent'}).find_all('a',
                        href=re.compile("^(/wiki/)((?!:).)*$"))


def main():
    links = get_links('/wiki/Kevin_Bacon')
    while len(links) > 0:
        new_atrical = links[random.randint(0, len(links)-1)].attrs['href']
        print(new_atrical)
        links = get_links(new_atrical)

if __name__ == '__main__':
    main()
