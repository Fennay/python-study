#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from random import randrange, choice  # generate and place new tile

field = [[0 for i in range(4)] for j in range(4)]

t = [(i,j) for i in range(4) for j in range(4) if field[i][j] == 0]