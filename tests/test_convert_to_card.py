import unittest

from hand_selector.convert_to_card import convert_to_card
from hand_selector.domain.card import Card
from hand_selector.domain.deck_suite import DeckSuite
from hand_selector.domain.deck_value import DeckValue


class TestConvertToCard(unittest.TestCase):
    def test_convert_to_card_should_create_card_from_2_chars(self):
        card1 = Card(DeckSuite.HEARTS, DeckValue.EIGHT)
        self.assertEqual(card1, convert_to_card("H8"))

    def test_convert_to_card_should_create_card_from_3_chars(self):
        card1 = Card(DeckSuite.TILES, DeckValue.TEN)
        self.assertEqual(card1, convert_to_card("T10"))
