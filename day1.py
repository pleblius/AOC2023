import re


def parse_string(string):
    digits = re.findall("[0-9]", string)
    digit1 = digits[0]
    digit2 = digits[-1]

    return 10 * int(digit1) + int(digit2)


f = open("files/day1input.txt")

lines = f.readlines()
count = 0
line: str
for line in lines:
    count = count + parse_string(line)

print(count)