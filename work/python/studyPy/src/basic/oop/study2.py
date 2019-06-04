#!/usr/bin/env python3
# -*- coding=utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s %s" % (self.__name, self.__score))


if __name__ == "__main__":
    stu = Student("12", 22)
    stu.print_score()
    # 私有属性，访问不了
    stu.__name
