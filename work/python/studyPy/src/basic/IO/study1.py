def readFile(arg):
    try:
        f = open(arg, 'r')
        # print(f.read())  # 一次读取所有的文件内容
        # print(f.read(4))  # 读取4个字节的内容
        print(f.readline())  # 读取一行内容

    except FileNotFoundError:
        raise FileNotFoundError(arg, "没有找到")
    finally:
        if f:
            f.close()


def withReadFile(arg):
    with open(arg, 'r') as f:
        for line in f.readlines():
            print(line.strip())


if __name__ == "__main__":
    readFile("/Users/zhangke/code/studyPy/src/basic/IO/input.txt")
    withReadFile("/Users/zhangke/code/studyPy/src/basic/IO/input.txt")
