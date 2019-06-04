# 解决汉若塔问题


# def move(x, y):
#     print(x, '-->', y)


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)


move(3, 'a', 'b', 'c')
