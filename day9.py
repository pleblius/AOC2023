import utils


def get_differences(input_list) -> list[int]:
    return_list = list()

    for i in range(len(input_list)-1):
        return_list.append(input_list[i+1] - input_list[i])

    return return_list


def all_zeroes(input_list) -> bool:
    for input in input_list:
        if input != 0:
            return False

    return True


def add_element(input_list) -> int:
    differences = get_differences(input_list)

    if not all_zeroes(differences):
        add_element(differences)

    last_element = input_list[-1]
    last_difference = differences[-1]

    num = last_element + last_difference
    input_list.append(num)

    return num


def add_prev_element(input_list) -> int:
    differences = get_differences(input_list)

    if not all_zeroes(differences):
        add_prev_element(differences)

    first_element = input_list[0]
    first_difference = differences[0]

    num = first_element - first_difference
    input_list.insert(0, num)

    return num

f = open("files/day9input.txt")
lines = f.readlines()

sum = 0

for line in lines:
    nums = utils.get_nums_from_string(line.strip())
    sum += add_element(nums)

print(sum)

sum = 0

for line in lines:
    nums = utils.get_nums_from_string(line.strip())
    sum += add_prev_element(nums)

print(sum)