import sys

import utils
sys.setrecursionlimit(100000)
f = open("files/day10input.txt")
lines = f.readlines()
new_lines = lines
f.close()
width = 0
height = len(lines)
f = open("files/day10input2.txt", mode="w")

pipe_types = {
    "F": ["right", "down"],
    "J": ["left", "up"],
    "7": ["left", "down"],
    "L": ["right", "up"],
    "|": ["up", "down"],
    "-": ["left", "right"],
    ".": ["none"],
    "S": ["up", "down", "left", "right"]
}
visited = list()

i = 0
start = [0, 0]

for j in range(height):
    line = lines[j]
    width = len(line)

    if "S" in line:
        i = line.find("S")
        start[0] = i
        start[1] = j
        break


def check_inlet(pipe, in_direction):
    if in_direction == "right":
        if "left" in pipe_types[pipe]:
            return True
    elif in_direction == "left":
        if "right" in pipe_types[pipe]:
            return True
    elif in_direction == "up":
        if "down" in pipe_types[pipe]:
            return True
    elif in_direction == "down":
        if "up" in pipe_types[pipe]:
            return True
    return False


def get_pipe(x, y):
    return lines[y][x]


def get_outlet_dir(pipe, inlet_dir):
    if inlet_dir == "left":
        for direction in pipe_types[pipe]:
            if direction != "right":
                return direction
    elif inlet_dir == "right":
        for direction in pipe_types[pipe]:
            if direction != "left":
                return direction
    elif inlet_dir == "up":
        for direction in pipe_types[pipe]:
            if direction != "down":
                return direction
    elif inlet_dir == "down":
        for direction in pipe_types[pipe]:
            if direction != "up":
                return direction

    return "none"


def get_right_tiles(x, y, dir, outlet_dir):
    right_tiles = list()
    if dir == "up" and outlet_dir == "up":
        right_tiles.append([x+1, y])
    elif dir == "down" and outlet_dir == "down":
        right_tiles.append([x-1, y])
    elif dir == "right" and outlet_dir == "right":
        right_tiles.append([x, y+1])
    elif dir == "left" and outlet_dir == "left":
        right_tiles.append([x,y-1])
    elif dir == "left" and outlet_dir == "down":
        right_tiles.append([x-1,y])
        right_tiles.append([x, y-1])
        right_tiles.append([x-1, y-1])
    elif dir == "left" and outlet_dir == "up":
        pass
    elif dir == "right" and outlet_dir == "up":
        right_tiles.append([x+1,y])
        right_tiles.append([x, y+1])
        right_tiles.append([x+1, y+1])
    elif dir == "right" and outlet_dir == "down":
        pass
    elif dir == "up" and outlet_dir == "left":
        right_tiles.append([x+1,y])
        right_tiles.append([x, y-1])
        right_tiles.append([x+1, y-1])
    elif dir == "up" and outlet_dir == "right":
        pass
    elif dir == "down" and outlet_dir == "left":
        pass
    elif dir == "down" and outlet_dir == "right":
        right_tiles.append([x-1,y])
        right_tiles.append([x, y+1])
        right_tiles.append([x-1, y+1])

    return right_tiles


def move(x, y, dir):
    if dir == "left":
        x -= 1
    elif dir == "right":
        x += 1
    elif dir == "up":
        y -= 1
    elif dir == "down":
        y += 1
    else:
        return False

    if x >= width or x < 0 or y >= height or y < 0:
        return False

    pos = [x, y]
    pipe = get_pipe(x, y)

    if not check_inlet(pipe, dir):
        return False

    if pos == start:
        visited.append(pos)
        return True

    outlet_dir = get_outlet_dir(pipe, dir)
    if outlet_dir == "none":
        return False

    if move(x, y, outlet_dir):
        visited.append(pos)
        return True
    else:
        return False


def move_and_replace(x, y, dir):
    old_x = x
    old_y = y

    if dir == "left":
        x -= 1
    elif dir == "right":
        x += 1
    elif dir == "up":
        y -= 1
    elif dir == "down":
        y += 1
    else:
        return False

    pos = [x, y]
    pipe = get_pipe(x, y)
    if pos == start:
        return True
    outlet_dir = get_outlet_dir(pipe, dir)

    right_tiles = get_right_tiles(old_x, old_y, dir, outlet_dir)
    for right_pos in right_tiles:
        right_x = right_pos[0]
        right_y = right_pos[1]

        if 0 <= right_x < width-1 and 0 <= right_y < height and right_pos not in visited:
            old_right_line = new_lines[right_y]
            new_right_line = old_right_line[0:right_x] + "E" + old_right_line[right_x+1:width]
            new_lines[right_y] = new_right_line

    if move_and_replace(x, y, outlet_dir):
        return True
    else:
        return False


start_list = list()
for key in pipe_types.keys():
    start_list.append(key)

for start_pipe in start_list:
    start_direction = pipe_types[start_pipe][0]

    if move(start[0], start[1], start_direction):
        break

print(visited)
print(start_pipe)
print(len(visited)/2)

start_pipe = "F"
start_direction = "up"
move_and_replace(start[0], start[1], start_direction)

newer_lines = new_lines

write_pos = [-1, -1]

for new_line in new_lines:
    write_pos[0] = -1
    write_pos[1] += 1

    newer_line = list()
    write_char = write_pos[0]

    closed_pos = False

    for char in new_line:
        write_pos[0] += 1

        if char == "E":
            newer_line.append(char)
            closed_pos = True
        elif char == "\n":
            newer_line.append(char)
        elif write_pos in visited:
            closed_pos = False
            newer_line.append(char)
        else:
            if closed_pos:
                newer_line.append("E")
            else:
                newer_line.append("U")

    newer_lines[write_pos[1]] = ''.join(map(str, newer_line))

for asdf in newer_lines:
    print(len(asdf))
    f.write(asdf)

f.close()
