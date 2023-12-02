#!/usr/bin/env python3

import re

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

number_pattern = re.compile("(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))")


def process_file():
    total = 0

    with open("input.txt") as file:
        while True:
            line = file.readline()

            if not line:
                break

            total += text_as_number(line)

    print(f"Sum: {total}")


def text_as_number(text):
    matches = re.findall(number_pattern, text)
    return int(numbers.get(matches[0], matches[0]) + numbers.get(matches[-1], matches[-1]))


if __name__ == '__main__':
    process_file()
