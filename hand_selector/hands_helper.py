from collections import Counter

from hand_selector.domain.card import Card


class HandsHelper:
    @staticmethod
    def is_straight(*cards: Card) -> bool:
        vals = [card.value.get_value() for card in cards]
        return vals == list(range(vals[0], vals[-1] + 1))

    @staticmethod
    def is_flush(*cards: Card) -> bool:
        return len(set(map(lambda card: card.suit, cards))) == 1

    @staticmethod
    def is_royal_flush(*cards: Card) -> bool:
        return HandsHelper.is_straight(*cards) and HandsHelper.is_flush(*cards)

    @staticmethod
    def is_four_of_kind(*cards: Card) -> bool:
        return 4 in Counter([card.value.get_value() for card in cards]).values()

    @staticmethod
    def is_full_house(*cards: Card) -> bool:
        unique_vals_count = Counter([card.value.get_value() for card in cards]).values()
        return 3 in unique_vals_count and 2 in unique_vals_count

    @staticmethod
    def is_three_of_kind(*cards: Card) -> bool:
        return 3 in Counter([card.value.get_value() for card in cards]).values()

    @staticmethod
    def two_pair(*cards: Card) -> bool:
        unique_vals_count = Counter([card.value.get_value() for card in cards]).values()
        return sum([i == 2 for i in unique_vals_count]) == 2

    @staticmethod
    def one_pair(*cards: Card) -> bool:
        unique_vals_count = Counter([card.value.get_value() for card in cards]).values()
        return sum([i == 2 for i in unique_vals_count]) == 1
