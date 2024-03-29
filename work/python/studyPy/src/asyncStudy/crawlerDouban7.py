#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    author      : zhangke
    createTime  : 2019-01-23 11:36
    filename    : crawlerDouban7.py
    info        : 使用async/await来代替
'''
import asyncio
from  time import time
import aiohttp
from lxml import etree

url = 'https://movie.douban.com/top250'
async def fetch_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
          return  await response.text()

async def parse(url):
    page = await fetch_content(url)
    html = etree.HTML(page)

    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result = []

    for element_movie in html.xpath(xpath_movie):
        result.append(element_movie)

    for p in pages:
        fetch_list.append(url + p.get('href'))

    tasks = [fetch_content(url) for url in fetch_list]
    pages = await asyncio.gather(*tasks)
    for page in pages:
        html = etree.HTML(page)
        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)

    for i, movie in enumerate(result, 1):
        title = movie.find(xpath_title).text
        # print(i, title)
def main():
    loop = asyncio.get_event_loop()    
    start = time()    
    for i in range(5):
        loop.run_until_complete(parse(url))
    end = time()
    print ('Cost {} seconds'.format((end - start) / 5))
    loop.close()
if __name__=='__main__':
    main()
### Cost 0.5127902030944824 seconds