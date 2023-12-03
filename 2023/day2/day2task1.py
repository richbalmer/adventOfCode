
# 12 red cubes, 13 green cubes, and 14 blue cubes
total = 0

with open("day2/input1.txt") as f:
    for line in f:
        line = line.strip()
        game, setstring = line.split(":")
        sets = setstring.split(";")

        possible = True
        for set in sets:
            colourcounts = set.split(",")
            for colourcount in colourcounts:
                if "green" in colourcount:
                    count = int(colourcount.strip(" green"))
                    if count > 13:
                        possible = False
                        break
                if "red" in colourcount:
                    count = int(colourcount.strip(" red"))
                    if count > 12:
                        possible = False
                        break
                if "blue" in colourcount:
                    count = int(colourcount.strip(" blue"))
                    if count > 14:
                        possible = False
                        break
            if not possible:
                break

        if possible:
            total += int(game[5:])

print(total)