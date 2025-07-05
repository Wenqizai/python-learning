""" 
扩展 RandomPicker 协议
"""
from typing import Protocol, runtime_checkable
from randompick import RandomPicker

@runtime_checkable
class RandomLoadPicker(RandomPicker, Protocol):
    def load(self, Iterable) -> None: ...

