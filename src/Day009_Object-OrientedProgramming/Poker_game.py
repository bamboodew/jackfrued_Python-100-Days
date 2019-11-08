import random


class Card(object):
    """一张牌"""

    def __init__(self, suite, face):
        self._suite = suite  # 花色
        self._face = face

    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self):
        return self.__str__()


class Poker(object):
    """一副牌"""

    def __init__(self):
        # 4个花色*13个大小=52张牌
        self._cards = [Card(suite, face) for suite in '♠♥♣♦' for face in range(1, 14)]
        # 已发牌的数量
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    # @property
    # def has_next(self):
    #     """还有没有牌"""
    #     return self._current < len(self._cards)


class Player(object):
    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property  # getter
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        """理牌"""
        self._cards_on_hand.sort(key=card_key)


def get_key(card):
    return card.suite, card.face


def main():
    # 拿出一副牌
    p = Poker()
    # 洗牌：随机打乱
    p.shuffle()
    # 四个玩家
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    # 发牌13次
    for _ in range(13):
        # 每人1张
        for player in players:
            # 发牌
            player.get(p.next)
    # 各自亮牌
    for player in players:
        print(player.name + ':', end=' ')
        # 按顺序理牌
        player.arrange(get_key)
        # 亮牌
        print(player.cards_on_hand)


if __name__ == '__main__':
    main()
