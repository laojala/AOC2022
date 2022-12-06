'''
Solutions for https://adventofcode.com/2022/day/6

'''

import os
from collections import deque

def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        return file.read()

def unique_values(values: list) -> bool:
    """checks if list values are unique"""
    length = len(values)
    unique = set(values)
    length_unique = len(unique)
    if length_unique != length:
        return False
    return True

def find_start_marker(signal: str, required_length: int) -> int:
    """returns index of a character that ends a substring of unique characters with a lenght of a required_length"""
    most_recent = deque()
    for index, char in enumerate(signal):
        most_recent.append(char)
        if len(most_recent) > required_length:
            most_recent.popleft()
        if len(most_recent) == required_length and unique_values(most_recent):
            return index + 1
    return -1   # no suitable substring found

def solve() -> None:
    data = read_input()

    part1_result = find_start_marker(data, 4)
    print(part1_result)
    assert part1_result == 1582 or 11

    part2_result = find_start_marker(data, 14)
    print(part2_result)
    assert part2_result == 3588 or 26

if __name__ == '__main__':
    solve()
