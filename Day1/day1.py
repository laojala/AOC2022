'''
Solutions for https://adventofcode.com/2022/day/1

'''

import os

def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r') as f:
        all_lines = [d.rstrip() for d in f.readlines()]
    return all_lines

def count_part1(elf_data):
    biggest_counter = 0
    next_counter = 0
    for item in elf_data:
        if item != '':
            next_counter += int(item)
        else:
            if next_counter > biggest_counter:
                biggest_counter = next_counter
            next_counter = 0
    return biggest_counter

def count_part2(elf_data):
    top_elves = [0, 0, 0]
    next_counter = 0
    for item in elf_data:
        if item != '':
            next_counter += int(item)
        else:
            if next_counter > min(top_elves):
                top_elves.remove(min(top_elves))
                top_elves.append(next_counter)
            next_counter = 0
    return sum(top_elves)

if __name__ == '__main__':
    data = read_input()

    part1_result = count_part1(data)
    print(part1_result)
    assert(part1_result == 67622)

    part2_result = count_part2(data)
    print(part2_result)
    assert(part2_result == 201491)
   