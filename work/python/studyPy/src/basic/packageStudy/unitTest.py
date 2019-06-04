#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import unittest


class Dict(dict):
    """docstring for Dict."""

    def __init__(self, **arg):
        super().__init__(arg)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# 编写单元测试 测试方法都是以test_开头的方法视为单元测试
class TestDict(unittest.TestCase):
    def setUp(self):
        print("开始启动测试")

    def tearDown(self):
        print("测试完成")

    def test_init(self):
        d = Dict(a=1, b="test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == "__main__":
    unittest.main()
