import unittest

from hand_selector.domain.card import Card
from hand_selector.domain.deck_suite import DeckSuite
from hand_selector.domain.deck_value import DeckValue
from hand_selector.hands_helper import HandsHelper


class TestHandsHelper(unittest.TestCase):
    def test_is_straight_should_return_true_if_cards_are_ordered(self):
        card1 = Card(DeckSuite.TILES, DeckValue.SIX)
        card2 = Card(DeckSuite.TILES, DeckValue.SEVEN)
        card3 = Card(DeckSuite.HEARTS, DeckValue.EIGHT)
        card4 = Card(DeckSuite.TILES, DeckValue.NINE)
        card5 = Card(DeckSuite.CLOVERS, DeckValue.TEN)
        self.assertTrue(HandsHelper.is_straight(card1, card2, card3, card4, card5))

        card6 = Card(DeckSuite.TILES, DeckValue.TEN)
        card7 = Card(DeckSuite.TILES, DeckValue.JACK)
        card8 = Card(DeckSuite.HEARTS, DeckValue.QUEEN)
        card9 = Card(DeckSuite.TILES, DeckValue.KING)
        card10 = Card(DeckSuite.CLOVERS, DeckValue.ACE)
        self.assertTrue(HandsHelper.is_straight(card6, card7, card8, card9, card10))

    def test_is_straight_should_return_false(self):
        card1 = Card(DeckSuite.TILES, DeckValue.TWO)
        card2 = Card(DeckSuite.TILES, DeckValue.THREE)
        card3 = Card(DeckSuite.TILES, DeckValue.EIGHT)
        card4 = Card(DeckSuite.TILES, DeckValue.NINE)
        card5 = Card(DeckSuite.CLOVERS, DeckValue.ACE)
        self.assertFalse(HandsHelper.is_straight(card1, card2, card3, card4, card5))

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

    def test_is_four_of_kind_should_return_true_for_four_cards_with_same_values(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.TILES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card4 = Card(DeckSuite.TILES, DeckValue.JACK)
        card5 = Card(DeckSuite.PIKES, DeckValue.ACE)
        self.assertTrue(HandsHelper.is_four_of_kind(card1, card2, card3, card4, card5))

    def test_is_four_of_kind_should_return_false(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.TILES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card4 = Card(DeckSuite.TILES, DeckValue.KING)
        card5 = Card(DeckSuite.PIKES, DeckValue.ACE)
        self.assertFalse(HandsHelper.is_four_of_kind(card1, card2, card3, card4, card5))

    def test_is_full_house_should_return_true_for_three_and_two_cards_with_same_value(
        self
    ):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card4 = Card(DeckSuite.TILES, DeckValue.KING)
        card5 = Card(DeckSuite.PIKES, DeckValue.KING)
        self.assertTrue(HandsHelper.is_full_house(card1, card2, card3, card4, card5))

    def test_is_full_house_should_return_false(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.PIKES, DeckValue.ACE)
        card3 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card4 = Card(DeckSuite.TILES, DeckValue.KING)
        card5 = Card(DeckSuite.PIKES, DeckValue.KING)
        self.assertFalse(HandsHelper.is_full_house(card1, card2, card3, card4, card5))

    def test_is_three_of_kind_should_return_true_for_three_cards_with_same_value(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card4 = Card(DeckSuite.TILES, DeckValue.ACE)
        card5 = Card(DeckSuite.PIKES, DeckValue.TWO)
        self.assertTrue(HandsHelper.is_three_of_kind(card1, card2, card3, card4, card5))

    def test_is_three_of_kind_should_return_false(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.PIKES, DeckValue.KING)
        card3 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card4 = Card(DeckSuite.TILES, DeckValue.ACE)
        card5 = Card(DeckSuite.PIKES, DeckValue.TWO)
        self.assertFalse(
            HandsHelper.is_three_of_kind(card1, card2, card3, card4, card5)
        )

    def test_two_pair_should_return_true_for_three_cards_with_same_value(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.ACE)
        card4 = Card(DeckSuite.TILES, DeckValue.ACE)
        card5 = Card(DeckSuite.PIKES, DeckValue.TWO)
        self.assertTrue(HandsHelper.two_pair(card1, card2, card3, card4, card5))

    def test_two_pair_should_return_false(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.ACE)
        card4 = Card(DeckSuite.TILES, DeckValue.THREE)
        card5 = Card(DeckSuite.PIKES, DeckValue.TWO)
        self.assertFalse(HandsHelper.two_pair(card1, card2, card3, card4, card5))

    def test_one_pair_should_return_true(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.QUEEN)
        card4 = Card(DeckSuite.TILES, DeckValue.THREE)
        card5 = Card(DeckSuite.PIKES, DeckValue.ACE)
        self.assertTrue(HandsHelper.one_pair(card1, card2, card3, card4, card5))

    def test_one_pair_should_return_false(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.SEVEN)
        card2 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.QUEEN)
        card4 = Card(DeckSuite.TILES, DeckValue.THREE)
        card5 = Card(DeckSuite.PIKES, DeckValue.ACE)
        self.assertFalse(HandsHelper.one_pair(card1, card2, card3, card4, card5))
