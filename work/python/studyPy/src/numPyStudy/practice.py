#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    author      : zhangke
    createTime  : 2019-04-15 19:37
    filename    : practice.py
    info        : 学习numPy Ndarray对象的使用
'''
import numpy as np

def createNdarry():
    a = np.array([1,2,3])
    print("一维数组:",a)

    b = np.array([[1,2],[3,4]])
    print("二维数组：",b)

    ## 设置最小维度
    c = np.array([1,2,3,4],ndmin=2)
    print("二维数组：",c)

    ## 设置数据类型
    d = np.array([1,2,3,4],dtype=complex)
    print(d)

def createNdarryType():
    dt = np.dtype(np.int32)
    print(dt)

    # 创建结构化的数据
    dt1 = np.dtype([("age",np.int8)])
    print(dt1)

    ## 将数据类型应用于 ndarray 对象
    a = np.array([(10,),(20,),(30,)],dtype=dt1)
    print(a)
    # 类型字段可以用于存储实际的age列
    print(a["age"])
    ## 定义结构化数据
    student = np.dtype([("name","S20"),('age',"i1"),("marks","f4")])
    a = np.array([("abc",21,50),("xyz",18,75)],dtype=student)
    print(a["age"])

def studyNdAarrayPro():
    ## 秩
    a = np.arange(24)
    print(a.ndim) # 数组只有一个维度
    print(a)
    ## 调整其大小
    b = a.reshape(2,4,3) # b现在拥有三个维度
    print(b.ndim)
    print(b)

    ## shape
    a1 =np.array([[1,2,3],[4,5,6]])
    print(a1.shape)
    print(a1)
    ## 调整其数组
    a1.shape = (3,2)
    print(a1)

def createndArray():
    x = np.empty([3,2],dtype=int)
    print(x)
    # 默认为浮点数
    x1 = np.zeros(5)
    print(x1)

    # 设置类型为整数
    y = np.zeros((5 ,) ,dtype=np.int)
    print(y)
    print(y.ndim)

    # 自定义类型
    z = np.zeros((2 ,2) ,dtype=[('x' ,'i4') ,('y' ,'i4')])
    print(z)
    print(z.ndim)
    print(z.shape)
if __name__ == '__main__':
    # createNdarry()
    # createNdarryType()
    # studyNdAarrayPro()
    createndArray()
    exit(0)