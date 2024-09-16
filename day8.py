import re
import math


def fill_dict(d: dict[tuple[str, str]], strings):
    for i in range(2, len(strings)):
        string = strings[i]
        nodes = re.findall("[A-Z]{3}", string)
        key = nodes[0]
        left = nodes[1]
        right = nodes[2]

        d[key] = tuple((left, right))


f = open("files/day8input.txt")
lines = f.readlines()

directions = lines[0].strip()
node_dict = dict()
fill_dict(node_dict, lines)

steps = 0
current_node = "AAA"
loops = 0

while current_node != "ZZZ":
    print("loops: " + str(loops))
    loops += 1

    for direction in directions:
        print(direction)
        if direction == "L":
            current_node = node_dict[current_node][0]
        elif direction == "R":
            current_node = node_dict[current_node][1]
        steps += 1
        if current_node == "ZZZ":
            break

starting_nodes = list()
ending_nodes = list()
node_steps = dict()

for node in node_dict.keys():
    if node[2] == "A":
        starting_nodes.append(node)

for node in node_dict.keys():
    if node[2] == "Z":
        ending_nodes.append(node)

print(starting_nodes)
print(ending_nodes)

for node in starting_nodes:
    current_node = node
    steps = 0

    while current_node not in ending_nodes:
        for direction in directions:
            if direction == "L":
                current_node = node_dict[current_node][0]
            elif direction == "R":
                current_node = node_dict[current_node][1]
            steps += 1
            if current_node in ending_nodes:
                break

    node_steps[node] = steps

print(node_steps)

value_list = list()

for value in node_steps.values():
    value_list.append(value)

lcm = list()

for i in range(len(value_list) - 1):
    lcm.append(math.lcm(value_list[i], value_list[i+1]))

size = len(lcm)
while size > 1:
    new_lcm = list()

    for i in range(len(lcm)-1):
        new_lcm.append(math.lcm(lcm[i], lcm[i+1]))

    lcm = new_lcm
    size = len(lcm)

print(lcm)