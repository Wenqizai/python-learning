""" 
依序下载旗帜的脚本
"""
import time 
from pathlib import Path
from typing import Callable
import httpx

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://mp.ituring.com.cn/files'
DEST_DIR = Path('./downloaded')

def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img)

def get_flag(cc: str) -> bytes:
    # http://mp.ituring.com.cn/files/flags/ad/ad.gif
    url = f"{BASE_URL}/flags/{cc}/{cc}.gif".lower()
    print(url)
    resp = httpx.get(url, timeout=6.1, follow_redirects=True)
    return resp.content

def download_many(cc_list: list[str]) -> None:
    for cc in sorted(cc_list):
        image = get_flag(cc)
        save_flag(image, f'{cc}.gif')
        print(cc, end=' ', flush=True)
    return len(cc_list)

def main(downloader: Callable[[list[str]], int]) -> None:
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} downloaded in {elapsed:.2f}s')

if __name__ == '__main__':
    main(download_many)