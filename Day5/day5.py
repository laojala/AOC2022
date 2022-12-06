'''
Solutions for https://adventofcode.com/2022/day/4

'''

import os
import re


def read_instructions():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test_instructions.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input_instructions.txt'
    with open(file_path, 'r') as f:
        all_lines = [re.findall('\d+', line) for line in f.readlines()]
    all_lines = [[int(i) for i in list] for list in all_lines]
    return all_lines

def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test_crates.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input_crates.txt'
    with open(file_path, 'r') as f:
        all_lines = [d for d in f.readlines()]
    
    number_of_stacks = int(len(all_lines[0])/4 + 1)

    #create stack and remove last line (number indexes) from the input
    stacks = {new_list:[] for new_list in range(1, number_of_stacks)}
    all_lines.pop()
    
    # go throuhg the list in chunks of 4 and add add stacks
    all_lines.reverse()
    
    for line in all_lines:
        for i in range(0, len(line), 4):
            chunk = line[i:i+4]
            chunk = chunk.strip()
            chunk = chunk.replace('[', '').replace(']', '').replace(' ', '')
            crate = int(i/4)+1
            if chunk != '':
                stacks[crate] += chunk
    return stacks

def get_top_row(stacks):
    row = ''
    for key in stacks:
        row += stacks[key][-1]
    return row

def count_part1(stacks, instructions):
    for line in instructions:
        for move in range(line[0]):
            item = stacks[line[1]].pop()
            stacks[line[2]] += item
    
    result = get_top_row(stacks)

    return result

def count_part2(stacks, instructions):
    for line in instructions:
        count, where, to = line[0], line[1], line[2]
        items_to_move = stacks[where][-count:]
        del stacks[where][-count:]
        stacks[to] += items_to_move
    result = get_top_row(stacks)

    return result


if __name__ == '__main__':
    stacks = read_input()
    instructions = read_instructions()
    
    part1_result = count_part1(stacks, instructions)
    print(part1_result)
    assert(part1_result == 'CNSZFDVLJ' or part1_result == 'CMZ')

    stacks2 = read_input()
    part2_result = count_part2(stacks2, instructions)
    print(part2_result)
    assert(part2_result == 'QNDWLMGNS' or part2_result == 'MCD')

