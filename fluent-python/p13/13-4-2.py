""" 
洗牌
"""
import collections
from random import shuffle

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck: 
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self): 
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self): 
        return len(self._cards)
    
    def __getitem__(self, position): 
        return self._cards[position]

    def set_card(self, position, card): 
        self._cards[position] = card

deck = FrenchDeck()
FrenchDeck.__setitem__ = FrenchDeck.set_card # 重写 __setitem__ 将 set_card 绑定到 __setitem__ 上
shuffle(deck)
print(deck[:5])