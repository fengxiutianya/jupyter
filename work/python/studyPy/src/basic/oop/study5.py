from types import MethodType


class Student(object):
    # 限制的是实例对象的属性，不限制class的属性添加
    __slots__ = ('name', 'age', 'score', 'set_age')  # 用tuple定义允许绑定的对象属性
    pass


s = Student()
s.name = "zhagke"
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例添加一个方法
s.set_age(123)
print(s.age)

s1 = Student()

# s1 中没有s实例中添加的一些新属性


# 直接在class上绑定对象
def set_score(self, score):
    self.score = score


Student.set_score = set_score

s1.set_score(12)
print(s1.score)
