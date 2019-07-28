import unittest

from hand_selector.convert_to_hands import convert_to_hands
from hand_selector.domain.card import Card
from hand_selector.domain.deck_suite import DeckSuite
from hand_selector.domain.deck_value import DeckValue
from hand_selector.domain.hand import Hand


class TestConvertToHands(unittest.TestCase):
    def test_convert_to_hands_should_return_array_of_hands_with_cards(self):
        card1 = Card(DeckSuite.HEARTS, DeckValue.EIGHT)
        card2 = Card(DeckSuite.TILES, DeckValue.TEN)
        card3 = Card(DeckSuite.PIKES, DeckValue.ACE)
        hand1 = Hand(card1, card2, card3)

        card4 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card5 = Card(DeckSuite.HEARTS, DeckValue.QUEEN)
        card6 = Card(DeckSuite.CLOVERS, DeckValue.KING)
        hand2 = Hand(card4, card5, card6)

        self.assertListEqual([hand1, hand2], convert_to_hands("H8 T10 PA, PJ HQ CK"))
