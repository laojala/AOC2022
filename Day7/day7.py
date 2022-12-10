'''
Solutions for https://adventofcode.com/2022/day/7

Algorithm is very heavily inspired by
https://github.com/savbell/2022-Advent-of-Code/blob/master/day-07.py

'''

import os

def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        all_lines = [d.rstrip() for d in file.readlines()]
    all_lines = [x.split(' ') for x in all_lines]
    return all_lines

def handle_filesystem(commands):
    dirs = {}
    path = []

    for line in commands:
        if line[0] == '$' and line[1] == 'cd':
            if line[2] == '/':
                path = ['/']
                dirs['/'] = 0
            elif line[2] == '..':
                path.pop()
            else:
                new_path = '/'.join(path) + '/' + line[2]
                path.append(new_path)
                if not dirs.get(new_path):
                    dirs[new_path] = 0
        elif line[0].isdigit():
            for item in path:
                dirs[item] += int(line[0])

    # part 1
    part1_files = [value for value in dirs.values() if value <= 100000]
    part1 = sum(part1_files)

    #part 2 30000000
    unused_space = 70000000 - dirs['/']
    space_needed = 30000000 - unused_space

    part2_files =  [value for value in dirs.values() if value >= space_needed]
    part2 = min(part2_files)

    return part1, part2

def solve() -> None:
    data = read_input()

    part1, part2 = handle_filesystem(data)
    print(part1)
    assert part1 == 95437 or part1 == 1513699
    print(part2)
    assert part2 == 24933642 or part2 == 7991939

if __name__ == '__main__':
    solve()
