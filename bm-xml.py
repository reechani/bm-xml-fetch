#!/usr/bin/env python3

import sys
import getopt
import urllib.request as urllib
import time
import json
from datetime import datetime, timedelta

# pip install beautifulsoup4
from bs4 import BeautifulSoup

base_url = 'http://blackmilkclothing.com'
collection_path = '/collections/all'


# TODO:
# error handlig
# set baseurl if us

# once to get nr of pages
def get_nr_pages(url):
	# TODO: add error handling
	# right now it's ok that it's not here, this is not item critical
	usock = urllib.urlopen(url)
	html = usock.read()
	usock.close()

	soup = BeautifulSoup(html)
	list_soup = soup.select('.pagination-custom li')
	next_to_last = len(list_soup) - 2
	last_page = int(list_soup[next_to_last].find('a').text)

	return last_page


# for every page to get all items on that page
def read_collection_page(page, url):
	# TODO: add error handling
	url = url + '?page=' + str(page)
	usock = urllib.urlopen(url)
	html = usock.read()
	usock.close()

	soup = BeautifulSoup(html)
	titles = soup.select(".h6")

	return titles


# for every item, pause after each of these
def check_item_xml_for_tag(url, tag):
	# TODO: add error handling
	usock = urllib.urlopen(url + '.xml')
	xml = usock.read()
	usock.close()

	xml_soup = BeautifulSoup(xml)
	tags = xml_soup.find('tags')
	title = xml_soup.title.text

	if tag in tags.text:
		# get image
		img = xml_soup.find('image').find('src').text
		price = xml_soup.find('price').text
		# return the item
		print('found', title)
		return {'name': title, 'url': url, 'img': img, 'price': price}
	else:
		return False


def save_to_file(output_file, data):
	with open(output_file, "w") as fh:
		json.dump(data, fh)
	

def main(argv):
	base_url = 'http://blackmilkclothing.com'
	tag = None
	file = None
	pages = None
	items = dict()
	try:
		opts, args = getopt.getopt(argv, 't:f:', ['us'])
		# print(opts, args)
	except getopt.GetoptError:
		print('nope')
		exit(2)
	for opt, arg in opts:
		if opt == '-t':
			tag = arg
			print('tag:', arg)
		elif opt == '-f':
			file = arg
			print('file:', arg)
		elif opt == '--us':
			base_url = 'http://us.blackmilkclothing.com'
			print('us:', 'yes')
	if tag is None or file is None:
		print('argument missing')
		exit(2)

	pages = get_nr_pages(base_url + collection_path)
	try:
		for x in range(1, pages+1):
			print(x)
			titles = read_collection_page(x, base_url + collection_path)

			for title in titles:
				a = title.find('a')
				href = a['href']
				url = base_url + href
				# name = a.text
				item = check_item_xml_for_tag(url, tag)
				if item != False:
					# save
					items[item['name']] = {'url': item['url'], 'img': item['img'], 'price': item['price']}
					# print(items)
				# pause!
				time.sleep(0.15)
	except socket.error as err:
		save_to_file(file, items)
		print('socket error', err)
	except urllib.error.URLError as err:
		save_to_file(file, items)
		print('URL error', err)
	save_to_file(file, items)


if __name__ == "__main__":
	main(sys.argv[1:])
