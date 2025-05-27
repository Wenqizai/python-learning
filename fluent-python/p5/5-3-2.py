""" 
具名元组：为具名元组注入方法
"""
import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])
Card.suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    suit_value = Card.suit_values[card.suit]
    return rank_value * len(Card.suit_values) + suit_value

# 注入方法
Card.overall_rank = spades_high

lowest_cards = Card('2', 'clubs')
highest_cards = Card('A', 'spades')

print(lowest_cards)
print(highest_cards)

print(Card.overall_rank(lowest_cards))
print(Card.overall_rank(highest_cards))

