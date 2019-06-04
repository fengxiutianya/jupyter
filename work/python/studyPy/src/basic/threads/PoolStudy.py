import os
import random
import time
from multiprocessing.pool import Pool


def long_time_task(name):
    print("Run task %s (%s)..." % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end =time.time()
    print("Task %s runs %0.2f seconds," % (name,end-start))

if __name__=='__main__':
    print("parent process %s." % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print("waitting for all subprocesses done,,,")
    p.close()
    ## join 之前必须先调用close ，不能再往里面添加线程
    p.join()
    print("all subprocess done")