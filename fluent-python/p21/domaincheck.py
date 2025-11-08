""" 
使用 domainlib 模块探测域名
"""
import asyncio
import sys 
from keyword import kwlist

from domainlib import multi_probe

MAX_KEYWORD_LEN = 4

async def main(tld: str) -> None:
    tld = tld.strip('.')
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)
    domains = (f'{name}.{tld}'.lower() for name in names)
    print('FOUND\t\tNOT FOUND')
    print('====\========')
    async for domain, found in multi_probe(domains):
        indent = '' if found else '\t\t'
        print(f'{indent}{domain}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        asyncio.run(main(sys.argv[1]))
    else:
        print('Please provide a TLD.', f'Example: {sys.argv[0]} COM.BR')
