import regex as re


def get_nums_from_string(string):
    """
    Finds all integers that appear in the provided string and returns them as a list.

    :param string: The string to parse into ints
    :return: An ordered list of the integers that appear in string
    """
    nums = re.findall("[-]?[0-9]+", string)

    ints = list()
    for num in nums:
        ints.append(int(num))

    return ints


def get_max(items):
    """
    Gets the maximum item from the provided list

    :param items: A list of integers
    :return: The largest item in the list
    """
    max_count = items[0]

    for item in items:
        if item > max_count:
            max_count = item
    return max_count


def get_min(items):
    """
    Gets the minimum item from the provided list

    :param items: A list of integers
    :return: The smallest item in the list
    """
    min_count = items[0]

    for item in items:
        if item < min_count:
            min_count = item
    return min_count


string_to_int = {
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
