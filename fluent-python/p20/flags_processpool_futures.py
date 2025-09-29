""" 
使用 futures.ProcessPoolExecutor 实现多进程下载的脚本

对于 IO 密集型的任务，多进程的性能比多线程的性能要差，耗费的资源却很大
"""
from concurrent import futures
from flags import save_flag, get_flag, main

def download_one(cc: str): 
    image = get_flag(cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

def download_many(cc_list: list[str]) -> int:
    cc_list = cc_list[:5] # 只下载前5个
    workers = min(3, len(cc_list))
    with futures.ProcessPoolExecutor(max_workers=workers) as executor: # 进程池
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f"Scheduled for {cc}: {future}")
            
        for count, future in enumerate(futures.as_completed(to_do), 1):
            res: str = future.result()
            print(f"{future} result: {res!r}")
        
    return count


if __name__ == '__main__':
    main(download_many)

