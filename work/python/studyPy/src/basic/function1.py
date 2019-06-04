def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax += x
        return ax
    return sum


print(lazy_sum(1, 2, 3, 4)())
f1 = lazy_sum(1, 2, 3, 4)
f2 = lazy_sum(1, 2, 3, 4)
print(f1 == f2)


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())


def createCounter():
    f = [0]

    def counter():
        f[0] = f[0] + 1
        return f[0]
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
