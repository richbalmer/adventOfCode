
# 12 red cubes, 13 green cubes, and 14 blue cubes
total = 0

with open("day2/input1.txt") as f:
    for line in f:
        line = line.strip()
        game, setstring = line.split(":")
        sets = setstring.split(";")

        maxred = 0
        maxgreen = 0
        maxblue = 0
        for set in sets:
            colourcounts = set.split(",")
            for colourcount in colourcounts:
                if "green" in colourcount:
                    count = int(colourcount.strip(" green"))
                    if count > maxgreen:
                        maxgreen = count
                if "red" in colourcount:
                    count = int(colourcount.strip(" red"))
                    if count > maxred:
                        maxred = count
                if "blue" in colourcount:
                    count = int(colourcount.strip(" blue"))
                    if count > maxblue:
                        maxblue = count
        total += maxred * maxgreen * maxblue

print(total)