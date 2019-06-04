d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print(d["Bob"])
print(d.get("22"))  # 获取不到，如果用d[""]则会产生错误如果没有对应的key
s = set([1, 2, 3])
print(s)
s.add(1)
print(s.remove(1))
print(s)
t1 = (1, 2, 3)
t2 = (1, [2, 3])
d = set([t1])
# 虽然t2不可变，但是里面的内容会发生变化，所以hash值会发生变化
d2 = set([t2])
