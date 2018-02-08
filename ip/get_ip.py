#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup
import csv
import socket
import urllib.request as urllib2


def get_ip(page):
    base_url = 'http://www.xicidaili.com/nn/'
    csvfile = open('ips.csv', 'a', errors='ignore', newline='')
    writer = csv.writer(csvfile)
    user_agent = 'IP'
    headers = {'User-agent': user_agent}
    for num in range(1, page + 1):
        url = base_url + str(num)
        print(url)
        print('Now downloading the ' + str(num * 100) + ' ips')
        request = requests.get(url, headers=headers)
        content = request.text
        bs = BeautifulSoup(content, 'html.parser')
        res = bs.find_all('tr')
        for item in res:
            try:
                temp = []
                tds = item.find_all('td')
                temp.append(tds[1].text)
                temp.append(tds[2].text)
                writer.writerow(temp)
            except:
                pass


def IPpool(num):
    socket.setdefaulttimeout(2)
    reader = csv.reader(open('ips.csv'))
    IPpool = []
    for row in reader:
        proxy = row[0] + ':' + row[1]
        proxy_handler = urllib2.ProxyHandler({"http": proxy})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        try:
            html = urllib2.urlopen('http://www.baidu.com')
            IPpool.append([row[0], row[1]])
            print('可用', row[0])
            if (len(IPpool) > num):
                break
        except:
            continue
    return IPpool


if __name__ == '__main__':
    get_ip(1)
    ips = IPpool(10)
    print(ips)
