import re
import utils

f = open("files/day6input.txt")
lines = f.readlines()

times = utils.get_nums_from_string(lines[0])
distances = utils.get_nums_from_string(lines[1])

total_wins = list()

for i in range(len(times)):
    time = times[i]
    distance = distances[i]

    wins = 0
    for j in range(time):
        speed = j
        distance_traversed = speed*(time-j)

        if distance_traversed > distance:
            wins += 1

    total_wins.append(wins)

ways = 1
for wins in total_wins:
    ways *= wins

print(ways)

new_time = str()
new_dist = str()

for time in times:
    new_time += str(time)
for distance in distances:
    new_dist += str(distance)

new_time = int(new_time)
new_dist = int(new_dist)
wins = 0

for i in range(new_time):
    speed = i
    distance_traversed = speed*(new_time - i)

    if distance_traversed > new_dist:
        wins += 1

print(wins)
