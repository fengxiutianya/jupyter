#!/usr/bin/env python3
# -*- coding=utf-8 -*-


class Student(object):
    # def get_score(self):
    #     return self._score

    # def set_score(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('score must be an integer!')
    #     if value < 0 or value > 100:
    #         raise ValueError('score must between 0 ~ 100!')
    #     self._score = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # 下面的birth是可读写属性，age是只读属性
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


# if __name__ == "__main__":
#     s = Student()
#     # s.set_score(12)
#     # print(s.get_score())
#     s.score = 12
#     print(s.score)
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, w):
        self._height = w

    @property
    def resolution(self):
        return self.width * self.height


if __name__ == "__main__":
   # 测试:
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')
