class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_scores(self):
        print("%s %s" % (self.name, self.score))


if __name__ == "__main__":
    bart = Student("zhangke", 123)
    lisa = Student("lisa", 111)
    bart.print_scores()
    lisa.print_scores()
