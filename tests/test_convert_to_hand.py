import unittest

from hand_selector.convert_to_hand import convert_to_hand
from hand_selector.domain.card import Card
from hand_selector.domain.deck_suite import DeckSuite
from hand_selector.domain.deck_value import DeckValue
from hand_selector.domain.hand import Hand


class TestConvertToCard(unittest.TestCase):
    def test_convert_to_hand_should_convert_string_to_hand(self):
        card1 = Card(DeckSuite.HEARTS, DeckValue.EIGHT)
        card2 = Card(DeckSuite.TILES, DeckValue.TEN)
        card3 = Card(DeckSuite.PIKES, DeckValue.ACE)
        hand = Hand(card1, card2, card3)

        self.assertEqual(hand, convert_to_hand("H8 T10 PA"))
