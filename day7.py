class Hand:

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid

        self.card_values = self.get_card_values()
        self.hand_value = self.get_hand_value()

    def get_card_values(self):
        values = list[int]()
        value_dict = {
            "T": 10,
            "J": 1,
            "Q": 12,
            "K": 13,
            "A": 14
        }

        for card in self.cards:
            if card.isdigit():
                values.append(int(card))
            else:
                values.append(value_dict[card])

        return values

    def get_hand_value(self):
        counts = dict()
        joker_count = 0

        for card in self.cards:
            if card == "J":
                joker_count += 1
            elif card in counts.keys():
                counts[card] += 1
            else:
                counts[card] = 1

        count_list = list()
        for count in counts.values():
            count_list.append(count)

        count_list.sort()
        count_list.reverse()

        if joker_count != 5:
            count_list[0] += joker_count
        else:
            count_list.append(joker_count)

        max_count = count_list[0]
        if max_count != 5:
            second_count = count_list[1]
        else:
            second_count = 0

        if max_count == 5:
            return 6
        elif max_count == 4:
            return 5
        elif max_count == 3:
            if second_count == 2:
                return 4
            return 3
        elif max_count == 2:
            if second_count == 2:
                return 2
            return 1
        elif max_count == 1:
            return 0

    def __lt__(self, other):
        if self.hand_value != other.hand_value:
            return self.hand_value < other.hand_value
        else:
            for i in range(len(self.card_values)):
                if self.card_values[i] < other.card_values[i]:
                    return True
                elif self.card_values[i] > other.card_values[i]:
                    return False
        return False

    def __eq__(self, other):
        return not self < other and not other < self

    def __ne__(self, other):
        return self < other or other < self

    def __le__(self, other):
        return not other < self

    def __ge__(self, other):
        return not self < other

    def __gt__(self, other):
        return other < self


f = open("files/day7input.txt")
lines = f.readlines()

hands = list[Hand]()
for line in lines:
    cards = line[0:5]
    bid = int(line[6:])

    hand = Hand(cards, bid)
    hands.append(hand)

hands.sort()
score = 0
for i in range(len(hands)):
    j = i+1
    score += j*hands[i].bid
    print(hands[i].cards + " " + str(hands[i].bid))

print(score)