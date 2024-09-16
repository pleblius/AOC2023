import regex as re


def parse_string(string):
    digits = parse_advanced(string)
    digit1 = digits[0]
    digit2 = digits[-1]

    int1 = get_int(digit1)
    int2 = get_int(digit2)

    return 10 * int1 + int2


def get_int(digit):
    num_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    if digit in num_dict.keys():
        return num_dict[digit]
    else:
        return int(digit)


def parse_advanced(string):
    pattern = "one|two|three|four|five|six|seven|eight|nine|[0-9]"
    return re.findall(pattern, string, overlapped=True)


f = open("files/day1input.txt")

lines = f.readlines()
count = 0
line: str
for line in lines:
    count = count + parse_string(line)

print(count)
