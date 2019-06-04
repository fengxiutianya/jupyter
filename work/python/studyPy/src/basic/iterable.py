import os


def findMinAndMax(L):
    x1 = None
    x2 = None
    for v in L:
        if x1:
            if x1 < v:
                x1 = v
        else:
            x1 = v
        if x2:
            if x2 > v:
                x2 = v
        else:
            x2 = v
    return (x2, x1)


   # 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


# 生成器
l = [x * x for x in range(1, 11)]
print(l)

l = [x*x for x in range(1, 100) if x % 2 == 0]
print(l)

# 打印当前文件夹
dirs = [d for d in os.listdir('.')]
print(dirs)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for key, value in d.items():
    print(key, value)
L = ['Hello', 'World', 'IBM', 'Apple']
sl = [s.lower() for s in L]
print(sl)
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
