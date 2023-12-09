import re
import sys
import utils


def get_winning_numbers(string, left_index, right_index):
    return utils.get_nums_from_string(string[left_index:right_index])


def get_card_numbers(string, left_index):
    return utils.get_nums_from_string(string[left_index:])


def get_num_wins(string):
    left_index = string.find(":")
    right_index = string.find("|")

    winning_numbers = get_winning_numbers(string, left_index, right_index)
    card_numbers = get_card_numbers(string, right_index)

    num_wins = 0
    for card_number in card_numbers:
        if card_number in winning_numbers:
            num_wins += 1

    return num_wins


def get_card_count(strings, index):
    count = 1

    if index in card_win_totals.keys():
        return card_win_totals[index]

    if index < len(strings):
        num_wins = get_num_wins(strings[index])
        for i in range(index+1, index + 1 + num_wins):
            count += get_card_count(strings, i)

    card_win_totals[index] = count

    return count


f = open("files/day4input.txt")
lines = f.readlines()

total_score = 0

for line in lines:
    num_wins = get_num_wins(line)
    if num_wins > 0:
        total_score += 2**(num_wins - 1)

print(total_score)

total_cards = 0

sys.setrecursionlimit(10000)

card_win_totals = dict()

for i in range(len(lines)-1, -1, -1):
    total_cards += get_card_count(lines, i)
    print(i)

print(total_cards)
