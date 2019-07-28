from hand_selector.domain.hand import Hand
from hand_selector.convert_to_card import convert_to_card


def convert_to_hand(seq: str) -> Hand:
    return Hand(*map(convert_to_card, seq.split()))
