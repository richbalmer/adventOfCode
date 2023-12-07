from functools import reduce

with open("2023/day6/input.txt") as f:
    data = f.readlines()

times = [int(x) for x in data[0].split(":")[1].split()]
distances = [int(x) for x in data[1].split(":")[1].split()]

option_counts = []
for time, distance in zip(times, distances):
    options = []
    for accel in range(time):
        if (distance) < (accel * (time - accel)):
            options.append(accel)
    option_counts.append(len(options))

print(reduce(lambda x, y: x * y, option_counts))