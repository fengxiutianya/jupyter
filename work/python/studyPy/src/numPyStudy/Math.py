#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    author      : zhangke
    createTime  : 2019-04-16 14:28
    filename    : Math.py
    info        : 学习数学计算
'''
import numpy as np
import  operator
def squre():
    a = np.array([[2,12,2],[2,2,2]])
    print(np.square(a))
    print(a**2)




if __name__ == '__main__':
    # squre()
    te = {"te":4,"tee":3}
    s = sorted(te.items(),key=operator.itemgetter(1),reverse=True)
    print(s)