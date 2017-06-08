#! usr/bin/python
# -*- coding: utf-8 -*-
import os, ast, json
import requests
from time import sleep
from bs4 import BeautifulSoup

proxyHost = "proxy.abuyun.com"
proxyPort = "9020"
proxyUser = "HV8L3A06VJP3D43D"
proxyPass = "D6EEE3745DF426C4"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host" : proxyHost,
    "port" : proxyPort,
    "user" : proxyUser,
    "pass" : proxyPass,
    }

proxies = {
	"http":proxyMeta,
	"https":proxyMeta
	}

headers= {
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate, sdch",
	"Accept-Language":"zh-CN,zh;q=0.8",
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive",
	"Referer":"http://www.wine-searcher.com/regions.lml",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"
    }

def html_to_soup(content):
	return BeautifulSoup(content, "html.parser")

def make_request(url):
	try:
	    r = requests.get(url, headers={}, timeout=1, allow_redirects=True, proxies=proxies)
	except requests.exceptions.Timeout:
	    print 'Maybe set up for a retry, or continue in a retry loop'
	except requests.exceptions.TooManyRedirects:
	    print 'Tell the user their URL was bad and try a different one'
	except requests.exceptions.RequestException as e:
	    print 'catastrophic error. bail.'
	else:
	    sleep(0.1)
	    print r.status_code
	    if r.status_code == requests.codes.ok:
	    	return html_to_soup(r.text)

def make_requests(urls):
	while len(urls)>0:
		url = urls.popleft()
		soup = make_request(url)
		if soup == None:
			urls.append(url)
		else:
			yield soup
 
