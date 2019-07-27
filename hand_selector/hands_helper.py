from hand_selector.domain.card import Card


class HandsHelper:
    @staticmethod
    def is_straight_flush(*cards: Card) -> bool:
        vals = [card.value.get_value() for card in cards]
        return vals == list(range(vals[0], vals[-1] + 1))

    @staticmethod
    def is_flush(*cards: Card) -> bool:
        return len(set(map(lambda card: card.suit, cards))) == 1

    @staticmethod
    def is_royal_flush(*cards: Card) -> bool:
        return HandsHelper.is_straight_flush(*cards) and HandsHelper.is_flush(*cards)
