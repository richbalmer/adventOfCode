input= []

with open("2023/day3/input.txt") as f:
    for line in f:
        line = line.strip()
        input.append(line)

selected_numbers = []
current_number = ""
number_is_selected = False

for line_index, line in enumerate(input):
    for char_index, char in enumerate(line):
        if char.isnumeric():
            current_number += char
            if not number_is_selected:
                # Search for an adjacent symbol
                for search_line_index in range(line_index - 1, line_index + 2):
                    if search_line_index >= 0 and search_line_index < len(input):
                        search_line = input[search_line_index]
                        for search_char_index in range(char_index - 1, char_index + 2):
                            if search_char_index >= 0 and search_char_index < len(search_line):
                                search_char = search_line[search_char_index]
                                if not search_char.isnumeric() and search_char not in ".\n":
                                    number_is_selected = True
        else:
            if number_is_selected:
                selected_numbers.append(int(current_number))
            number_is_selected = False
            current_number = ""
    if number_is_selected:
        selected_numbers.append(int(current_number))
    number_is_selected = False
    current_number = ""

if number_is_selected:
    selected_numbers.append(int(current_number))
    
print(sum(selected_numbers))