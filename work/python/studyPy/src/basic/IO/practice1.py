import os


def currentDitList(currentDir):
    t = []
    for i in os.listdir(currentDir):
        if os.path.isdir(os.path.join(currentDir, i)):
            tem = currentDitList(os.path.join(currentDir, i))
            for i in tem:
                t.append(i)
        else:
            t.append(os.path.join(currentDir, i))
    return t


if __name__ == "__main__":
    current = os.path.abspath(".")
    t = currentDitList(current)
    print(t)
