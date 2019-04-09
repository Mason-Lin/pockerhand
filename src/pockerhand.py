import itertools
from collections import Counter

class Player(object):
    def __init__(self, name, str_handcards):
        self._name = name
        self._handcards = Handcards(str_handcards)

    @property
    def handcards(self):
        return self._handcards

    @property
    def name(self):
        return self._name

    @property
    def pattern_rank(self):
        return self._handcards._pattern._pattern_rank

    @property
    def pattern_name(self):
        return self._handcards._pattern._pattern_name

    def __gt__(self, other):
        if self.pattern_rank > other.pattern_rank:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.pattern_rank == other.pattern_rank:
            return True
        else:
            return False


class Pattern(object):
    def __init__(self, card_list):
        self._pattern_lookup = {
            'Straight Flush': 9,
            'Four of a Kind': 8,
            'Full house': 7,
            'Flush': 6,
            'Straight': 5,
            'Three of a kind': 4,
            'Two Pairs': 3,
            'One Pair': 2,
            'High card': 1
        }
        self._pattern_name = self.parse_pattern(card_list)
        self._pattern_rank = self._pattern_lookup[self._pattern_name]

    @property
    def pattern_rank(self):
        return self._pattern_rank

    def parse_pattern(self, card_list):
        suit_list = [card.suit for card in card_list]
        suit_group = Counter(suit_list)
        rank_list = [card.rank for card in card_list]
        rank_group = Counter(rank_list)
        
        has_flush = self.flush_detector(suit_group)
        pair_count = self.pair_counter(rank_group)
        triple_count = self.triple_counter(rank_group)
        has_four = self.four_detector(rank_group)
        has_straight = self.straight_detector(rank_group)

        if has_straight and has_flush:
            return 'Straight Flush'
        elif has_four:
            return 'Four of a Kind'
        elif pair_count == 1 and triple_count == 1:
            return 'Full house'
        elif has_flush:
            return 'Flush'
        elif has_straight:
            return 'Straight'
        elif pair_count == 0 and triple_count == 1:
            return 'Three of a kind'
        elif pair_count == 2:
            return 'Two Pairs'
        elif pair_count == 1 and triple_count == 0:
            return 'One Pair'
        else:
            return 'High card'

    def flush_detector(self, suit_group):
        for count in suit_group.values():
            if count == 5:
                return True
        else:
            return False

    def straight_detector(self, rank_list):
        rank_set = set(rank_list)
        max_min_dist = max(rank_set) - min(rank_set) + 1
        is_straight = (max_min_dist == len(rank_list)) and len(rank_set) == len(rank_list)
        return True if is_straight else False

    def pair_counter(self, rank_group):
        pair_count = 0
        for count in rank_group.values():
            if count == 2:
                pair_count += 1
        return pair_count

    def triple_counter(self, rank_group):
        triple_count = 0
        for count in rank_group.values():
            if count == 3:
                triple_count += 1
        return triple_count

    def four_detector(self, rank_group):
        for count in rank_group.values():
            if count == 4:
                return True
        else:
            return False


class Handcards(object):
    def __init__(self, str_handcards):
        self._card_list = self.parse_cards(str_handcards)
        self._pattern = self.verify_pattern(self._card_list)

    @property
    def card_list(self):
        return self._card_list

    @property
    def pattern(self):
        return self._pattern

    def parse_cards(self, str_handcards):
        card_list = []
        str_card_list = str_handcards.split(',')
        for str_card in str_card_list:
            card = Card(str_card.strip())
            card_list.append(card)
        return card_list

    def verify_pattern(self, card_list):
        return Pattern(card_list)


class Card(object):
    def __init__(self, str_card):
        self._suit = str_card[0].upper()
        self._rank = int(str_card[1])

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank


class Game(object):
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2

    def play(self):
        if self.p1 > self.p2:
            print(self.p1.name, 'win:', self.p1.pattern_name)
        elif self.p1 == self.p2:
            print('draw', self.p1.pattern_name, self.p2.pattern_name)
        else:
            print(self.p2.name, 'win:', self.p2.pattern_name)

if __name__ == '__main__':
    print('game setup')
    p1 = Player('Mason', 'S2, D3, D4, C5, C6')
    p2 = Player('Rina', 'H5, H3, D5, D7, C9')

    print('game play')
    game = Game(p1, p2)
    game.play()

    print('bye')
