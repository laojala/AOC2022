'''
Solutions for https://adventofcode.com/2022/day/3

'''

import os
import string


alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)


def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r') as f:
        all_lines = [d.rstrip() for d in f.readlines()]
    return all_lines



def put_to_half(string):
    half = round(len(string)/2)
    first_half = string[:half]
    second_half = string[half:]
    return [first_half, second_half]

def find_common_item(lists):
    for letter in lists[0]:
        if letter in lists[1]:
            return letter

def get_priority(string):
    return alphabet.index(string) + 1

def count_part1(all_rucksacks):
    priority = 0
    for rucksack in all_rucksacks:
        [first, second] = put_to_half(rucksack)
        common_item = find_common_item([first, second])
        letter_priority = get_priority(common_item)
        priority += letter_priority        
    return priority

def divide_to_chunks(lists):
    new = []
    start = 0
    end = len(lists)
    step = 3
    for i in range(start, end, step):
        x = i
        new.append(lists[x:x+step])
    return new

def find_common_item_from_bags(bags):
    for letter in bags[0]:
        if letter in bags[1] and letter in bags[2]:
            return letter


def count_part2(all_rucksacks):
    chuncks = divide_to_chunks(all_rucksacks)
    priority = 0
    for bags in chuncks:
        common_item =  find_common_item_from_bags(bags)
        priority += get_priority(common_item)   
    return priority



if __name__ == '__main__':
    data = read_input()

    part1_result = count_part1(data)
    print(part1_result)
    assert(part1_result == 8185)

    part2_result = count_part2(data)
    print(part2_result)
    assert(part2_result == 2817)
