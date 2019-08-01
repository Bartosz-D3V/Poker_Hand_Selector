import sys

from hand_selector.convert_to_hands import convert_to_hands
from hand_selector.select_strongest_hand import select_strongest_hand


def main():
    hands = convert_to_hands(sys.argv[1])
    for card in select_strongest_hand(*hands).cards:
        print(f'{card}, ')


if __name__ == '__main__':
    main()
