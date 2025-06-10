""" 
order 模块的自动化测试
"""
from decimal import Decimal
import pytest
from order import Order, Customer, LineItem, FidelityPromo, BulkItemPromo, LargeOrderPromo

@pytest.fixture
def joe() -> Customer:
    """积分为0的普通顾客"""
    return Customer('John Doe', 0)

@pytest.fixture
def ann() -> Customer:
    """积分超过1000的忠实顾客"""
    return Customer('Ann Smith', 1100)

@pytest.fixture
def cart() -> list[LineItem]:
    """包含3种商品的标准购物车"""
    return [LineItem('banana', 4, Decimal('.5')),
            LineItem('apple', 10, Decimal('1.5')),
            LineItem('watermelon', 5, Decimal('5'))]

def test_fidelity_promo(joe: Customer, ann: Customer, cart: list[LineItem]):
    """测试忠实顾客积分折扣"""
    # 顾客 Ann 积分超过1000，应享受5%折扣
    order_ann = Order(ann, cart, FidelityPromo())
    # 4*0.5 + 10*1.5 + 5*5 = 2 + 15 + 25 = 42
    # 42 * 0.05 = 2.1
    assert order_ann.due() == Decimal('42.00') - Decimal('2.10')

    # 顾客 Joe 积分不足，无折扣
    order_joe = Order(joe, cart, FidelityPromo())
    assert order_joe.due() == Decimal('42.00')

def test_bulk_item_promo(joe: Customer):
    """测试单个商品数量折扣"""
    # 香蕉数量为30，超过20，该商品享受10%折扣
    banana_cart = [LineItem('banana', 30, Decimal('.5')),
                   LineItem('apple', 10, Decimal('1.5'))]
    order = Order(joe, banana_cart, BulkItemPromo())
    # 总价: 30*0.5 + 10*1.5 = 15 + 15 = 30
    # 折扣: 15 * 0.1 = 1.5
    assert order.due() == Decimal('30.00') - Decimal('1.50')

def test_large_order_promo(joe: Customer):
    """测试不同种类商品数量折扣"""
    # 购物车中商品种类达到10种，整个订单享受7%折扣
    long_cart = tuple(LineItem(str(item_code), 1, Decimal(1)) for item_code in range(10))
    order = Order(joe, long_cart, LargeOrderPromo())
    # 总价: 10 * 1 = 10
    # 折扣: 10 * 0.07 = 0.7
    assert order.due() == Decimal('10.00') - Decimal('0.70')

    # 一个只有两种商品的购物车，不应享受折扣
    short_cart = [LineItem('banana', 1, Decimal(1)), LineItem('apple', 1, Decimal(1))]
    order_short = Order(joe, short_cart, LargeOrderPromo())
    assert order_short.due() == Decimal('2.00')