#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
爬取E宠商城猫商品信息
"""

import os
import sys
import time
import datetime
import urllib.request
import re

def url_request():
    url = 'http://list.epet.com/722b1f1.html'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) \
                   AppleWebKit/537.36 (KHTML, like Gecko) \
                   Chrome/57.0.2987.133 Safari/537.36"}
    try:
        request = urllib.request.Request(url=url,headers=headers)
        response = urllib.request.urlopen(request)
        if response.status == 200:
            return response.read().decode('utf-8')
        else:
            return None
    except:
        return None


def re_findall(content):
    re_compile = re.compile('<span class="title-subject">(.*?)\
</span>.*?<span class="c999 through market-price">(.*?)\
</span>.*?<span class="cred ft16 price">(.*?)</span>.*?\
<span class="c999 dprice">(.*?)</span>',re.S)
    if re.findall(re_compile,url_request()):
        return re.findall(re_compile,content)
    else:
        return None


def file(re_content):
    for eachline in re_content:
        print('商品：{}, 原价: {}, 现价: {}, 单价(元/斤): {}'.format(\
            eachline[0],eachline[1],eachline[2],eachline[3]))


def run(request):
    r_request = url_request()
    if r_request:
        re_content = re_findall(r_request)
        if re_content:
            return file(re_content)
        else:
            return None
    else:
        return None

if __name__ == '__main__':
    run(url_request)
