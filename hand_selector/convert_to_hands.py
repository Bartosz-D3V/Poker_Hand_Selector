from hand_selector.convert_to_hand import convert_to_hand
from hand_selector.domain.hand import Hand


def convert_to_hands(val: str) -> [Hand]:
    return [*map(convert_to_hand, val.split(", "))]
