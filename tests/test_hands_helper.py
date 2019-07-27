import unittest

from hand_selector.domain.card import Card
from hand_selector.domain.deck_suite import DeckSuite
from hand_selector.domain.deck_value import DeckValue
from hand_selector.hands_helper import HandsHelper


class TestHandsHelper(unittest.TestCase):
    def test_is_straight_flush_should_return_true_if_cards_are_ordered(self):
        card1 = Card(DeckSuite.TILES, DeckValue.SIX)
        card2 = Card(DeckSuite.TILES, DeckValue.SEVEN)
        card3 = Card(DeckSuite.HEARTS, DeckValue.EIGHT)
        card4 = Card(DeckSuite.TILES, DeckValue.NINE)
        card5 = Card(DeckSuite.CLOVERS, DeckValue.TEN)
        self.assertTrue(
            HandsHelper.is_straight_flush(card1, card2, card3, card4, card5)
        )

        card6 = Card(DeckSuite.TILES, DeckValue.TEN)
        card7 = Card(DeckSuite.TILES, DeckValue.JACK)
        card8 = Card(DeckSuite.HEARTS, DeckValue.QUEEN)
        card9 = Card(DeckSuite.TILES, DeckValue.KING)
        card10 = Card(DeckSuite.CLOVERS, DeckValue.ACE)
        self.assertTrue(
            HandsHelper.is_straight_flush(card6, card7, card8, card9, card10)
        )

    def test_is_straight_flush_should_return_false(self):
        card1 = Card(DeckSuite.TILES, DeckValue.TWO)
        card2 = Card(DeckSuite.TILES, DeckValue.THREE)
        card3 = Card(DeckSuite.TILES, DeckValue.EIGHT)
        card4 = Card(DeckSuite.TILES, DeckValue.NINE)
        card5 = Card(DeckSuite.CLOVERS, DeckValue.ACE)
        self.assertFalse(
            HandsHelper.is_straight_flush(card1, card2, card3, card4, card5)
        )

    def test_is_flush_should_return_true_if_cards_are_of_one_kind(self):
        card1 = Card(DeckSuite.TILES, DeckValue.TWO)
        card2 = Card(DeckSuite.TILES, DeckValue.THREE)
        card3 = Card(DeckSuite.TILES, DeckValue.EIGHT)
        card4 = Card(DeckSuite.TILES, DeckValue.NINE)
        card5 = Card(DeckSuite.TILES, DeckValue.ACE)
        self.assertTrue(HandsHelper.is_flush(card1, card2, card3, card4, card5))

    def test_is_flush_should_return_false(self):
        card1 = Card(DeckSuite.TILES, DeckValue.TWO)
        card2 = Card(DeckSuite.TILES, DeckValue.THREE)
        card3 = Card(DeckSuite.TILES, DeckValue.SEVEN)
        card4 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card5 = Card(DeckSuite.TILES, DeckValue.ACE)
        self.assertFalse(HandsHelper.is_flush(card1, card2, card3, card4, card5))

    def test_is_royal_flush_should_return_true_if_deck_is_flush_and_straight_flush(
        self
    ):
        card1 = Card(DeckSuite.TILES, DeckValue.TEN)
        card2 = Card(DeckSuite.TILES, DeckValue.JACK)
        card3 = Card(DeckSuite.TILES, DeckValue.QUEEN)
        card4 = Card(DeckSuite.TILES, DeckValue.KING)
        card5 = Card(DeckSuite.TILES, DeckValue.ACE)
        self.assertTrue(HandsHelper.is_royal_flush(card1, card2, card3, card4, card5))

    def test_is_royal_flush_should_return_false(self):
        card1 = Card(DeckSuite.TILES, DeckValue.TEN)
        card2 = Card(DeckSuite.TILES, DeckValue.JACK)
        card3 = Card(DeckSuite.TILES, DeckValue.TWO)
        card4 = Card(DeckSuite.TILES, DeckValue.KING)
        card5 = Card(DeckSuite.TILES, DeckValue.ACE)
        self.assertFalse(HandsHelper.is_royal_flush(card1, card2, card3, card4, card5))
