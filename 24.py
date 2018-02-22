#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement

num = []
# num.append(input('请输入第一个数：'))
# num.append(input('请输入第二个数：'))
# num.append(input('请输入第三个数：'))
# num.append(input('请输入第四个数：'))
num = ['2', '4', '6', '8']
symbol = (' + ', ' - ', ' * ', ' / ')
# symbol = [' ( ', ' ) ', ' + ', ' - ', ' * ', ' / ']
# s = num + symbol

left_s = '('
right_s = ')'

# 组合数字
num_data = []
for i in permutations(num, 4):
    num_data.append(list(i))

# print(num_data)
# 增加括号处理
# num_data_ex = []
# for i in num_data:
#     i[0] = left_s + i[0]
#     print(i)
#     # for i2 in permutations(str, 5):
#     #     pass
# print(num_data_ex)
# print(1)
# 组合符合
symbol_data = []
for i in combinations_with_replacement(symbol, 3):
    symbol_data.append(i)

# 生成符号组合列表
symbol_data2 = []
for s in symbol:
    for s2 in symbol:
        for s3 in symbol:
            r3 = []
            r3.append(s)
            r3.append(s2)
            r3.append(s3)
            symbol_data2.append(r3)

# print(symbol_data)
# print(symbol_data2)



#
# 生成数字
result = []
blank = ' '
for num in num_data:
    for x in symbol_data:
        str = num[0] + x[0] + num[1] + x[1] + num[2] + x[2] + num[3]
        try:
            if (24 == abs(eval(str))):
                print(str)
                result.append(str)
        except:
            pass

if 0 == len(result):
    print('解不出来')

# print(result)

#
#
#
# sss = [
#     [2, 6, 8, 4],
#     [2, 6, 4, 8],
#     [2, 4, 6, 8],
#     [2, 4, 8, 6],
#     [4, 2, 6, 8],
#     [4, 2, 8, 6],
#     [4, 6, 2, 8],
#     [4, 6, 8, 2],
# ]
#
# l2 = []
# # 组装参数
# for n1 in l:
#     pass
#
# symbol = ('+', '-', '*', '/')
#
# r2 = []
#
# # 生成符号组合列表
# for s in symbol:
#     for s2 in symbol:
#         for s3 in symbol:
#             r3 = []
#             r3.append(s)
#             r3.append(s2)
#             r3.append(s3)
#             r2.append(r3)
#
# # 生成数字
# result = []
# blank = ' '
# for num in l2:
#     for x in r2:
#         str = num[0] + blank + x[0] + blank + num[1] + blank + x[1] + blank + num[2] + blank + x[2] + blank + num[3]
#         try:
#             if (24 == abs(eval(str))):
#                 result.append(str)
#         except:
#             pass
#
# print(result)
