#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup
import csv
import random

# 基础的路径
base_data_path = './data/'
# 基础域名
basic_url = 'http://wiki.mbalib.com'


# 代理ip
def get_ip():
    list = [['61.135.217.7', '80'], ['122.114.31.177', '808'], ['115.227.134.253', '8118'], ['218.74.29.216', '8118'],
            ['112.249.54.130', '8118'], ['180.120.211.9', '808'], ['110.248.98.62', '8118'], ['119.98.209.28', '8118'],
            ['117.62.233.122', '808'], ['121.233.208.103', '8118'], ['139.226.56.230', '8118']]
    ip = random.sample(list, 1)
    return ip


def download(url):
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    # ip = get_ip()
    # ip = ip[0][0] + ':' + ip[0][1]
    ip = '61.135.217.7:80'
    proxies = {"http": "http://" + ip, "https": "http://" + ip, }
    response = requests.get(url, headers=headers,proxies=proxies)
    return response.text


def get_content_first_page(html, year):
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    body_content = body.find('div', {'id': 'bodyContent'})
    tables = body_content.find_all('table', {'class': 'wikitable'})

    # 获取所有的行
    trs = tables[-1].find_all('tr')
    row_title = [item.text.strip() for item in trs[1].find_all('th')]

    rank_list = []
    rank_list.append(row_title)
    for i, tr in enumerate(trs):
        # if 0 == i:
        if 0 == i or 1 == i:
            continue
        tds = tr.find_all('td')

        # 获取公司的排名及列表
        row = [item.text.strip() for item in tds]
        row.insert(0, year)
        rank_list.append(row)

    return rank_list


# 爬去其他页面内容
def get_content_other_page(html, year):
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    body_content = body.find('div', {'id': 'bodyContent'})
    tables = body_content.find_all('table', {'class': 'wikitable'})

    # 获取所有的行
    trs = tables[0].find_all('tr')
    # row_title = [item.text.strip() for item in trs[0].find_all('th')]
    # row_title.insert(0, '年份')

    rank_list = []
    # rank_list.append(row_title)
    for i, tr in enumerate(trs):
        if 0 == i or 1 == i:
        # if 0 == i:
            continue
        tds = tr.find_all('td')

        # 获取公司的排名及列表
        row = [item.text.strip() for item in tds]
        row.insert(0, year)
        rank_list.append(row)

    return rank_list


def get_page_urls(html):
    basic_url = 'http://wiki.mbalib.com'
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    body_content = body.find('div', {'id': 'bodyContent'})
    label_div = body_content.find('div', {'align': 'center'})
    label_a = label_div.find('p').find('b').find_all('a')
    page_urls = [basic_url + item.get('href') for item in label_a]
    return page_urls


# 存储到csv
def save_date_to_csv_file(data, file_name):
    with open(file_name, 'a', errors='ignore', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


def get_forbes_global_year_2007(year=2007):
    url = 'http://wiki.mbalib.com/wiki/2007%E3%80%8A%E7%A6%8F%E5%B8%83%E6%96%AF%E3%80%8B%E5%85%A8%E7%90%83%E4%B8%8A%E5%B8%82%E5%85%AC%E5%8F%B82000%E5%BC%BA'
    html = download(url)
    data_first_page = get_content_first_page(html, year)
    # 存储入库
    save_date_to_csv_file(data_first_page, base_data_path + 'forbes_' + str(year) + '.csv')

    page_urls = get_page_urls(html)
    for url in page_urls:
        html = download(url)
        data_other_page = get_content_other_page(html, year)
        print('saving data ...', url)
        save_date_to_csv_file(data_other_page, base_data_path + 'forbes_' + str(year) + '.csv')


if __name__ == '__main__':
    get_forbes_global_year_2007(2007)
