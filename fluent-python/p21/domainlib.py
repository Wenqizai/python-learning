""" 
探测域名的函数
"""
import asyncio
import socket
from typing import AsyncIterator, Iterable, NamedTuple, Optional


class Result(NamedTuple):
    domain: str
    found: bool

OptionalLoop = Optional[asyncio.AbstractEventLoop]

async def probe(domain: str, loop: OptionalLoop = None) -> Result:
    if loop is None:
        loop = asyncio.get_running_loop()
    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return Result(domain, False)
    return Result(domain, True)


async def multi_probe(domains: Iterable[str]) -> AsyncIterator[Result]:
    loop = asyncio.get_running_loop()
    coros = [probe(domain, loop) for domain in domains]
    for coro in asyncio.as_completed(coros):
        result = await coro
        yield result