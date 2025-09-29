""" 
ThreadPoolExecutor.map 的示例numbers

ThreadPoolExecutor.map 相当于返回一个 futures 结果，futures 获取结果时是阻塞获取的，所以最好在执行完结果后调用 futures.getResult() 来获取结果。
"""
from time import strftime, sleep
from concurrent import futures

def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)

def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t' * n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t' * n, n))
    return n * 10

def main():
    display('Script starting.')     
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display('results:', results)
    display('Waiting for individual results:')
    for i, result in enumerate(results):
        display(f'result {i}: {result}')

if __name__ == '__main__':
    main()