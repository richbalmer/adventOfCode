import re

inputs = []

with open("day1/input1.txt") as f:
    for line in f:
        number = re.sub("[^0-9]", "", line)
        inputs.append(int(number[0] + number[-1]))

print(sum(inputs))