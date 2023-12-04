scores = {}

with open("2023/day4/input.txt") as f:
    for index, line in enumerate(f):
        line = line.strip()
        card_id, winning_ours = line.split(":")
        winning, ours = winning_ours.split("|")
        winning_numbers = winning.split()
        ours_numbers = ours.split()

        intersection = len(set(winning_numbers) & set(ours_numbers))
        scores[index] = intersection

cards = [1 for _ in range(len(scores))]
for index, count in enumerate(cards):
    for _ in range(count):
        for i in range(scores[index]):
            if index + i + 1 in scores:
                cards[index + i + 1] += 1

print(sum(cards))