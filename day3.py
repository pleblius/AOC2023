import re
import utils


def get_number_indexes(string: str) -> list[tuple]:
    results = list()

    for match in re.finditer("[0-9]+", string):
        results.append((match.start(), match.end()-1, int(match.group())))

    return results


def get_gear_indexes(string: str) -> list[int]:
    results = list()

    for match in re.finditer("[*]", string):
        results.append(match.start())

    return results


def check_indexes_for_symbol(string, low_index, high_index) -> bool:
    if low_index != 0:
        low_index -= 1

    if high_index != len(string)-1:
        high_index += 1

    if re.search("[^.a-z0-9]", string[low_index:high_index]):
        return True

    return False


def get_gear_ratio(line_number, gear_position) -> int:
    num_numbers = 0
    gear_num = 0

    if line_number != 0:
        nums = get_number_indexes(lines[line_number-1])
        for i in range(len(nums)):
            if is_in_range(nums[i][1], gear_position):
                num_numbers += 1
                if gear_num != 0:
                    gear_num *= nums[i][2]
                else:
                    gear_num = nums[i][2]

            elif is_in_range(nums[i][0], gear_position):
                num_numbers += 1
                if gear_num != 0:
                    gear_num *= nums[i][2]
                else:
                    gear_num = nums[i][2]

    nums = get_number_indexes(lines[line_number])
    for i in range(len(nums)):
        if is_in_range(nums[i][1], gear_position):
            num_numbers += 1
            if gear_num != 0:
                gear_num *= nums[i][2]
            else:
                gear_num = nums[i][2]

        elif is_in_range(nums[i][0], gear_position):
            num_numbers += 1
            if gear_num != 0:
                gear_num *= nums[i][2]
            else:
                gear_num = nums[i][2]

    if line_number != len(lines)-1:
        nums = get_number_indexes(lines[line_number + 1])
        for i in range(len(nums)):
            if is_in_range(nums[i][1], gear_position):
                num_numbers += 1
                if gear_num != 0:
                    gear_num *= nums[i][2]
                else:
                    gear_num = nums[i][2]

            elif is_in_range(nums[i][0], gear_position):
                num_numbers += 1
                if gear_num != 0:
                    gear_num *= nums[i][2]
                else:
                    gear_num = nums[i][2]

    if num_numbers == 2:
        return gear_num
    else:
        return 0


def is_in_range(pos1, pos2):
    if pos1 == pos2 or pos1 == pos2-1 or pos1 == pos2+1:
        return True
    return False


f = open("files/day3input.txt")

lines = f.readlines()

part_sum = 0

for i in range(len(lines)):
    for match in get_number_indexes(lines[i]):
        low = match[0]
        high = match[1]
        num = match[2]

        if i == 0:
            if check_indexes_for_symbol(lines[i], low, high):
                part_sum += num
            elif check_indexes_for_symbol(lines[i+1], low, high):
                part_sum += num
        elif i is len(lines)-1:
            if check_indexes_for_symbol(lines[i-1], low, high):
                part_sum += num
            elif check_indexes_for_symbol(lines[i], low, high):
                part_sum += num
        else:
            if check_indexes_for_symbol(lines[i-1], low, high):
                part_sum += num
            elif check_indexes_for_symbol(lines[i], low, high):
                part_sum += num
            elif check_indexes_for_symbol(lines[i+1], low, high):
                part_sum += num

print(part_sum)

gear_sum = 0

for i in range(len(lines)):
    for gear in get_gear_indexes(lines[i]):
        gear_sum += get_gear_ratio(i, gear)

print(gear_sum)
