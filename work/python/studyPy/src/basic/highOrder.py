import math
from functools import reduce
# 函数名类似于指针，可以复制给变量


def learn1():
    print(abs)
    print(abs(-1))
    f = abs
    print(f(-1))


# learn1()

# 传入参数，函数可以当做变量名来传递
def add(a, b, f):
    return f(b) + f(a)


# 打印结果是2，可以说明abs起到作用
# 把函数作为参数传入，这样的函数称为高阶函数
# ，函数式编程就是指这种高度抽象的编程范式。
# print(add(-1, 1, abs))


# map 演示
def f1(x):
    return x*x


# r = map(f1, [1, 2, 3, 4, 5, 6])
# print(list(r))
# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def add(x, y):
    return x+y


l = reduce(add, [1, 2, 3, 4])
print(l)


def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, "13579")))
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def strToInt(s):
    return reduce(lambda x, y: x*10+y, map(char2num, s))


print(strToInt('12334'))
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字


def normalize(s):
    return s.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x, y: x*y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    def fn(x, y):
        return x*10+y
    n = s.index('.')
    s1 = list(map(int, [x for x in s[:n]]))
    s2 = list(map(int, [x for x in s[n+1:]]))
    return reduce(fn, s1) + reduce(fn, s2)/10**len(s2)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


def is_odd(n):
    return n % 2 == 0


l = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(l)


def not_empty(s):
    return s and s.strip()


l = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(l)


def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break


def is_palindrome(n):
    strn = str(n)
    l = len(strn)
    for i in range(len(strn)//2):
        if strn[i] != strn[len(strn)-1-i]:
            return False
    return True


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


def by_name(t):
    return t[0]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score)
print(L2)
