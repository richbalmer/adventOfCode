# Read the input file
with open('2023/day9/input.txt', 'r') as file:
    lines = file.readlines()

# Create a list of sequences of integers
sequences = []
for line in lines:
    sequence = [int(num) for num in line.strip().split()]
    sequences.append(sequence)

def get_next_value(history):
    if all(n == 0 for n in history):
        return 0
    else:
        diff = [history[i + 1] - history[i] for i in range(len(history) - 1)]
        return history[-1] + get_next_value(diff)
    
def get_prev_value(history):
    if all(n == 0 for n in history):
        return 0
    else:
        diff = [history[i + 1] - history[i] for i in range(len(history) - 1)]
        return history[0] - get_prev_value(diff)


result1 = 0
result2 = 0
for sequence in sequences:
    result1 += get_next_value(sequence)
    result2 += get_prev_value(sequence)

print(result1)
print(result2)