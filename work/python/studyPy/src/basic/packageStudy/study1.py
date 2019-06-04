from functools import reduce
import logging


def basic():
    try:
        print('try.....')
        t = 10 / int('a')
        print("result", r)
    except ZeroDivisionError as e:
        print("excepr:", e)
    except ValueError as e:
        print("except:", e)
        logging.exception(e)
    else:
        print("no error!")
    finally:
        print("finally....")
    print('END')


def str2num(s):
    return int(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
if __name__ == "__main__":
    # basic()
    main()
