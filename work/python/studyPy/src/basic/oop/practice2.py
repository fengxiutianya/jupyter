class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        # static 属性，需要直接使用student来定义
        Student.count += 1


if __name__ == "__main__":
    # 测试:
    if Student.count != 0:
        print('测试失败!')
    else:
        bart = Student('Bart')
        if Student.count != 1:
            print('测试失败!')
        else:
            lisa = Student('Bart')
            if Student.count != 2:
                print('测试失败!')
            else:
                print('Students:', Student.count)
                print('测试通过!')
