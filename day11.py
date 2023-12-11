import utils


def get_empty_verticals(lines: list[str]) -> list[int]:
    vertical_lines = list()

    for i in range(len(lines[-1])):
        galaxy_found = False

        for line in lines:
            if line[i] == "#":
                galaxy_found = True

        if not galaxy_found:
            vertical_lines.append(i)

    return vertical_lines


def get_empty_horizontals(lines) -> list[int]:
    horizontal_lines = list()

    for i in range(len(lines)):
        line = lines[i]
        galaxy_found = False

        for char in line:
            if char == "#":
                galaxy_found = True

        if not galaxy_found:
            horizontal_lines.append(i)

    return horizontal_lines


def grow_space(lines, empty_verticals, empty_horizontals) -> list[str]:
    new_lines = list()

    # Grow horizontal lines
    for i in range(len(lines)):
        new_lines.append(lines[i])

        if i in empty_horizontals:
            new_lines.append(lines[i])

    num_grows = 0
    # Grow vertical lines
    for i in range(len(new_lines[-1])):
        if i in empty_verticals:
            for j in range(len(new_lines)):
                new_line = new_lines[j]
                head = new_line[0:i+num_grows]
                tail = new_line[i+num_grows:]
                new_line = head + "." + tail
                new_lines[j] = new_line
            num_grows += 1


    return new_lines


def get_galaxies(lines) -> list[list[int]]:
    galaxy_list = list()

    for i in range(len(lines)):
        line = lines[i]

        for j in range(len(lines[-1])):
            if line[j] == "#":
                galaxy_list.append([j, i])

    return galaxy_list


def get_distance(galaxy1: list[int], galaxy2: list[int], empty_verticals, empty_horizontals) -> int:
    galaxy1_x = galaxy1[0]
    galaxy1_y = galaxy1[1]
    galaxy2_x = galaxy2[0]
    galaxy2_y = galaxy2[1]

    galaxy1_grows_x = 0
    galaxy1_grows_y = 0
    galaxy2_grows_x = 0
    galaxy2_grows_y = 0

    for vert in empty_verticals:
        if vert < galaxy1_x:
            galaxy1_grows_x += 1
        if vert < galaxy2_x:
            galaxy2_grows_x += 1

    for horizontal in empty_horizontals:
        if horizontal < galaxy1_y:
            galaxy1_grows_y += 1
        if horizontal < galaxy2_y:
            galaxy2_grows_y += 1

    grow_factor = 2
    galaxy1_new_x = galaxy1_x + (grow_factor-1)*galaxy1_grows_x
    galaxy1_new_y = galaxy1_y + (grow_factor-1)*galaxy1_grows_y
    galaxy2_new_x = galaxy2_x + (grow_factor-1)*galaxy2_grows_x
    galaxy2_new_y = galaxy2_y + (grow_factor-1)*galaxy2_grows_y

    x_dist = abs(galaxy1_new_x - galaxy2_new_x)
    y_dist = abs(galaxy1_new_y - galaxy2_new_y)

    return x_dist + y_dist


f = open("files/day11input.txt")
lines = f.readlines()
f.close()

empty_verts = get_empty_verticals(lines)
empty_hor = get_empty_horizontals(lines)

galaxy_list = get_galaxies(lines)

total_dist = 0
for i in range(len(galaxy_list)):
    for j in range(i+1, len(galaxy_list)):
        total_dist += get_distance(galaxy_list[i], galaxy_list[j], empty_verts, empty_hor)

print(total_dist)
