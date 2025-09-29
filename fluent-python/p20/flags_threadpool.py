""" 
使用 futures.ThreadPoolExecutor 实现多线程下载的脚本
"""
from concurrent import futures
from flags import save_flag, get_flag, main

def download_one(cc: str): 
    image = get_flag(cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

def download_many(cc_list: list[str]) -> int:
    workers = min(10, len(cc_list))
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
        
    return len(list(res))


if __name__ == '__main__':
    main(download_many)

