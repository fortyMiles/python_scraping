from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    work_fine = True

    try:
        html = urlopen(url)
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except HTTPError as e:
        print(e)
    except AttributeError as e:
        work_fine = False

    if work_fine:
        return title
    else:
        return None


def test():
    url = 'http://www.pythonscraping.com/pages/page1.html'
    title = get_title(url)
    if not title:
        print('Title could not be found')
    else:
        print(title)

if __name__ == '__main__':
    test()
