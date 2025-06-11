""" 
装饰器改进策略模式
"""
from collections.abc import Callable
from typing import List
from decimal import Decimal
from order import Order

Promotion = Callable[[Order], Decimal]

promos: List[Promotion] = []
def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo

@promotion
def fidelity_promo(order: Order) -> Decimal:
    """ 为积分1000以上的顾客提供5%的折扣 """
    return Decimal(0) if order.customer.fidelity < 1000 else order.total() * Decimal(0.05)

@promotion
def bulk_item_promo(order: Order) -> Decimal:
    """ 单个商品为20个或以上时提供10%的折扣 """
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal(0.1)
    return discount

@promotion
def large_order_promo(order: Order) -> Decimal:
    """ 订单中的不同商品达到10个或以上时提供7%的折扣 """
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal(0.07)
    return Decimal(0)

# best_promo 函数使用 promos 列表中的所有策略
def best_promo(order: Order) -> Decimal:
    """ 选择最佳策略 """
    return max(promo(order) for promo in promos)


