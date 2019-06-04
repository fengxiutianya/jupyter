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


def getErrorRate(weight, trainset):
    n = len(trainset)
    errorRate = 0
    for x in trainset:
        if sign(multiply_wx(weight, x, 5)) != x[5]:
            errorRate += 1
    return errorRate / n


def pocketpla(trainset, iter):
    # 获取数据
    n = len(trainset)

    # 当前操作的索引
    index = 0

    isFinished = 0

    # 默认最好的向量
    pocketWeight = [0, 0, 0, 0, 0]
    # 随机w向量
    w = [0, 0, 0, 0, 0]
    while isFinished < iter:
        x = trainset[index]
        sum = multiply_wx(w, x, 5)

        if x[5] != sign(sum):
            xy = multiply_xy(x, 5)
            w = add(w, xy, 5)
            if(getErrorRate(w, trainset) < getErrorRate(pocketWeight, trainset)):
                for i in range(len(pocketWeight)):
                    pocketWeight[i] = w[i]
            isFinished += 1
        if index == (n - 1):
            index = 0
        else:
            index += 1
    return pocketWeight


def pocketpla19(trainset, iter):
    # 获取数据
    n = len(trainset)

    # 当前操作的索引
    index = 0

    isFinished = 0

    # 默认最好的向量
    pocketWeight = [0, 0, 0, 0, 0]
    # 随机w向量
    w = [0, 0, 0, 0, 0]
    while isFinished < iter:
        x = trainset[index]
        sum = multiply_wx(w, x, 5)

        if x[5] != sign(sum):
            xy = multiply_xy(x, 5)
            w = add(w, xy, 5)
            # if(getErrorRate(w, trainset) < getErrorRate(pocketWeight, trainset)):
            #     for i in range(len(pocketWeight)):
            #         pocketWeight[i] = w[i]
            isFinished += 1
        if index == (n - 1):
            index = 0
        else:
            index += 1
    return pocketWeight


if __name__ == "__main__":
    # train_set = getData("q18_train.txt")
    # test_set = getData("q18_test.txt")
    # totalError = 0
    # for i in range(2000):
    #     random.shuffle(train_set)
    #     pocketWeights = pocketpla(train_set, 50)
    #     totalError += getErrorRate(pocketWeights, test_set)
    # print(totalError / 2000)
    # 0.1307279999999999
    # 0.1317589999999997
    # train_set = getData("q18_train.txt")
    # test_set = getData("q18_test.txt")
    # totalError = 0
    # for i in range(2000):
    #     random.shuffle(train_set)
    #     pocketWeights = pocketpla19(train_set, 50)
    #     totalError += getErrorRate(pocketWeights, test_set)
    # print(totalError / 2000)
    # 0.29800000000000165

    train_set = getData("q18_train.txt")
    test_set = getData("q18_test.txt")
    totalError = 0
    for i in range(2000):
        random.shuffle(train_set)
        pocketWeights = pocketpla(train_set, 100)
        totalError += getErrorRate(pocketWeights, test_set)
    print(totalError / 2000)
