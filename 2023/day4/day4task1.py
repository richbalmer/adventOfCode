total = 0

with open("2023/day4/input.txt") as f:
    for line in f:
        line = line.strip()
        card_id, winning_ours = line.split(":")
        winning, ours = winning_ours.split("|")
        winning_numbers = winning.split()
        ours_numbers = ours.split()

        intersection = list(set(winning_numbers) & set(ours_numbers))
        score = 0
        if len(intersection):
            score = pow(2, len(intersection) - 1)
            total += score

print(total)