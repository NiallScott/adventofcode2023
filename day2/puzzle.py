#!/usr/bin/env python3

import re


def extract_game_id(game_text):
    return int(re.search(r"\d+", game_text).group())


def is_game_possible(game_text):
    bag_picks = game_text.split(";")

    for pick in bag_picks:
        is_possible = is_bag_pick_possible(pick.strip())

        if not is_possible:
            return False

    return True


def is_bag_pick_possible(bag_pick_text):
    cubes = bag_pick_text.split(",")

    for cube in cubes:
        is_possible = is_cube_possible(cube.strip())

        if not is_possible:
            return False

    return True


def is_cube_possible(cube_text):
    number = int(re.search(r"\d+", cube_text).group())

    if "red" in cube_text:
        return number <= 12
    elif "green" in cube_text:
        return number <= 13
    elif "blue" in cube_text:
        return number <= 14


def get_game_power(game_text):
    maximums = get_game_cube_maximums(game_text)
    power = 1

    for v in maximums.values():
        power = power * v

    return power


def get_game_cube_maximums(game_text):
    colour_counts = dict()
    bag_picks = game_text.split(";")

    for pick in bag_picks:
        counts = get_bag_pick_counts(pick.strip())

        for k, v in counts.items():
            current = colour_counts.get(k)

            if current is None or current < v:
                colour_counts[k] = v

    return colour_counts


def get_bag_pick_counts(bag_pick_text):
    colour_counts = dict()
    cubes = bag_pick_text.split(",")

    for cube in cubes:
        result = get_colour_and_count(cube.strip())
        current = colour_counts.get(result[1])

        if current is None or current < result[0]:
            colour_counts[result[1]] = result[0]

    return colour_counts


def get_colour_and_count(cube_text):
    split = re.split(r"\s+", cube_text)
    return int(split[0]), split[1]


assert extract_game_id("Game 1") == 1
assert extract_game_id("Game 11") == 11
assert is_game_possible("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
assert is_game_possible("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
assert not is_game_possible("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
assert not is_game_possible("1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
assert is_game_possible("6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
assert is_bag_pick_possible("3 green, 4 blue, 1 red")
assert not is_bag_pick_possible("8 green, 6 blue, 20 red")
assert is_cube_possible("12 red")
assert not is_cube_possible("13 red")
assert is_cube_possible("13 green")
assert not is_cube_possible("14 green")
assert is_cube_possible("14 blue")
assert not is_cube_possible("15 blue")
assert get_colour_and_count("12 red") == (12, "red")
assert get_bag_pick_counts("1 red, 2 green, 3 blue") == {"red": 1, "green": 2, "blue": 3}
assert get_game_cube_maximums("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == {"red": 4, "green": 2, "blue": 6}
assert get_game_cube_maximums("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == {
    "red": 1,
    "green": 3,
    "blue": 4}
assert get_game_cube_maximums("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == {
    "red": 20,
    "green": 13,
    "blue": 6
}
assert get_game_cube_maximums("1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == {
    "red": 14,
    "green": 3,
    "blue": 15
}
assert get_game_cube_maximums("6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green") == {"red": 6, "green": 3, "blue": 2}
assert get_game_power("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 48
assert get_game_power("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == 12
assert get_game_power("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == 1560
assert get_game_power("1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == 630
assert get_game_power("6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green") == 36

if __name__ == '__main__':
    id_sum = 0
    power_sum = 0

    with open("input.txt") as file:
        while True:
            line = file.readline()

            if not line:
                break

            game_split = line.split(":")
            game_id = extract_game_id(game_split[0])

            if is_game_possible(game_split[1]):
                id_sum += game_id

            power_sum += get_game_power(game_split[1])

    print(f"Part 1: {id_sum}")
    print(f"Part 2: {power_sum}")
