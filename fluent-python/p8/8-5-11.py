""" 
类型提示: Callable

Callable[[ParamType1, ParamType2], ReturnType]
"""
from collections.abc import Callable
from typing import Any

def repl(input_fn: Callable[[Any], str] = input) -> None:
    pass

def update(
      probe: Callable[[], float],
      display: Callable[[float], None]
    ) -> None:
    temperature = probe()
    display(temperature)

def probe_ok() -> int:
    return 42

def display_wrong(temperature: int) -> None:
    print(hex(temperature))

update(probe_ok, display_wrong) # 类型检查失败

def display_ok(temperature: complex) -> None:
    print(temperature)

update(probe_ok, display_ok) # 类型检查通过


