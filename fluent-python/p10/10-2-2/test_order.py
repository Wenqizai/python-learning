"""
order 模块的自动化测试 (函数式策略版本)
"""
from decimal import Decimal
import pytest
from order import (
    Customer,
    LineItem,
    Order,
    fidelity_promo,
    bulk_item_promo,
    large_order_promo,
)

@pytest.fixture
def joe() -> Customer:
    """积分为0的普通顾客"""
    return Customer("John Doe", 0)

@pytest.fixture
def ann() -> Customer:
    """积分超过1000的忠实顾客"""
    return Customer("Ann Smith", 1100)

@pytest.fixture
def cart() -> list[LineItem]:
    """包含3种商品的标准购物车"""
    return [
        LineItem("banana", 4, Decimal("0.5")),
        LineItem("apple", 10, Decimal("1.5")),
        LineItem("watermelon", 5, Decimal("5")),
    ]

def test_fidelity_promo(ann: Customer, cart: list[LineItem]):
    """测试忠实顾客积分折扣函数 (有折扣)"""
    order = Order(ann, cart, fidelity_promo)
    # 总价: 4*0.5 + 10*1.5 + 5*5 = 42
    # 折扣: 42 * 0.05 = 2.1
    assert order.due() == Decimal("39.90")

def test_fidelity_promo_no_discount(joe: Customer, cart: list[LineItem]):
    """测试忠实顾客积分折扣函数 (无折扣)"""
    order = Order(joe, cart, fidelity_promo)
    assert order.due() == Decimal("42.00")

def test_bulk_item_promo(joe: Customer):
    """测试单个商品数量折扣函数"""
    banana_cart = [
        LineItem("banana", 30, Decimal("0.5")),
        LineItem("apple", 10, Decimal("1.5")),
    ]
    order = Order(joe, banana_cart, bulk_item_promo)
    # 总价: 30*0.5 + 10*1.5 = 30
    # 折扣: 15 * 0.1 = 1.5
    assert order.due() == Decimal("28.50")

def test_large_order_promo(joe: Customer):
    """测试不同种类商品数量折扣函数 (有折扣)"""
    long_cart = tuple(
        LineItem(str(item_code), 1, Decimal("1")) for item_code in range(10)
    )
    order = Order(joe, long_cart, large_order_promo)
    # 总价: 10 * 1 = 10
    # 折扣: 10 * 0.07 = 0.7
    assert order.due() == Decimal("9.30")

def test_large_order_promo_no_discount(joe: Customer):
    """测试不同种类商品数量折扣函数 (无折扣)"""
    short_cart = [LineItem("banana", 1, Decimal(1)), LineItem("apple", 1, Decimal(1))]
    order = Order(joe, short_cart, large_order_promo)
    assert order.due() == Decimal("2.00")

def test_no_promo(joe: Customer, cart: list[LineItem]):
    """测试没有促销策略的情况"""
    order = Order(joe, cart, None)
    assert order.due() == Decimal("42.00")


