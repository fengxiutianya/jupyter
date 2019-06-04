from hello import Hello

h = Hello()
h.hello()
print(type(Hello))
print(type(h))


def fn(self, name='world'):
    print("hello %s" % name)


Hello1 = type("Hello", (object,), dict(hello=fn))  # 创建Hello class
h = Hello1()
h.hello()
