from hand_selector.domain.card import Card


class Hand:

    def __init__(self, *cards: Card) -> None:
        self.cards = cards

    def __eq__(self, o) -> bool:
        return isinstance(o, Hand) and o.cards == self.cards
