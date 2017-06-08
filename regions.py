#! usr/bin/python
# -*- coding: utf-8 -*-
import os, ast, json, string
from collections import deque
from tools.request import make_requests, make_request

def test_regions():
	print "test regions"

def parse_subregions(soup):
	return []

def dfs_requests(urls, visited):
	if visited is None:
		visited = set()
	for url in urls:
		visited.add(url)
		subregion_urls = get_subregion_urls(url)
		dfs_requests(subregion_urls, visited)
	return visited

def get_subregion_urls(url):
	responses = make_requests([url])
	soup = None
	for response in responses:
		if response != None:
			soup = response
			subregion_urls = parse_subregions(soup)
			return subregion_urls
	return []
