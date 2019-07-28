from hand_selector.domain.deck_suite import DeckSuite
from hand_selector.domain.deck_value import DeckValue


class Card:

    def __init__(self, suit: DeckSuite, value: DeckValue) -> None:
        self.suit = suit
        self.value = value

    def __eq__(self, o) -> bool:
        return isinstance(o, Card) and o.suit == self.suit and o.value == self.value

    def __str__(self) -> str:
        return '{suite} {value}'.format(suite = self.suit.name, value = self.value.name)