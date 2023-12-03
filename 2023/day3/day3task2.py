import math

input= []

with open("2023/day3/input.txt") as f:
    for line in f:
        line = line.strip()
        input.append(line)

numbers_next_to_gears = {}
current_number = ""
number_is_selected = False

for line_index, line in enumerate(input):
    for char_index, char in enumerate(line):
        if char.isnumeric():
            current_number += char
            if not number_is_selected:
                # Search for an adjacent gear
                for search_line_index in range(line_index - 1, line_index + 2):
                    if search_line_index >= 0 and search_line_index < len(input):
                        search_line = input[search_line_index]
                        for search_char_index in range(char_index - 1, char_index + 2):
                            if search_char_index >= 0 and search_char_index < len(search_line):
                                search_char = search_line[search_char_index]
                                if search_char == "*":
                                    number_is_selected = (search_line_index, search_char_index)
        else:
            if number_is_selected:
                if numbers_next_to_gears.get(number_is_selected):
                    numbers_next_to_gears[number_is_selected].append(int(current_number))
                else:
                    numbers_next_to_gears[number_is_selected] = [int(current_number)]
            number_is_selected = False
            current_number = ""
    if number_is_selected:
        if numbers_next_to_gears.get(number_is_selected):
            numbers_next_to_gears[number_is_selected].append(int(current_number))
        else:
            numbers_next_to_gears[number_is_selected] = [int(current_number)]
        number_is_selected = False
    current_number = ""

if number_is_selected:
    if numbers_next_to_gears.get(number_is_selected):
        numbers_next_to_gears[number_is_selected].append(int(current_number))
    else:
        numbers_next_to_gears[number_is_selected] = [int(current_number)]

selected_numbers = []
for numbers in numbers_next_to_gears.values():
    if len(numbers) == 2:
        selected_numbers.append(math.prod(numbers))

print(sum(selected_numbers))