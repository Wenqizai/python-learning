""" 
存储多个命令, 并按顺序执行
"""
from typing import List
from command import Command

class MacroCommand:
    """ 存储多个命令, 并按顺序执行 """
    def __init__(self, commands: List[Command]) -> None:
        self.commands = list(commands)

    def __call__(self) -> None:
        for command in self.commands:
            command()
    