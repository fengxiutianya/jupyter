#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import types
import math


class MyDog(object):

    def __len__(self):
        return 111

    def read(self):
        print("read")


if __name__ == "__main__":
    print(type(123))
    print(type(None))
    print(type(123) == type(222))
    print(type(123) == int)
    print(type("123") == str)
    print(type("abe") == type(123))

    # 函数判定
    print(type(abs) == types.BuiltinFunctionType)
    print(type(lambda x: x) == types.LambdaType)

    # 打印对象的所有属性和方法
    print(dir(str))
    print("abc".__len__())
    dog = MyDog()
    print(len(dog))
    if hasattr(dog, 'read'):
        dog.read()
