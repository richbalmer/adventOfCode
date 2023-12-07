import collections

with open("2023/day7/input.txt") as f:
    data = f.readlines()

hand_type_rank = ["fivekind", "fourkind", "house", "threekind", "twopair", "onepair", "highcard"]

def hand_type(hand):
    common_chars = collections.Counter(hand).most_common(2)
    common_char = common_chars[0][0]
    if common_char == "J" and len(common_chars) > 1:
        common_char = common_chars[1][0]
    new_hand = hand.replace("J", common_char)
    sorted_cards = sorted(new_hand)
    if sorted_cards[0] == sorted_cards[1] == sorted_cards[2] == sorted_cards[3] == sorted_cards[4]:
        rank = 0
    elif sorted_cards[0] == sorted_cards[1] == sorted_cards[2] == sorted_cards[3] or sorted_cards[1] == sorted_cards[2] == sorted_cards[3] == sorted_cards[4]:
        rank = 1
    elif (sorted_cards[0] == sorted_cards[1] == sorted_cards[2] and sorted_cards[3] == sorted_cards[4]) or (sorted_cards[2] == sorted_cards[3] == sorted_cards[4]) and (sorted_cards[0] == sorted_cards[1]):
        rank = 2
    elif sorted_cards[0] == sorted_cards[1] == sorted_cards[2] or sorted_cards[1] == sorted_cards[2] == sorted_cards[3] or sorted_cards[2] == sorted_cards[3] == sorted_cards[4]:
        rank = 3
    elif (sorted_cards[0] == sorted_cards[1] and (sorted_cards[2] == sorted_cards[3] or sorted_cards[3] == sorted_cards[4])) or (sorted_cards[1] == sorted_cards[2] and sorted_cards[3] == sorted_cards[4]):
        rank = 4
    elif sorted_cards[0] == sorted_cards[1] or sorted_cards[1] == sorted_cards[2] or sorted_cards[2] == sorted_cards[3] or sorted_cards[3] == sorted_cards[4]:
        rank = 5
    else:
        rank = 6
    return hand_type_rank[rank]

hand_bid_map = {}
hands_by_type = {
    "fivekind": [],
    "fourkind": [],
    "house": [],
    "threekind": [],
    "twopair": [],
    "onepair": [],
    "highcard": []
}
for line in data:
    hand, bid = line.split()
    hand_bid_map[hand] = int(bid)
    hands_by_type[hand_type(hand)].append(hand)

card_rank = "AKQT98765432J"
score = 0
current_rank = len(data)
for rank in hand_type_rank:
    for hand in sorted(hands_by_type[rank], key=lambda word: [card_rank.index(c) for c in word]):
        score += hand_bid_map[hand] * current_rank
        current_rank -= 1

print(score)