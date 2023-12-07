from functools import reduce

with open("2023/day5/input.txt") as f:
    file = f.read()

sections = file.split("\n\n")

def process_map(numbers):
    lines = numbers.split("\n")
    source_dest_size: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines if line]
    return source_dest_size

for section in sections:
    title, numbers = section.split(":")
    match title:
        case "seeds":
            seeds = numbers.split()
        case "seed-to-soil map":
            seed_soil_tuples = process_map(numbers)
        case "soil-to-fertilizer map":
            seed_fertilizer_tuples = process_map(numbers)
        case "fertilizer-to-water map":
            fertilizer_water_tuples = process_map(numbers)
        case "water-to-light map":
            water_light_tuples = process_map(numbers)
        case "light-to-temperature map":
            light_temp_tuples = process_map(numbers)
        case "temperature-to-humidity map":
            temp_humidity_tuples = process_map(numbers)
        case "humidity-to-location map":
            humidity_location_tuples = process_map(numbers)

all_tuples = [seed_soil_tuples, seed_fertilizer_tuples, fertilizer_water_tuples, water_light_tuples, light_temp_tuples, temp_humidity_tuples, humidity_location_tuples]

def tuples_lookup(x, tuples):
    for (dst, src, sz) in tuples:
      if src<=x<src+sz:
        return x+dst-src
    return x

locations = []
for seed in seeds:
    locations.append(reduce(tuples_lookup, all_tuples, int(seed)))

print(min(locations))