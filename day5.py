import utils


class RangeMap:
    def __init__(self):
        self.source_ranges = list[tuple[int, int]]()
        self.dest_ranges = list[tuple[int, int]]()

    def get_dest_from_source(self, source_num: int) -> int:
        source_index = self.get_source_index(source_num)
        if source_index == -1:
            return source_num

        source_base = (self.source_ranges[source_index])[0]
        dest_base = (self.dest_ranges[source_index])[0]

        difference = source_num - source_base
        return dest_base + difference

    def get_source_index(self, num) -> int:
        for i in range(len(self.source_ranges)):
            if self.source_ranges[i][0] <= num <= self.source_ranges[i][1]-1:
                return i
        return -1

    def add_source_range(self, base: int, length: int):
        tup = tuple((base, base + length))
        self.source_ranges.append(tup)

    def add_dest_range(self, base, length):
        self.dest_ranges.append((base, base + length))


def is_map_change(string) -> bool:
    if string.find("map:") != -1:
        return True
    return False


def get_next_map(string) -> dict:
    if string.find("to-soil") != -1:
        new_map = seed_to_soil_map
    elif string.find("to-fertilizer") != -1:
        new_map = soil_to_fert_map
    elif string.find("to-water") != -1:
        new_map = fert_to_water_map
    elif string.find("to-light") != -1:
        new_map = water_to_light_map
    elif string.find("to-temp") != -1:
        new_map = light_to_temp_map
    elif string.find("to-hum") != -1:
        new_map = temp_to_hum_map
    elif string.find("to-loc") != -1:
        new_map = hum_to_loc_map
    else:
        new_map = dict()

    return new_map


def get_loc_from_seed(asdf):
    asdff = seed_to_soil_map.get_dest_from_source(asdf)
    asdfff = soil_to_fert_map.get_dest_from_source(asdff)
    asdffff = fert_to_water_map.get_dest_from_source(asdfff)
    asdfffff = water_to_light_map.get_dest_from_source(asdffff)
    asdffffff = light_to_temp_map.get_dest_from_source(asdfffff)
    asdfffffff = temp_to_hum_map.get_dest_from_source(asdffffff)
    asdffffffff = hum_to_loc_map.get_dest_from_source(asdfffffff)

    return asdffffffff


f = open("files/day5input.txt")
lines = f.readlines()

seed_list = list()
soil_list = list()
fert_list = list()
water_list = list()
light_list = list()
temp_list = list()
hum_list = list()
loc_list = list()

seed_to_soil_map = RangeMap()
soil_to_fert_map = RangeMap()
fert_to_water_map = RangeMap()
water_to_light_map = RangeMap()
light_to_temp_map = RangeMap()
temp_to_hum_map = RangeMap()
hum_to_loc_map = RangeMap()
current_map = RangeMap()

for line in lines:
    if line == "\n":
        continue
    elif line.find("seeds:") != -1:
        seed_list = utils.get_nums_from_string(line)
        continue
    elif is_map_change(line):
        current_map = get_next_map(line)
        continue

    map_nums = utils.get_nums_from_string(line)
    dest_start = map_nums[0]
    source_start = map_nums[1]
    length = map_nums[2]

    current_map.add_source_range(source_start, length)
    current_map.add_dest_range(dest_start, length)

for seed in seed_list:
    soil_list.append(seed_to_soil_map.get_dest_from_source(seed))

for soil in soil_list:
    fert_list.append(soil_to_fert_map.get_dest_from_source(soil))

for fert in fert_list:
    water_list.append(fert_to_water_map.get_dest_from_source(fert))

for water in water_list:
    light_list.append(water_to_light_map.get_dest_from_source(water))

for light in light_list:
    temp_list.append(light_to_temp_map.get_dest_from_source(light))

for temp in temp_list:
    hum_list.append(temp_to_hum_map.get_dest_from_source(temp))

for hum in hum_list:
    loc_list.append(hum_to_loc_map.get_dest_from_source(hum))

min_loc = utils.get_min(loc_list)
print(min_loc)

seed_list.clear()
soil_list.clear()
fert_list.clear()
water_list.clear()
light_list.clear()
temp_list.clear()
hum_list.clear()
loc_list.clear()

seeds = utils.get_nums_from_string(lines[0])

for i in range(0, len(seeds), 2):
    seed_base = seeds[i]
    seed_range = seeds[i+1]
    seed_max = seed_base + seed_range

    print(i)
    prev_loc = 0
    last_iter = 0

    for j in range(seed_base, seed_max, 5000):
        loc = get_loc_from_seed(j)

        if loc != 5000 + prev_loc:
            for k in range(j-5000, j+1):
                loc = get_loc_from_seed(k)

                if loc < min_loc:
                    min_loc = loc

                last_iter = k
        else:
            last_iter = j
            if loc < min_loc:
                min_loc = loc

        prev_loc = loc

    for j in range(last_iter, seed_max):
        newer_loc = get_loc_from_seed(j)

        if newer_loc < min_loc:
            min_loc = newer_loc

print(min_loc)
