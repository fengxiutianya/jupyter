#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    author      : zhangke
    createTime  : 2019-04-15 11:11
    filename    : demo.py
    info        :  简单使用
'''

from numpy import *

if __name__ == '__main__':
    print(random.rand(4,4))

    randMat = mat(random.rand(4,4))
    print(randMat.I * randMat)
