#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup
import csv


def download(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    response = requests.get(url, headers=headers)
    # print(response.status_code)
    return response.text


def get_content_first_page(html, country='China'):
    '''
    获取China的公司列表，且包含表头
    '''
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    label_div = body.find('div', {'class': 'content post'})
    tables = label_div.find_all('table')
    # tables一共有2个，第一个才是我们想要的数据
    trs = tables[0].find_all('tr')
    # 获取标题行信息
    row_title = [td.text for td in trs[0].find_all('td')]
    row_title.insert(2, 'Country')
    data_list = []
    data_list.append(row_title)
    for i, tr in enumerate(trs):
        if i == 0:
            continue
        tds = tr.find_all('td')
        # 获取公司排名及列表
        row = [item.text.strip() for item in tds]
        row.insert(2, country)
        data_list.append(row)
    return data_list

def get_content_other_country(html, country='China'):
    '''
    获取China的公司列表，且包含表头
    '''
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    label_div = body.find('div', {'class': 'content post'})
    tables = label_div.find_all('table')
    # tables一共有2个，第一个才是我们想要的数据
    trs = tables[0].find_all('tr')
    # 获取标题行信息
    row_title = [td.text for td in trs[0].find_all('td')]
    row_title.insert(2, 'Country')
    data_list = []
    # data_list.append(row_title)
    for i, tr in enumerate(trs):
        if i == 0:
            continue
        tds = tr.find_all('td')
        # 获取公司排名及列表
        row = [item.text.strip() for item in tds]
        row.insert(2, country)
        data_list.append(row)
    return data_list


def get_country_info(html):
    '''
    获取除China外其他国家的网页链接及国家名称
    '''
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    label_div = body.find('div', {'class': 'content post'})
    tables = label_div.find_all('table')
    label_a = tables[1].find_all('a')
    country_names = [item.text for item in label_a]
    page_urls = [item.get('href') for item in label_a]
    country_info = list(zip(country_names, page_urls))
    return country_info


def save_data_to_csv_file(data, file_name):
    '''
    保存数据到csv文件中
    '''
    with open(file_name, 'a', errors='ignore', newline='',encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


def get_forbes_global_year_2013():
    url = 'http://www.economywatch.com/companies/forbes-list/china.html'
    html = download(url)
    # print(html)
    data_first_page = get_content_first_page(html)
    # print(data_first_page)
    print('saving data ...', 'China')
    save_data_to_csv_file(data_first_page, 'forbes_economywatch_2013.csv')
    country_info = get_country_info(html)
    # print(country_info)
    for item in country_info:
        country_name = item[0]
        country_url = item[1]
        if country_name == 'China':
            continue
        html = download(country_url)
        data_other_country = get_content_other_country(html, country_name)
        # print(data_other_country)
        print('saving data ...', country_name)
        save_data_to_csv_file(data_other_country, 'forbes_economywatch_2013.csv')


if __name__ == '__main__':
    # get data from Forbes Global 2000 in Year 2013
    get_forbes_global_year_2013()
