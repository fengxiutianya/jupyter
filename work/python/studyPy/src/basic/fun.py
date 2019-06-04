import math
n1 = 255
n2 = 1000
# 打印16进制
print(hex(n1), hex(n2))

# 定义一个abs函数


def my_abs(n):
    if n > 0:
        return n
    else:
        return -n


print(my_abs(12))

# 定义空操作


def my_none():
    pass


def my_none2():
    if 2 > 3:
        pass

# 改进abs


def my_improve_abs(x):
    if not isinstance(x, (float, int)):
        raise TypeError('bad operator error')
    if x >= 0:
        return x
    else:
        return -x


# 定义多个返回值


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 使用
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 也可以下面这样写
r = move(100, 100, 60, math.pi / 6)
print(r)
# 可以将r当做一个tuble，这是python的一种简写


# ax2 + bx + c = 0
def quadratic(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        return
    else:
        a1 = (-b + math.sqrt(d))/(2*a)
        a2 = (-b - math.sqrt(d))/(2*a)
        if a1 == a2:
            return a1
        else:
            return a1, a2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


# 位置参数：简单的写上参数名即可，必须传进去
# def test(a, b)

# 默认参数：参数名写上value值，可以不传进去
# def test(a, b=12)
#   默认参数调用时，可以不按照默认参数的位置来传递
# 类如test(a,b=1,c=22)这时，可以test(a,c=222)
# 表示只想改变c的默认值，不该变b的默认值，这时必须传递默认参数名
# def add_end(L=[]):
# 很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# 可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数：
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
# nums = [1, 2, 3]
# calc(*nums)
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：

# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, **extra)
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

# 命名关键字函数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# def person(name, age, *, city, job):
#     print(name, age, city, job)


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符 *，*后面的参数被视为命名关键字参数。
# 调用方式如下：
# person('Jack', 24, city='Beijing', job='Engineer')
# Jack 24 Beijing Engineer
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 小测试，改变可以接受一个个多个来接受乘机
def product(x, y=1, *args):
    sum = x * y
    for arg in args:
        sum = sum * arg
    return sum


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
