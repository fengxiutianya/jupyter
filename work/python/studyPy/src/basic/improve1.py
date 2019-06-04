# 函数高级特性1 切片 list[index1:index2] 取 从index1 到index2中间的元素包含index1，但不包含index2
# 前10个数，每两个取一个：
#  L[:10:2]
# [0, 2, 4, 6, 8]
# 所有数，每5个取一个：
#  L[::5]
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
# 甚至什么都不写，只写[:]就可以原样复制一个list：
#  L[:]
# [0, 1, 2, 3, ..., 99]
#


def trim(s):
    slen = len(s)
    if slen <= 0:
        return s
    index1 = 0
    index2 = -1
    for i in range(slen-1):
        if s[i] != ' ':
            index1 = i
            break
    i = slen-1
    while(i >= 0):
        if s[i] != ' ':
            index2 = i
            break
        i = i-1
    if index2 == (slen - 1):
        return s[index1:]
    else:
        return s[index1:index2+1]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败6!')
elif trim('    ') != '':
    print('测试失败7!')
else:
    print('测试成功!')
