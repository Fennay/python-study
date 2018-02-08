#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 加这行不需要再写plt.show()，直接显示图像出来
# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pymysql

# 连接数据库，获取数据
conn = pymysql.connect(host='10.0.4.117', port=33066, user='root', passwd='QWERT!@#$%', db='test', charset='utf8')
sql = 'select * from `article`;'
df = pd.read_sql(sql, con=conn)

# 将views中的k转化成数字1000
df['views'] = np.array(list(map(lambda x: float(x[:-1]) * 1000 if ('k' in str(x)) else float(x), df['view'])))
# 修改列数据列席
df['views'] = df['views'].astype('float64')
df['answer'] = df['answer'].astype('float64')

# 分析阅读量与回答量二者关系图
ax = df.plot(kind="scatter", y='answer', x='views', s=10, figsize=(9, 6), fontsize=15)
ax.set_xlabel(u'浏览')
ax.set_ylabel(u'回答')
z = np.polyfit(df.views, df.answer, 1)
p = np.poly1d(z)
plt.title('buzhichizhongwen')
plt.plot(df.views, p(df.views), "r--")

# tags_df = df.tags.value_counts().reset_index('count')
# ax = tags_df.plot(x='p_date', y='total', kind='bar', figsize=(9,6), fontsize=15)
# ax.set_ylabel("文章数")
# ax.set_xlabel("")
# ax.legend().set_visible(False)
# # 柱状图上显示数字
# for p in ax.patches:
#     ax.annotate(str(p.get_height()), xy=(p.get_x(), p.get_height()))

# tags_list = np.array(list(map(f,df.tags)))
# 输出图片
plt.show()
