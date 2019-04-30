# 示例1.1 一摞有序的纸牌
import collections

# collections.namedtuple构建了一个简单的类（少量属性没有方法的对象）来表示一张纸牌
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


# 实例化一套扑克牌
deck = FrenchDeck()
print(deck)

# 使用len查看一套牌有多少张
print(len(deck))

print('*' * 100)

from random import choice
# 不用重新写一个方法来实现随机抽取一张扑克，python内置的随机选择函数，可以随机抽取一张扑克
a1 = choice(deck)
print(a1)

print('*' * 100)
# 实现 __getitem__   方法使得这套扑克牌变成可迭代
for i in deck:
    print(i)

print('*' * 100)

# 反向迭代也可以
for j in reversed(deck):
    print(j)

# 实现排序
# 给四个花色赋值，指定花色大小
suit_values = dict(spades=3, diamonds=1, clubs=0, hearts=2)


# 排序函数
def spades_high(card):
    # 取出每张牌的下标
    rank_values = FrenchDeck.ranks.index(card.rank)
    print(rank_values)
    print('*' * 50)
    # 每张牌的下标乘以4再加上花色的大小得出该张牌在整套牌中的大小
    print(rank_values * len(suit_values) + suit_values[card.suit])
    return rank_values * len(suit_values) + suit_values[card.suit]


print('*' * 100)
# 排序并输出，一套扑克牌一张一张的传递给排序函数spades_high，根据返回值的大小最为关键字进行排序
for card in sorted(deck, key=spades_high):
    print(card)