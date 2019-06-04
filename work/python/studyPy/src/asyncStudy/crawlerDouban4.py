#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    author      : zhangke
    createTime  : 2019-01-23 11:19
    filename    : crawlerDouban4.py
    info        : 多线程的方式
'''
import requests
from lxml import etree
from time import time
from threading import Thread

url = 'https://movie.douban.com/top250'

def fetch_page(url):
    response = requests.get(url)
    return response
def parse(url):
    response = fetch_page(url)
    page = response.content
    html = etree.HTML(page)

    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result = []

    def fetch_content(url):
        response = fetch_page(url)
        page = response.content
        html = etree.HTML(page)
        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)

    threads = []
    for url in fetch_list:
        t = Thread(target=fetch_content,args=[url])
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    for i, movie in enumerate(result, 1):
        title = movie.find(xpath_title).text
if __name__=='__main__':
    from time import time
    start = time()
    for i in range(5):
        parse(url)
    end = time()
    print('Cost {} seconds'.format((end - start) / 5))
## Cost 0.28850641250610354 seconds