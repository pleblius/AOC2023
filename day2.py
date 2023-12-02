import regex as re


def is_game_valid(string):
    red_max = 12
    green_max = 13
    blue_max = 14
    red_pattern = "[0-9]+ red"
    green_pattern = "[0-9]+ green"
    blue_pattern = "[0-9]+ blue"

    red_strings = re.findall(red_pattern, string)
    green_strings = re.findall(green_pattern, string)
    blue_strings = re.findall(blue_pattern, string)

    red_counts = list()
    for red_string in red_strings:
        red_counts.append(int(re.findall("[0-9]+", red_string)[0]))

    for red_count in red_counts:
        if red_count > red_max:
            return False

    green_counts = list()
    for green_string in green_strings:
        green_counts.append(int(re.findall("[0-9]+", green_string)[0]))
    for green_count in green_counts:
        if green_count > green_max:
            return False

    blue_counts = list()
    for blue_string in blue_strings:
        blue_counts.append(int(re.findall("[0-9]+", blue_string)[0]))
    for blue_count in blue_counts:
        if blue_count > blue_max:
            return False

    return True


def get_power(string):
    red_pattern = "[0-9]+ red"
    green_pattern = "[0-9]+ green"
    blue_pattern = "[0-9]+ blue"

    red_strings = re.findall(red_pattern, string)
    green_strings = re.findall(green_pattern, string)
    blue_strings = re.findall(blue_pattern, string)

    red_counts = list()
    red_max = 0

    for red_string in red_strings:
        red_counts.append(int(re.findall("[0-9]+", red_string)[0]))

    for red_count in red_counts:
        if red_count > red_max:
            red_max = red_count

    green_counts = list()
    green_max = 0

    for green_string in green_strings:
        green_counts.append(int(re.findall("[0-9]+", green_string)[0]))
    for green_count in green_counts:
        if green_count > green_max:
            green_max = green_count

    blue_counts = list()
    blue_max = 0

    for blue_string in blue_strings:
        blue_counts.append(int(re.findall("[0-9]+", blue_string)[0]))
    for blue_count in blue_counts:
        if blue_count > blue_max:
            blue_max = blue_count

    return red_max*green_max*blue_max


def get_id(string):
    return int(re.findall("[0-9]+", string)[0])


f = open("files/day2input.txt")
lines = f.readlines()
id_sum = 0
for line in lines:
    if is_game_valid(line):
        id_sum += get_id(line)

print("Sum of ID's: ", id_sum)

power_sum = 0
for line in lines:
    power_sum += get_power(line)

print("Sum of powers: ", power_sum)
