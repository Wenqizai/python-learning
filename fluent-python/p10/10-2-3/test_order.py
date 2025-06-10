""" 
order 模块的自动化测试 (最佳策略）
"""

import pytest
from order import Customer, LineItem, Order, fidelity_promo, bulk_item_promo, large_order_promo
from decimal import Decimal


promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order: Order) -> Decimal:
    """选择最佳策略"""
    return max(promo(order) for promo in promos)

def test_best_promo():
    """测试最佳策略"""
    joe = Customer("John Doe", 0)
    cart = [LineItem("banana", 4, Decimal("0.5")), LineItem("apple", 10, Decimal("1.5")), LineItem("watermelon", 5, Decimal("5"))]
    order = Order(joe, cart, best_promo)
    assert order.due() == Decimal("42.00")