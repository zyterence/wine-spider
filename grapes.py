#! usr/bin/python
# -*- coding: utf-8 -*-
import os, ast, json, string
from collections import deque
from tools.request import make_requests, make_request

lowercase = string.ascii_lowercase
grapes_url = 'http://www.wine-searcher.com/grapes-{}-{}'
test_url = 'http://www.wine-searcher.com/grapes-a-b'

grapes = []

def get_urls():
	assert len(lowercase) == 26, "There are 26 letters in the alphabet."
	urls = deque()
	for index in xrange(0, 26, 2):
		url = grapes_url.format(lowercase[index], lowercase[index+1])
		urls.append(url)
	return urls

def get_grapes():
	urls = get_urls()
	for soup in make_requests(urls):
		parse_grapes(soup)

def parse_grapes(soup):
	if not soup:
		print "No soup"
		return
	table = soup.find('table', class_='grape-detail tab-zero')
	if not table:
		return "No table tag"
	links = table.find_all('a')
	if not links:
		return "No a tag"
	urls = deque()
	for link in links:
		urls.append(link['href'])
	for soup in make_requests(urls):
		parse_information(soup)

def parse_information(soup):
	if not soup:
		return "No soup"
	info = soup.find('div', {"itemprop":"articleBody"})
	if not info:
		return "No info tag"
	strong = info.find('strong')
	grape = dict()
	grape['name'] = strong.get_text()
	grape['information'] = info.get_text()
	grapes.append(grape)
	print soup.title
	print grape

def test_grapes():
	print 'test_grapes start'
	soup = make_request(test_url)
	if soup == None:
		print "test_parse_grapes request failed!\n" + test_url
	else:
		parse_grapes(soup)
	print 'test_grapes start'
