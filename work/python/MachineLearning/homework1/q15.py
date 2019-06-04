#!/usr/bin/env python3
# -*- coding=utf-8 -*-
'''
用于实现一个简单的pla
'''
import os
import re
import random


def getData(path):
    # 这一步要特别注意一点，所有的向量现在需要在向量里面加上x0，默认为1
    ret = []
    with open(path, "r") as f:
        for line in f.readlines():
            tem = [1]
            for x in re.split(r'[\s]', line.strip()):
                tem.append(float(x))
            ret.append(tem)
        return ret


def sign(n):
    if n <= 0:
        return -1
    return 1


def multiply_wx(w, x, n):
    sum = 0
    for i in range(n):
        sum += w[i] * x[i]
    return sum


def multiply_xy(x, n):
    xy = []
    for i in range(n):
        xy.append(x[i] * x[n])
    return xy


def add(w, xy, n):
    w1 = []
    for i in range(n):
        w1.append(w[i] + xy[i])
    return w1


def add17(w, xy, n):
    w1 = []
    for i in range(n):
        w1.append(w[i] + 0.5 * xy[i])
    return w1


def pla():
    # 获取数据
    ret = getData("q15.txt")
    n = len(ret)

    # 进行计算

    # 修正的次数
    step = 0

    # 当前操作的索引
    index = 0
    # 连续正确的次数
    correctNum = 0

    isFinished = False
    test = 0
    w = [0, 0, 0, 0, 0]  # 默认w向量
    while not isFinished:
        x = ret[index]
        sum = multiply_wx(w, x, 5)
        if x[5] == sign(sum):
            correctNum += 1
        else:
            xy = multiply_xy(x, 5)
            w = add(w, xy, 5)
            step += 1
            correctNum = 0
        if index == (n - 1):
            index = 0
        else:
            index += 1
        if correctNum == n:
            isFinished = True
    return step


def pla16():
     # 获取数据
    ret = getData("q15.txt")
    n = len(ret)
    random.shuffle(ret)
    # 进行计算

    # 修正的次数
    step = 0

    # 当前操作的索引
    index = 0
    # 连续正确的次数
    correctNum = 0

    isFinished = False
    test = 0
    w = [0, 0, 0, 0, 0]  # 默认w向量
    while not isFinished:
        x = ret[index]
        sum = multiply_wx(w, x, 5)
        if x[5] == sign(sum):
            correctNum += 1
        else:
            xy = multiply_xy(x, 5)
            w = add(w, xy, 5)
            step += 1
            correctNum = 0
        if index == (n - 1):
            index = 0
        else:
            index += 1
        if correctNum == n:
            isFinished = True
    return step


def pla17():
     # 获取数据
    ret = getData("q15.txt")
    n = len(ret)
    random.shuffle(ret)
    # 进行计算

    # 修正的次数
    step = 0

    # 当前操作的索引
    index = 0
    # 连续正确的次数
    correctNum = 0

    isFinished = False
    test = 0
    w = [0, 0, 0, 0, 0]  # 默认w向量
    while not isFinished:
        x = ret[index]
        sum = multiply_wx(w, x, 5)
        if x[5] == sign(sum):
            correctNum += 1
        else:
            xy = multiply_xy(x, 5)
            w = add17(w, xy, 5)
            step += 1
            correctNum = 0
        if index == (n - 1):
            index = 0
        else:
            index += 1
        if correctNum == n:
            isFinished = True
    return step


if __name__ == "__main__":
    # ret = pla() # 45
    # print(ret)

    # 40
    # sum = 0
    # for i in range(2000):
    #     sum += pla16()
    # print(sum / 2000)

    # 40
    sum = 0
    for i in range(2000):
        sum += pla17()
    print(sum / 2000)
