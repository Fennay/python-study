#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import *


def main():
    # lst = [[1, 3, 5], [2, 4, 6]]
    # np_lst = np.array(lst)
    # print(type(np_lst))
    # np_list = np.array(lst,dtype=np.float)
    # print(np_list.shape)
    # print(np_list.ndim)
    # print(np_list.dtype)
    # print(np_list.itemsize)
    # print(np_list.size)

    # print(np.zeros([2, 4]))
    # print(np.ones([5,6]))
    # print(np.random.rand(2,4))
    # print(np.random.randint(1,10,3))
    # print(np.random.randn(2,4))
    # print(np.random.choice([10,20,30,40,50]))
    # print(np.random.beta(1, 10, 100))
    # lst = np.arange(1, 11).reshape([5, -1])
    # print(lst)
    # print('-------1111------')
    # lst.reshape([2, -1])
    # print(lst)
    lst = np.array(
        [
            [
                [1, 2, 3, 4],
                [4, 5, 6, 7]
            ],
            [
                [7, 8, 9, 10],
                [10, 11, 12, 13]
            ],
            [
                [14, 15, 16, 17],
                [18, 19, 20, 21]
            ]
        ])
    # print(lst.max(axis=2))

    lst = np.array([[1., 2.], [3., 4.]])
    y = np.array([[5.], [7.]])
    print(solve(lst, y))


if __name__ == "__main__":
    main()
