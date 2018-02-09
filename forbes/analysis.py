#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import pandas as pd

df_2007 = pd.read_csv('H:/python/python-study/forbes/data/forbes_2007.csv', encoding='utf-8')
df_2008 = pd.read_csv('H:/python/python-study/forbes/data/forbes_2008.csv', encoding='utf-8')
df_2009 = pd.read_csv('H:/python/python-study/forbes/data/forbes_2009.csv', encoding='utf-8')
df_2010 = pd.read_csv('H:/python/python-study/forbes/data/forbes_2010.csv', encoding='utf-8')
df_2011 = pd.read_csv('H:/python/python-study/forbes/data/forbes_2011.csv', encoding='utf-8')
df_2012 = pd.read_csv('H:/python/python-study/forbes/data/forbes_2012.csv', encoding='utf-8')
df_2013 = pd.read_csv('H:/python/python-study/forbes/data/forbes_2013.csv', encoding='utf-8')
df_2014 = pd.read_csv('H:/python/python-study/forbes/data/forbes_2014.csv', encoding='utf-8')
df_2015 = pd.read_csv('H:/python/python-study/forbes/data/forbes_2015.csv', encoding='utf-8')
df_2016 = pd.read_csv('H:/python/python-study/forbes/data/forbes_2016.csv', encoding='utf-8')
df_2017 = pd.read_csv('H:/python/python-study/forbes/data/forbes_2017.csv', encoding='utf-8')

# 表头
column_update = ['Year', 'Rank', 'Company_cn_en', 'Country_cn_en', 'Industry_cn', 'Sales', 'Profits', 'Assets',
                 'Market_value']
df_2007.columns = column_update
# 找出Sales列中包含字母的行
df_2007[df_2007['Sales'].str.contains('.*[A-za-z]', regex=True)]
df_2007['Sales'] = df_2007['Sales'].replace('([A-za-z])', '', regex=True)
df_2007.loc[[117, 616, 880], :]

# 找出 Assets 列中包含字母的行
df_2007[df_2007['Assets'].str.contains('.*[A-za-z]', regex=True)]
df_2007['Assets'] = df_2007['Assets'].replace('([A-za-z])', '', regex=True)
# 千分位数字的逗号被识别为string了，需要替换
df_2007['Assets'] = df_2007['Assets'].replace(',', '', regex=True)

# 替换profits中NaN
df_2007[pd.isnull(df_2007['Profits'])]
df_2007['Profits'].fillna(0, inplace=True)
df_2007['Profits'] = df_2007['Profits'].replace('([A-za-z])', '', regex=True)

# 将string类型转换成数字类型
df_2007['Sales'] = pd.to_numeric(df_2007['Sales'])
df_2007['Profits'] = pd.to_numeric(df_2007['Profits'])
df_2007['Assets'] = pd.to_numeric(df_2007['Assets'])

# 拆分公司名称
df_2007['Company_en'], df_2007['Company_cn'] = df_2007['Company_cn_en'].str.split('/', 1).str

# 拆分国家中文和英文
df_2007['Country_cn'], df_2007['Country_en'] = df_2007['Country_cn_en'].str.split('(', 1).str
# 去除末尾的)
df_2007['Country_en'] = df_2007['Country_en'].str.slice(0, -1)
# 替换香港为CN-HK 台湾为CN-TA
df_2007['Country_en'] = df_2007['Country_en'].replace(['HK.*','TA'],['CN-HK','TA'],regex=True)

df_2007['Industry_en'] = ''

columns_sort = ['Year', 'Rank', 'Company_cn_en','Company_en',
                'Company_cn', 'Country_cn_en', 'Country_cn',
                'Country_en', 'Industry_cn', 'Industry_en',
                'Sales', 'Profits', 'Assets', 'Market_value']
df_2007 = df_2007.reindex(columns=columns_sort)
