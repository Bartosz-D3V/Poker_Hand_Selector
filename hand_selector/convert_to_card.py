from hand_selector.domain.card import Card
from hand_selector.domain.deck_suite import DeckSuite
from hand_selector.domain.deck_value import DeckValue


def convert_to_card(val) -> Card:
    return (
        Card(DeckSuite(val[0:1]), DeckValue(val[1:2]))
        if len(val) == 2
        else Card(DeckSuite(val[0:1]), DeckValue(val[1:3]))
    )
