import unittest

from hand_selector.domain.card import Card
from hand_selector.domain.deck_suite import DeckSuite
from hand_selector.domain.deck_value import DeckValue
from hand_selector.domain.hand import Hand
from hand_selector.select_strongest_hand import select_strongest_hand


class TestSelectStrongestHand(unittest.TestCase):
    def test_select_strongest_hand_should_return_royal_flush(self):
        card1 = Card(DeckSuite.TILES, DeckValue.TEN)
        card2 = Card(DeckSuite.TILES, DeckValue.JACK)
        card3 = Card(DeckSuite.TILES, DeckValue.QUEEN)
        card4 = Card(DeckSuite.TILES, DeckValue.KING)
        card5 = Card(DeckSuite.TILES, DeckValue.ACE)
        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card7 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card8 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card9 = Card(DeckSuite.TILES, DeckValue.KING)
        card10 = Card(DeckSuite.PIKES, DeckValue.KING)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(hand1, select_strongest_hand(hand1, hand2))

    def test_select_strongest_hand_should_return_four_of_kind(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.TILES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card4 = Card(DeckSuite.TILES, DeckValue.JACK)
        card5 = Card(DeckSuite.PIKES, DeckValue.ACE)
        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card7 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card8 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card9 = Card(DeckSuite.TILES, DeckValue.KING)
        card10 = Card(DeckSuite.PIKES, DeckValue.KING)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(hand1, select_strongest_hand(hand1, hand2))

    def test_select_strongest_hand_should_return_full_house(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card4 = Card(DeckSuite.TILES, DeckValue.KING)
        card5 = Card(DeckSuite.PIKES, DeckValue.KING)
        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card7 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card8 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card9 = Card(DeckSuite.TILES, DeckValue.ACE)
        card10 = Card(DeckSuite.PIKES, DeckValue.TWO)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(hand1, select_strongest_hand(hand1, hand2))

    def test_select_strongest_hand_should_return_three_of_kind(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.JACK)
        card4 = Card(DeckSuite.TILES, DeckValue.ACE)
        card5 = Card(DeckSuite.PIKES, DeckValue.TWO)
        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card7 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card8 = Card(DeckSuite.HEARTS, DeckValue.ACE)
        card9 = Card(DeckSuite.TILES, DeckValue.ACE)
        card10 = Card(DeckSuite.PIKES, DeckValue.TWO)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(hand1, select_strongest_hand(hand1, hand2))

    def test_select_strongest_hand_should_return_two_pair(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.ACE)
        card4 = Card(DeckSuite.TILES, DeckValue.ACE)
        card5 = Card(DeckSuite.PIKES, DeckValue.TWO)
        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card7 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card8 = Card(DeckSuite.HEARTS, DeckValue.QUEEN)
        card9 = Card(DeckSuite.TILES, DeckValue.THREE)
        card10 = Card(DeckSuite.PIKES, DeckValue.ACE)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(hand1, select_strongest_hand(hand1, hand2))

    def test_select_strongest_hand_should_return_one_pair(self):
        card1 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card2 = Card(DeckSuite.PIKES, DeckValue.JACK)
        card3 = Card(DeckSuite.HEARTS, DeckValue.QUEEN)
        card4 = Card(DeckSuite.TILES, DeckValue.THREE)
        card5 = Card(DeckSuite.PIKES, DeckValue.ACE)
        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(DeckSuite.CLOVERS, DeckValue.JACK)
        card7 = Card(DeckSuite.PIKES, DeckValue.TWO)
        card8 = Card(DeckSuite.HEARTS, DeckValue.QUEEN)
        card9 = Card(DeckSuite.TILES, DeckValue.THREE)
        card10 = Card(DeckSuite.PIKES, DeckValue.ACE)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(hand1, select_strongest_hand(hand1, hand2))
