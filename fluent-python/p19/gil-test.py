""" 
GIL 限制示例：CPU 密集型任务

cpu 密集型任务的执行效率：单线程 > 多进程 > 多线程 
""" 

import threading
import time
import multiprocessing

# CPU 密集型任务：计算斐波那契数列
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 线程版本 - 受 GIL 限制
def thread_version():
    print("=== 线程版本 (受 GIL 限制) ===")
    start_time = time.time()
    
    # 创建多个线程
    threads = []
    for i in range(4):  # 4个线程
        t = threading.Thread(target=fibonacci, args=(35,))
        t.start()
        threads.append(t)
    
    # 等待所有线程完成
    for t in threads:
        t.join()
    
    end_time = time.time()
    print(f"线程版本耗时: {end_time - start_time:.2f} 秒")
    print("注意：由于 GIL，这 4 个线程实际上是在串行执行！")

# 进程版本 - 真正并行
def process_version():
    print("\n=== 进程版本 (真正并行) ===")
    start_time = time.time()
    
    # 创建多个进程
    processes = []
    for i in range(4):  # 4个进程
        p = multiprocessing.Process(target=fibonacci, args=(35,))
        p.start()
        processes.append(p)
    
    # 等待所有进程完成
    for p in processes:
        p.join()
    
    end_time = time.time()
    print(f"进程版本耗时: {end_time - start_time:.2f} 秒")
    print("注意：这 4 个进程可以真正并行执行！")

if __name__ == "__main__":
    # 单线程基准
    print("=== 单线程基准 ===")
    start_time = time.time()
    fibonacci(35)
    end_time = time.time()
    print(f"单线程耗时: {end_time - start_time:.2f} 秒")
    
    # 线程版本
    thread_version()
    
    # 进程版本
    process_version()
    
    print(f"\nCPU 核心数: {multiprocessing.cpu_count()}")
    print("结论：线程版本不会比单线程快，但进程版本会显著更快！")