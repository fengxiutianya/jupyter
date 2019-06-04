age = 20
if age < 18:
    print("未成年")
elif age < 60:
    print("中年")
else:
    print("old")
x = []
x = True
if x:
    print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# 暂时使用简单的输入
birth = input("birth:")
birth = int(birth)
if birth < 1992:
    print("1992")
else:
    print("2000")

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
high = 1.75
weight = 90.5
bmi = weight / (high*high)
if bmi < 18.5:
    print("较轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("较重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")

names = ['Michael', 'Bob', 'Tracy']

for name in names:
    print(name)
# 生成一个list
rang100 = list(range(100))
print(rang100)

sum = 0
for x in range(100):
    sum += x
print(sum)
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print("hello ", x)
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
