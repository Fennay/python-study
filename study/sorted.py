#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from collections import Iterable

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

M = []


def by_name(t):
    return t[1]


ss = sorted(L, key=by_name, reverse=True)

print(ss)


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


sum = calc_sum(1, 2, 3, 4, 55)
print(sum)


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


sum2 = lazy_sum(1, 2, 3, 4, 5, 6, 7)
sum3 = sum2()
print(sum2())
