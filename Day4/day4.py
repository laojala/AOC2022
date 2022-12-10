'''
Solutions for https://adventofcode.com/2022/day/4

'''

import os

def read_input() -> list:
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        all_lines = [d.rstrip().split(',') for d in file.readlines()]
    all_lines = [[area.split('-') for area in pair ] for pair in all_lines]
    all_lines = [[[int(item) for item in area] for area in pair] for pair in all_lines]
    return all_lines

def count_part1(data:list) -> int:
    #sort pairs so that smallest item of the second area is first
    [sub_list.sort(key = lambda x: x[1]) for sub_list in data]

    overlapping = 0
    for first, second in data:
        if second[1] == first[1]:
            overlapping += 1
        if second[1] > first[1]:
            if first[0] >= second[0]:
                overlapping +=1
    return overlapping

def count_part2(data:list) -> int:
    # sort data so that first item of first pair is the smallest
    [pair.sort(key = lambda x: x[0]) for pair in data]
    overlapping = 0
    for first, second in data:
        if first[1] >= second[0]:
            overlapping += 1
    return overlapping

def solve() -> None:
    data = read_input()

    part1_result = count_part1(data)
    print(part1_result)
    assert part1_result == 471 or part1_result == 2

    part2_result = count_part2(data)
    print(part2_result)
    assert part2_result == 888 or part2_result == 4

if __name__ == '__main__':
    solve()
