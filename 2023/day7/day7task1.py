with open("2023/day7/input.txt") as f:
    data = f.readlines()

def hand_type(hand):
    sorted_cards = sorted(hand)
    if sorted_cards[0] == sorted_cards[1] == sorted_cards[2] == sorted_cards[3] == sorted_cards[4]:
        return "fivekind"
    if sorted_cards[0] == sorted_cards[1] == sorted_cards[2] == sorted_cards[3] or sorted_cards[1] == sorted_cards[2] == sorted_cards[3] == sorted_cards[4]:
        return "fourkind"
    if (sorted_cards[0] == sorted_cards[1] == sorted_cards[2] and sorted_cards[3] == sorted_cards[4]) or (sorted_cards[2] == sorted_cards[3] == sorted_cards[4]) and (sorted_cards[0] == sorted_cards[1]):
        return "house"
    if sorted_cards[0] == sorted_cards[1] == sorted_cards[2] or sorted_cards[1] == sorted_cards[2] == sorted_cards[3] or sorted_cards[2] == sorted_cards[3] == sorted_cards[4]:
        return "threekind"
    if (sorted_cards[0] == sorted_cards[1] and (sorted_cards[2] == sorted_cards[3] or sorted_cards[3] == sorted_cards[4])) or (sorted_cards[1] == sorted_cards[2] and sorted_cards[3] == sorted_cards[4]):
        return "twopair"
    if sorted_cards[0] == sorted_cards[1] or sorted_cards[1] == sorted_cards[2] or sorted_cards[2] == sorted_cards[3] or sorted_cards[3] == sorted_cards[4]:
        return "onepair"
    return "highcard"

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

card_rank = "AKQJT98765432"
score = 0
rank = len(data)
for hand in sorted(hands_by_type["fivekind"], key=lambda word: [card_rank.index(c) for c in word]):
    score += hand_bid_map[hand] * rank
    rank -= 1
for hand in sorted(hands_by_type["fourkind"], key=lambda word: [card_rank.index(c) for c in word]):
    score += hand_bid_map[hand] * rank
    rank -= 1
for hand in sorted(hands_by_type["house"], key=lambda word: [card_rank.index(c) for c in word]):
    score += hand_bid_map[hand] * rank
    rank -= 1
for hand in sorted(hands_by_type["threekind"], key=lambda word: [card_rank.index(c) for c in word]):
    score += hand_bid_map[hand] * rank
    rank -= 1
for hand in sorted(hands_by_type["twopair"], key=lambda word: [card_rank.index(c) for c in word]):
    score += hand_bid_map[hand] * rank
    rank -= 1
for hand in sorted(hands_by_type["onepair"], key=lambda word: [card_rank.index(c) for c in word]):
    score += hand_bid_map[hand] * rank
    rank -= 1
for hand in sorted(hands_by_type["highcard"], key=lambda word: [card_rank.index(c) for c in word]):
    score += hand_bid_map[hand] * rank
    rank -= 1

print(score)