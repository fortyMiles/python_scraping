# The Web Scraping With Python

> Minchiuan Gao 2015-13-Aug
>> Hangzhou, China

A web server is just code, and code can be taken apart, broken into its basic components, re-written, re-userd, and made everything we want. 

	from urllib.request import urlopen
	html = urlopen('http://pythonscraping.com/pages/page1.html')
	print(html.read())


urlopen() could open a remote object across network and read it. It's a farily generic library(HTML files, images files, or any other files)


>> BeautifulSoup

Like in Wonderland namesakes, BeautifulSoup tires to make sense of the nonsensical. It helps format and organize the messy web by fixing bad HTML and presenting us with easily-traverisble Python objects representing XML structures.

Virtually any information can be extracted from any HTML(or XML) file, as long as it has some identifying tag surround it or **near it**

The web is messy. Data is poorly formatted, websites go down, and closing tags go missing. One of the most frustrating experiences in web scraping is to go to sleep with a scraper running, dreaming of all the data you’ll have in your database the next day—only to find out that the scraper hit an error on some unexpected data format and stopped execution shortly after you stopped looking at the screen. 


	if html is None:
		print('URL is not found')
	else:
		# program continues


When the page is existed, there are still some problems.

If you want to access a tag that does not exists, BeautifulSoup will return a None objects. The problem is, attemping to access a tag on a None object itself will result in an AttributeError being thrown.

When writing scarpers, it's important to think about the overall pattern of your code in order to handle exception.
