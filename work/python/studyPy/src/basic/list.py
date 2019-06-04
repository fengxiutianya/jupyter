classMates = ["zhanke", "test", "ddd"]
print(classMates)
print(classMates[0])

# 测量长度
print(len(classMates))
# 打印倒数第一个，第二个可以以此类推
print(classMates[-1])
print(classMates[-2])
# list是可变数组
classMates.append("test")
classMates.insert(len(classMates), "end")
# 使用函数删除末尾元素，就可以将此当成队列来使用
print(classMates.pop())
# 删除指定位置元素
print(classMates.pop(0))

# 替换元素
print(classMates[0])
classMates[0] = "333"
print(classMates[0])
# 不变数组
t = (1,)  # 如果只有一个元素，最好后面加上分号
print(t)
# 注意，这里是list中还包含一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
# 长度是4
print(len(s))

l = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(l[0][0])
# 打印Python:
print(l[1][1])
# 打印Lisa:
print(l[2][2])
