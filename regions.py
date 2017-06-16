#! usr/bin/python
# -*- coding: utf-8 -*-
import os, ast, json, string
from collections import deque
from tools.request import make_requests, make_request

test_url = 'https://www.wine-searcher.com/regions-california'

FINAL = True

def dfs_requests(urls, visited):
	if visited is None:
		visited = set()
	for url in urls:
		visited.add(url)
		subregion_urls = next_subregion_urls(url)
		if len(subregion_urls) > 0:
			dfs_requests(subregion_urls, visited)
	return visited

def next_subregion_urls(url):
	if len(url) == 1:
		responses = make_requests([url])
	else:
		return []
	soup = None
	for response in responses:
		if response != None:
			soup = response
			subregion_urls = parse_subregions(soup)
			if subregion_urls == FINAL:
				return []
			else:
				return subregion_urls
	return []

def parse_subregions(soup):
	if not soup:
		return "No soup"
	region_list = soup.find('ul', class_='top-level')
	if not region_list:
		return FINAL
	else:
		subregion_urls = []
		for a in region_list.find_all('a', href=True):
			subregion_urls.append(a['href'])
		return subregion_urls

def test_regions():
	print "test regions"

def test_parse_subregions():
	for soup in make_requests(deque([test_url])):
		if soup == None:
			print "test_parse_subregions request failed!\n" + test_url
		else:
			subregion_urls = parse_subregions(soup)
			print subregion_urls
