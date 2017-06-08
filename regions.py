#! usr/bin/python
# -*- coding: utf-8 -*-
import os, ast, json, string
from collections import deque
from tools.request import make_requests, make_request

DONE = True

def dfs_requests(urls, visited):
	if visited is None:
		visited = set()
	for url in urls:
		visited.add(url)
		subregion_urls = get_subregion_urls(url)
		if len(subregion_urls) > 0:
			dfs_requests(subregion_urls, visited)
	return visited

def get_subregion_urls(url):
	if len(url) == 1:
		responses = make_requests([url])
	else:
		return []
	soup = None
	for response in responses:
		if response != None:
			soup = response
			subregion_urls = parse_subregions(soup)
			if subregion_urls == DONE
				return []
			else 
				return subregion_urls
	return []

def parse_subregions(soup):
	if is final:
		return DONE
	else:
		return subregion_urls

def test_regions():
	print "test regions"
