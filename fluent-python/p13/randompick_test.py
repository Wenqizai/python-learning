""" 
test random pick
"""

from typing import Any, Iterable, TYPE_CHECKING
import random
from randompick import RandomPicker


class SimplePicker:
    def __init__(self, items: Iterable) -> None:
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self) -> Any:
        return self._items.pop()


def test_isinstance() -> None:
    popper: RandomPicker = SimplePicker([1])
    assert isinstance(popper, RandomPicker)


def test_item_type() -> None:
    items = [1, 2]
    popper = SimplePicker(items)
    item = popper.pick()
    assert item in items
    if TYPE_CHECKING:
        reveal_type(item) # “item”的类型为“Any”Pylance
    assert isinstance(item, int)