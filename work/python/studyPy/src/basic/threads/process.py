import os


def basic():
    print("Process (%s) start...." % os.getpid())
    pid = os.fork()
    if pid == 0:
        print("I`m child Process (%s) and my parent is %s" %
              (os.getpid(), os.getppid()))
    else:
        print("I (%s) just created a child Process (%s)." % (os.getpid(), pid))


if __name__ == "__main__":
    basic()
