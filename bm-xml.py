#!/usr/bin/env python3

import urllib.request as urllib
import time
import json
from datetime import datetime, timedelta

# pip install beautifulsoup4
from bs4 import BeautifulSoup


links = dict()

phpfile = "bm-cyber-sale-2015.php"
sale_tag = "Cyber_Sale_2015"
max_pages = 112

for x in range(1, max_pages+1):
	try:
		# print(x)
		usock = urllib.urlopen('http://blackmilkclothing.com/collections/all?page=' + str(x))
		html = usock.read()
		# print(html)
		usock.close()

		soup = BeautifulSoup(html)
		# print(soup)
		titles = soup.select(".h6"
	)
		# print(titles)

		for tag in titles:
			a = tag.find('a')
			href = a['href']
			link = "http://blackmilkclothing.com" + href
			name = a.text
			# print(name, link)

			usock = urllib.urlopen(link + '.xml')
			xml = usock.read()
			usock.close()
			xml_soup = BeautifulSoup(xml)

			tag = xml_soup.find('tags')
			img = xml_soup.find('image').find('src').text
			# print(tag.text)
			# print(sale_tag in tag.text)
			if sale_tag in tag.text:
			    # print(tag.text)
			    print(name)
			    links[name] = {'url': link, 'img': img}
			time.sleep(0.25)
	except socket.error as err:
		with open(phpfile, "w") as fh:
			json.dump(links, fh)
		print('socket error', err)
	except urllib.error.URLError as err:
		with open(phpfile, "w") as fh:
			json.dump(links, fh)
		print('URL error', err)


# print(links)

with open(phpfile, "w") as fh:
	json.dump(links, fh)
