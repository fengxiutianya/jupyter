import os
import types


def basic():
    print(os.name)
    print(os.uname())
    t = os.environ
    for key in t:
        print(key, ":", t[key])
    # print(os.environ)
    # for key, value in os.environ:
    #     print(key, ":", value)


def fileDirs():
    # 查看当前目录的绝对路径
    currentDirs = os.path.abspath(".")
    print(currentDirs)
    # 穿件目录
    jonindirs = os.path.join(currentDirs, "test")
    os.mkdir(jonindirs)
    # 删除目录
    os.rmdir(jonindirs)


def listDirs():
    # 列出所有的文件夹
    t = [x for x in os.listdir(".") if os.path.isdir(x)]
    print(t)
    # 查找basic目录下所有的py
    basic = os.path.join(os.path.abspath("."), "basic")
    print(basic)
    t = [x for x in os.listdir(basic) if os.path.isfile(
        os.path.join(basic, x)) and os.path.splitext(x)[1]]
    print(t)


if __name__ == "__main__":
    # basic()
    # fileDirs()
    listDirs()
