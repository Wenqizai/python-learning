""" 
素数检测多进程版本导入，类型和函数

CPU 密集型任务，多进程的性能优于多线程
"""
from os import cpu_count
import sys
from typing import NamedTuple
from time import perf_counter
from primes import is_prime, NUMBERS
from multiprocessing import Process, SimpleQueue


class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float

JobQueue = SimpleQueue
ResultQueue = SimpleQueue

def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    prime = is_prime(n)
    return PrimeResult(n, prime, perf_counter() - t0)

def worker(jobs: JobQueue, results: ResultQueue) -> None:
    while n := jobs.get():
        results.put(check(n))
    results.put(PrimeResult(0, False, 0.0))

def start_jobs(
    procs: int, jobs: JobQueue, results: ResultQueue
) -> None:
    for n in NUMBERS:
        jobs.put(n)
    for _ in range(procs):
        proc = Process(target=worker, args=(jobs, results))
        proc.start()
        jobs.put(0) # 毒丸，暂停
        
def main() -> None:
    if len(sys.argv) < 2:
        procs = cpu_count()
    else: 
        procs = int(sys.argv[1])

    print(f'Checking {len(NUMBERS)} numbers with {procs} processes:')
    t0 = perf_counter()

    jobs: JobQueue = SimpleQueue()
    results: ResultQueue = SimpleQueue()
    start_jobs(procs, jobs, results)

    checked = report(procs, results)
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')

def report(procs: int, results: ResultQueue) -> int:
    """ 打印结果 """
    checked = 0
    procs_done = 0
    while procs_done < procs:
        n, prime, elapsed = results.get()
        if n == 0:
            procs_done += 1
        else:
            checked += 1
            label = 'P' if prime else ' '
            print(f'{n:16}  {label}  {elapsed:9.6f}s')
    return checked
    
if __name__ == '__main__':
    main()