import re

inputs = []

number_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
pat = re.compile(r"(?=(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9))", flags = re.I)

with open("day1/input1.txt") as f:
    for line in f:
        numbers = pat.findall(line)
        first = number_words[numbers[0]] if numbers[0] in number_words else int(numbers[0])
        last = number_words[numbers[-1]] if numbers[-1] in number_words else int(numbers[-1])
        inputs.append(int(str(first) + str(last)))
        print(line, first, last, int(str(first) + str(last)))

print(sum(inputs))
