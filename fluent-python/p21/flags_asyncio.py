""" 
依序下载旗帜的脚本: 协程
"""
import asyncio
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

async def get_flag(client: httpx.AsyncClient, cc: str) -> bytes:
    # http://mp.ituring.com.cn/files/flags/ad/ad.gif
    url = f"{BASE_URL}/flags/{cc}/{cc}.gif".lower()
    print(url)
    resp = await client.get(url, timeout=6.1, follow_redirects=True)
    return resp.read()

async def download_one(client: httpx.AsyncClient, cc: str) -> str:
    image = await get_flag(client, cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

def download_many(cc_list: list[str]) -> None:
    return asyncio.run(supervisor(cc_list))

async def supervisor(cc_list: list[str]) -> int:
    async with httpx.AsyncClient() as client:
        to_do = [download_one(client, cc) for cc in sorted(cc_list)]
        res = await asyncio.gather(*to_do)
    return len(res)

def main(downloader: Callable[[list[str]], int]) -> None:
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} downloaded in {elapsed:.2f}s')

if __name__ == '__main__':
    main(download_many)