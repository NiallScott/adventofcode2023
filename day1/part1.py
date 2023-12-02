#!/usr/bin/env python3

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
    return int(first_number(text) + last_number(text))


def first_number(text):
    for character in text:
        if character.isdigit():
            return character


def last_number(text):
    for character in text[::-1]:
        if character.isdigit():
            return character


if __name__ == '__main__':
    process_file()
