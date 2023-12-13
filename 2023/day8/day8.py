filename = "2023/day8/input.txt"

with open(filename, "r") as file:
    lines = file.readlines()
    instructions = [dir for dir in lines[0].strip()]
    node_mappings = {line.strip().split(" = ")[0]: tuple(line.strip().split(" = ")[1].strip("()").split(", ")) for line in lines[2:]}

current_node = "AAA"
hops = 0

while current_node != "ZZZ":
    instruction = instructions.pop(0)
    instructions.append(instruction)
    hops += 1

    if instruction == "R":
        current_node = node_mappings[current_node][1]
    elif instruction == "L":
        current_node = node_mappings[current_node][0]

print(hops)
