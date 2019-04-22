import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()  # 把一个字符串分割成字符串数组。

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(deck)
print(len(deck))

print('*' * 100)

for i in deck:
    print(i)

print('*' * 100)

for j in reversed(deck):
    print(j)


suit_values = dict(spades=3, diamonds=1, clubs=0, hearts=2)


def spades_high(card):
    rank_values = FrenchDeck.ranks.index(card.rank)
    print(rank_values)
    print('*' * 100)
    print(rank_values * len(suit_values) + suit_values[card.suit])
    return rank_values * len(suit_values) + suit_values[card.suit]


print('*' * 100)
for card in sorted(deck, key=spades_high):
    print(card)