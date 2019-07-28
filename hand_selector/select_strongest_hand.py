from hand_selector.domain.hand import Hand
from hand_selector.hands_helper import HandsHelper


def select_strongest_hand(*hands: Hand) -> Hand:
    royal_flush = any(HandsHelper.is_royal_flush(*hand.cards) for hand in hands)
    if royal_flush:
        return next(x for x in hands if royal_flush)
    four_of_kind = any(HandsHelper.is_four_of_kind(*hand.cards) for hand in hands)
    if four_of_kind:
        return next(x for x in hands if four_of_kind)
    full_house = any(HandsHelper.is_full_house(*hand.cards) for hand in hands)
    if full_house:
        return next(x for x in hands if full_house)
    three_of_kind = any(HandsHelper.is_three_of_kind(*hand.cards) for hand in hands)
    if three_of_kind:
        return next(x for x in hands if three_of_kind)
    two_pair = any(HandsHelper.is_two_pair(*hand.cards) for hand in hands)
    if two_pair:
        return next(x for x in hands if two_pair)
    one_pair = any(HandsHelper.is_one_pair(*hand.cards) for hand in hands)
    if one_pair:
        return next(x for x in hands if one_pair)
