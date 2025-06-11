""" 
order 模块: 策略模式(使用函数实现)
"""
from collections import namedtuple
from decimal import Decimal
from typing import Callable, Optional, Sequence, NamedTuple
from dataclasses import dataclass

class Customer(NamedTuple):
    name: str
    fidelity: int

class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity

@dataclass(frozen=True)
class Order:
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = None # 可执行的函数

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))
    
    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self) # 执行函数, 返回折扣
        return self.total() - discount

    def __repr__(self) -> str:
        return f"<Order total: {self.total():.2f} due: {self.due():.2f}>"

def fidelity_promo(order: Order) -> Decimal:
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * Decimal('0.05') if order.customer.fidelity >= 1000 else Decimal(0)

def bulk_item_promo(order: Order) -> Decimal:
    """单个商品为20个或以上时提供10%折扣"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount

def large_order_promo(order: Order) -> Decimal:
    """订单中不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)
    