import math

matrix = []
with open("2023/day10/input.txt", "r") as file:
    for line in file:
        row = list(line.strip())
        matrix.append(row)

line_markers = [[0]*len(matrix[0]) for _ in range(len(matrix))]

def find_next_letter(letter, i, j, prev_i, prev_j):
    match letter:
        case "F":
            return (matrix[i+1][j], i+1, j, i, j) if prev_i != i+1 else (matrix[i][j+1], i, j+1, i, j)
        case "L":
            return (matrix[i-1][j], i-1, j, i, j) if prev_i != i-1 else (matrix[i][j+1], i, j+1, i, j)
        case "7":
            return (matrix[i+1][j], i+1, j, i, j) if prev_i != i+1 else (matrix[i][j-1], i, j-1, i, j)
        case "J":
            return (matrix[i-1][j], i-1, j, i, j) if prev_i != i-1 else (matrix[i][j-1], i, j-1, i, j)
        case "|":
            return (matrix[i+1][j], i+1, j, i, j) if prev_i != i+1 else (matrix[i-1][j], i-1, j, i, j)
        case "-":
            return (matrix[i][j+1], i, j+1, i, j) if prev_j != j+1 else (matrix[i][j-1], i, j-1, i, j)
    return None
    

def find_next_letter_from_start():
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == "S":
                # Check adjacent positions
                if i > 0: # Up
                    if matrix[i-1][j] in ["|", "7", "F"]:
                        return (matrix[i-1][j], i-1, j, i, j)
                if i < len(matrix) - 1: # Down
                    if matrix[i+1][j] in ["|", "J", "L"]:
                        return (matrix[i+1][j], i+1, j, i, j)
                if j > 0:  # Left
                    if matrix[i][j-1] in ["-", "F", "L"]:
                        return (matrix[i][j-1], i, j-1, i, j)
                if j < len(row) - 1:  # Right
                    if matrix[i][j+1] in ["-", "7", "J"]:
                        return (matrix[i][j+1], i, j+1, i, j)
    return None

next_letter = find_next_letter_from_start()
# print(f"Next letter from 'S': {next_letter}")

hops = 0
while next_letter[0] != "S":
    next_letter = find_next_letter(*next_letter)
    line_markers[next_letter[3]][next_letter[4]] = 1
    hops += 1
    # print(f"Next letter: {next_letter}, hops: {hops}")

print(math.ceil(hops/2))

next_letter = find_next_letter_from_start()
s_vert = True if next_letter[1] < next_letter[3] else False  # True if the next letter is above S (i.e. S is in "|JL")
line_markers[next_letter[3]][next_letter[4]] = 1

count = 0
for i in range(len(matrix)):
    inside = False
    for j in range(len(matrix[i])):
        if line_markers[i][j]:
            if matrix[i][j] in "|JL" or (matrix[i][j] == "S" and s_vert): inside = not inside
        else:
            count += inside

print(count)