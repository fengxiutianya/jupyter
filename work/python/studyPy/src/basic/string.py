#!/usr/bin/env python3
# -*- coding:utf-8 -*-
print("包含中文的str")
print(ord('a'))
print(ord('b'))
print(chr(25991))
print('\u4e2d\u6587')
# 英文使用ascii编码是一样的结果，其他的则不行
print('abc'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 计算字符个数
print(len("zhongguo "))
print(len("中文"))
print("%d" % (3))

print("%d %d" % (3, 3))
r = 85/72 - 1
print("%.1f" % (r*100))
