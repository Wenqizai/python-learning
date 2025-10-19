"""     
使用 asyncio 实现多线程下载的脚本
"""
import asyncio
import re  
from flags_asyncio import save_flag, get_flag, main
import time 
from pathlib import Path
from typing import Callable, Counter
import httpx
import tqdm

DEFAUL_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000

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
    resp = await client.get(url, timeout=3.1, follow_redirects=True)
    resp.raise_for_status()
    return resp.content

async def download_one(client: httpx.AsyncClient, 
                       cc: str,
                       semaphore: asyncio.Semaphore,
                       verbose: bool) -> str:
    try:
        async with semaphore:
            image = await get_flag(client, cc)
    except httpx.HTTPStatusError as exc:
        res = exc.response
        if res.status_code == 404:
            msg = f'not found: {cc}'
        else:
            raise
    else: 
        await asyncio.to_thread(save_flag, image, f'{cc}.gif')
        msg = 'ok'
    if verbose and msg:
        print(cc, msg)
    return f'{cc}: {msg}'

def download_many(cc_list: list[str],
                  verbose: bool,
                  concur_req: int
                  ) -> Counter[str]:
    return asyncio.run(supervisor(cc_list, verbose, concur_req))

async def supervisor(cc_list: list[str],
                    verbose: bool,
                    concur_req: int
                     ) -> Counter[str]:
    counter: Counter[str] = Counter()
    semaphore = asyncio.Semaphore(concur_req)
    async with httpx.AsyncClient() as client:
        to_do = [download_one(client, cc, semaphore, verbose) for cc in sorted(cc_list)]
        to_do_iter = asyncio.as_completed(to_do)
        if not verbose:
            to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))

        error: httpx.HTTPError | None = None
        for coro in to_do_iter:
            try:
                status = await coro
            except httpx.HTTPError as exc:
                error_msg = f'HTTP error {resp.staus_code} - {resp.reason_phrase}'
                error_msg = error_msg.format(resp = exc.response)
                error = exc
            except httpx.RequestError as exc:
                error_msg = f'{exc} {type(exc)}'.strip()
                error = exc
            except KeyboardInterrupt:
                break

            if error:
                status = f'error: {error}'
                if verbose:
                    url = str(error.request.url)
                    cc = Path(url).stem.upper()
                    print(f'{cc} error: {error_msg}')
                counter[status] += 1
    return counter

def main(downloader: Callable[[list[str]], int], verbose: bool, concur_req: int) -> None:
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloader(POP20_CC, verbose, concur_req)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} downloaded in {elapsed:.2f}s')

if __name__ == '__main__':
    main(download_many, DEFAUL_CONCUR_REQ, MAX_CONCUR_REQ)