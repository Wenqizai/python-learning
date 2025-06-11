""" 
order 模块: 策略模式(经典实现)
"""
from collections import namedtuple
from abc import ABC, abstractmethod
from typing import NamedTuple, Optional, Sequence
from decimal import Decimal
class Customer(NamedTuple):
    name: str
    fidelity: int

class LineItem(NamedTuple):
    """ 订单中的商品 """
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity

class Order(NamedTuple):
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional['Promotion'] = None

    def total(self) -> Decimal:
        """ 订单总价 """
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))
    
    def due(self) -> Decimal:
        """ 应付金额 """
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self) -> str:
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'

class Promotion(ABC):
    """ 策略: 抽象基类 """
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        """ 返回折扣金额(正值) """

class FidelityPromo(Promotion):
    """ 为积分1000以上的顾客提供5%的折扣 """
    def discount(self, order: Order) -> Decimal:
        return Decimal(0) if order.customer.fidelity < 1000 else order.total() * Decimal('0.05')

class BulkItemPromo(Promotion):
    """ 为单个商品20个以上的顾客提供10%的折扣 """
    def discount(self, order: Order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal('0.1')
        return discount

class LargeOrderPromo(Promotion):
    """ 订单中不同商品达到10个或以上时提供7%的折扣 """
    def discount(self, order: Order) -> Decimal:
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * Decimal('0.07')
        return Decimal(0)
        
        