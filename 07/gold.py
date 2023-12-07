ORDER = {'J': 0, '2': 1, '3': 2, '4': 3, '5': 4,
         '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12}

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


def get_hand_type(hand):
    struc_hand = dict()
    for c in hand:
        if c not in struc_hand.keys():
            struc_hand[c] = 1
        else:
            struc_hand[c] += 1
    if 'J' in struc_hand.keys():
        jokers = struc_hand['J']
        struc_hand.pop('J')
        if len(struc_hand.keys()) == 0:
            struc_hand = {'J': 5}
        else:
            card_with_largest_amount = list(struc_hand.keys())[0]
            for (card, amount) in struc_hand.items():
                if amount > struc_hand[card_with_largest_amount]:
                    card_with_largest_amount = card
            struc_hand[card_with_largest_amount] += jokers

    if any(amount == 5 for (card, amount) in struc_hand.items()):
        return FIVE_OF_A_KIND
    if any(amount == 4 for (card, amount) in struc_hand.items()):
        return FOUR_OF_A_KIND
    if any(amount == 3 for (card, amount) in struc_hand.items()) and any(amount == 2 for (card, amount) in struc_hand.items()):
        return FULL_HOUSE
    if any(amount == 3 for (card, amount) in struc_hand.items()):
        return THREE_OF_A_KIND
    if len(list(filter(lambda x: x[1] == 2, struc_hand.items()))) == 2:
        return TWO_PAIR
    if any(amount == 2 for (card, amount) in struc_hand.items()):
        return ONE_PAIR
    return HIGH_CARD


def get_hand_key(hand):
    key = [get_hand_type(hand)] + [ORDER[c] for c in hand]
    return tuple(key)


def main():
    hands = []
    with open("07/input.txt") as f:
        hands = [(line.rstrip().split()[0], int(line.rstrip().split()[1]))
                 for line in f]
    hands.sort(key=lambda x: get_hand_key(x[0]))

    winnings = 0
    for rank in range(1, len(hands)+1):
        winnings += rank * hands[rank-1][1]

    print(winnings)


if __name__ == "__main__":
    main()
