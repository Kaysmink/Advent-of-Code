Input = open("data/2023/dag 07. input.txt", "r").read().split("\n")[0:-1]
hands = [line.split(" ")[0] for line in Input]
bids = [int(line.split(" ")[1]) for line in Input]
bids_dict = {hands[index]: bids[index] for index, hand in enumerate(hands)}


card_scores = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12,
               "K": 13, "A": 14}

letter_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
               12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w',
               23: 'x', 24: 'y', 25: 'z'}


def select_new_value(hand_chars):
    if not hand_chars:
        return 2

    return max(set(hand_chars), key=hand_chars.count)


def get_type(hand, part):
    card_order = "".join([letter_dict[card_scores[card]] for card in hand])
    hand_chars = list(hand)

    """
    if part2, replace all J's to the most common card in the hand
    """
    if part == "part2":
        num_j = hand_chars.count("J")
        hand_chars = [card for card in hand_chars if card != "J"]

        for x in range(0, num_j):
            hand_chars.append(select_new_value(hand_chars))

    numbers = set(hand_chars)
    cards_per_number = [hand_chars.count(number) for number in numbers]

    """
    if one element occures 5 times then 5 of a kind
    if one element occures 4 times then 4 of a kind
    if one element occures 3 times and another element 2 times then fullhouse
    etc
    """
    if cards_per_number.count(5) == 1:
        return "6" + card_order
    if cards_per_number.count(4) == 1:
        return "5" + card_order
    if cards_per_number.count(3) == 1 and cards_per_number.count(2) >= 1:
        return "4" + card_order
    if cards_per_number.count(3) == 1:
        return "3" + card_order
    if cards_per_number.count(2) == 2:
        return "2" + card_order
    if cards_per_number.count(2) == 1:
        return "1" + card_order
    return "0" + card_order


def run_part(part):
    hand_scores = [get_type(hand, part) for hand in hands]
    score_to_hand_dict = {hand_scores[index]: hands[index] for index, hand in enumerate(hand_scores)}
    sorted_hands = sorted(hand_scores, reverse=True)

    return sum(
        [(len(sorted_hands) - index) * bids_dict[score_to_hand_dict[hand]] for index, hand in enumerate(sorted_hands)])


part1 = run_part("part1")
card_scores["J"] = 1
part2 = run_part("part2")

print(part1, part2)
