'''
Solutions for https://adventofcode.com/2022/day/2

'''

import os

def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        all_lines = [d.rstrip() for d in file.readlines()]
    strategy = []
    for game in all_lines:
        strategy.append([game[0], game[2]])
    return strategy

# outcomes
LOST = [['A', 'Z'], ['B', 'X'], ['C', 'Y']]
DRAWN = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
WIN = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]

# rock    paper   scissors
# A       B       C
# X       Y       Z

def add_shape_value(shape: str) -> int:
    if shape == 'X':
        return 1
    if shape == 'Y':
        return 2
    return 3

def get_part2_shape(table, opponents_value) -> str:
    for item in table:
        if item[0] == opponents_value:
            return item[1]

def count_part1(strategy: list) -> int:
    score = 0
    for game in strategy:
        shape_value = add_shape_value(game[1])
        if game in LOST:
            score += shape_value
        if game in WIN:
            score += 6 + shape_value
        if game in DRAWN:
            score += 3 + shape_value
    return score

def count_part2(strategy: list) -> int:
    score = 0
    for game in strategy:
        opponent = game[0]
        result = game[1]
        if result == 'Y': # draw
            own_shape = get_part2_shape(DRAWN, opponent)
            score += 3 + add_shape_value(own_shape)

        if result == 'X': # lost
            own_shape = get_part2_shape(LOST, opponent)
            score += add_shape_value(own_shape)

        if result == 'Z': # won
            own_shape = get_part2_shape(WIN, opponent)
            score += 6 + add_shape_value(own_shape)
    return score

if __name__ == '__main__':
    data = read_input()

    part1_result = count_part1(data)
    print(part1_result)
    assert part1_result == 12586

    part2_result = count_part2(data)
    print(part2_result)
    assert part2_result == 13193
