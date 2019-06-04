import  asyncio
import threading


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    ## 异步调用 asyncio.sleep(1)
    r  = yield  from asyncio.sleep(1)
    print('Hello world! (%s)' % threading.currentThread())
## 定义一个任务在里面执行
def basic():
    ### 获取eventLoop
    loop = asyncio.get_event_loop()
    ### 执行coroutine
    loop.run_until_complete(hello())
    loop.close()

## 定义俩个任务在里面执行
def twoTask():
    loop = asyncio.get_event_loop()
    tasks = [hello(),hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
@asyncio.coroutine
def wget(host):
    print("wget %s ...." % host)
    connect = asyncio.open_connection(host,80)
    reader,writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode("utf-8"))
    yield  from writer.drain()
    while True:
        line = yield from reader.readline()
        if line==b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        writer.close()
async def wgetImprove(host):
    print("wget %s ...." % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await  connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode("utf-8"))
    await  writer.drain()
    while True:
        line = await  reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        writer.close()
def wgetLoop():
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
def wgetimproveLoop():
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
if __name__ == '__main__':
    # basic()
    # twoTask()
    # wgetLoop()
    wgetimproveLoop()