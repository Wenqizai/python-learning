""" 
找出一个模块中的全部策略
"""
from decimal import Decimal
from order import Order, Customer, LineItem
from order import (
    fidelity_promo,
    bulk_item_promo,
    large_order_promo,
)

# globals() 返回一个字典, 包含当前全局作用域中的所有变量    
promos = [
    promo for name, promo in globals().items() if name.endswith("_promo") and name != "best_promo"  
]

def best_promo(order: Order) -> Decimal:
    """选择最佳策略"""
    return max(promo(order) for promo in promos)

def test_best_promo():
    """测试最佳策略"""
    joe = Customer("John Doe", 0)
    cart = [LineItem("banana", 4, Decimal("0.5")), LineItem("apple", 10, Decimal("1.5")), LineItem("watermelon", 5, Decimal("5"))]
    order = Order(joe, cart, best_promo)
    assert order.due() == Decimal("42.00")
