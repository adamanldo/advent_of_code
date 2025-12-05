from functools import cmp_to_key

hands_and_bids = open("input/7", "r").read().split("\n")


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.type = self.get_type(cards)
        self.bid = bid

    def get_type(self, cards):
        d = {}
        for c in cards:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        if len(d.keys()) == 1:
            return "five_of_a_kind"
        elif len(d.keys()) == 2:
            if any(v >= 4 for v in d.values()):
                return "four_of_a_kind"
            else:
                return "full_house"
        elif len(d.keys()) == 3:
            if any(v >= 3 for v in d.values()):
                return "three_of_a_kind"
            else:
                return "two_pair"
        elif len(d.keys()) == 4:
            return "one_pair"
        else:
            return "high_card"

    def __str__(self):
        return f"Cards: {self.cards}, Bid: {self.bid}, Type: {self.type}"

    def __repr__(self):
        return self.__str__()


TYPE_RANKINGS = {
    "five_of_a_kind": 7,
    "four_of_a_kind": 6,
    "full_house": 5,
    "three_of_a_kind": 4,
    "two_pair": 3,
    "one_pair": 2,
    "high_card": 1,
}

CARD_RANKINGS = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def compare_hands(hand1: Hand, hand2: Hand):
    if TYPE_RANKINGS[hand1.type] < TYPE_RANKINGS[hand2.type]:
        return -1
    elif TYPE_RANKINGS[hand1.type] > TYPE_RANKINGS[hand2.type]:
        return 1
    else:
        for card1, card2 in zip(hand1.cards, hand2.cards):
            if CARD_RANKINGS[card1] == CARD_RANKINGS[card2]:
                continue
            elif CARD_RANKINGS[card1] < CARD_RANKINGS[card2]:
                return -1
            elif CARD_RANKINGS[card1] > CARD_RANKINGS[card2]:
                return 1


def main():
    hands = []
    for row in hands_and_bids:
        c, b = row.split()
        b = int(b)
        hands.append(Hand(c, b))
    ranked_hands = sorted(hands, key=cmp_to_key(compare_hands))
    total = 0
    for idx, hand in enumerate(ranked_hands, start=1):
        total += idx * hand.bid
    return total


print(main())
