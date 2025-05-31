""" 
@dataclass: 初始化不作为字段的变量
"""
from dataclasses import dataclass, InitVar


class DatabaseType:  # Placeholder for actual DatabaseType
    def get_default_j(self):
        # Replace with actual logic to get default j
        return 42  # Example default value


@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.get_default_j()

c = C(10, database=DatabaseType())