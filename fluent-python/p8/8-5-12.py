""" 
类型提示: NoReturn 类型

这种类型适合, 没有返回值类型的函数, 这类函数通常会抛出异常
"""
from typing import NoReturn


def exit(_status: object = ...) -> NoReturn:
    ...

def main() -> None:
    exit()

