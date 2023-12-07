from functools import reduce

with open("2023/day6/input.txt") as f:
    data = f.readlines()

time = int("".join(data[0].split(":")[1].split()))
distance = int("".join(data[1].split(":")[1].split()))

option_count = 0
for accel in range(time):
    if (distance) < (accel * (time - accel)):
        option_count += 1

print(option_count)