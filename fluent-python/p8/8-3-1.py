""" 
渐进式类型实践
"""

from pytest import mark


def show_count(count, word):
    """
    显示单词的计数
    """
    if count == 1:
        print(f"1 {word}")

    count_str = str(count) if count else "no"
    return f"{count_str} {word}s"


show_count(99, "bird")
show_count(1, "bird")
show_count(0, "bird")


@mark.parametrize("qty, expected", [
    (1, "1 part"),
    (2, "2 parts"),
])
def test_show_count(qty, expected):
    """
    测试 show_count 函数
    """
    result = show_count(qty, "bird")
    assert result == expected

def test_show_count_zero():
    got = show_count(0, "bird")
    assert got == "no birds"
