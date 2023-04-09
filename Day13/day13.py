import os
import json
from itertools import zip_longest

# compare function is copied from https://hamatti.org/adventofcode/2022/day_13/


def test_compare():
    assert compare(1, 2) == -1
    assert compare(1, [2]) == -1
    assert compare([1], 2) == -1
    assert compare([1,1,3,1,1], [1,1,5,1,1]) == -2
    assert compare([[1],[2,3,4]], [[1],4]) == -2
    assert compare([9], [[8,7,6]]) == 1
    assert compare([[4,4],4,4], [[4,4],4,4,4]) == -1
    assert compare([7,7,7,7], [7,7,7]) == 1
    assert compare([], [3]) == -1
    assert compare([[[[]]]], [[]]) == 1
    assert compare([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]) == 7


def read_input():
    '''Returns list that consists of lists of pairs as alist'''
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        lines = [d.strip() for d in file.readlines()]
    lines = [item for item in lines if item != '']
    table = [json.loads(item) for item in lines]
    return table


def compare(left, right) -> int:
    match (left, right):
        case int(left), int(right):
            return left - right
        case int(left), list(right):
            return compare([left], right)
        case list(left), int(right):
            return compare(left, [right])
        case None, right:
            return -1
        case left, None:
            return 1
        case list(left), list(right):
            for l, r in zip_longest(left, right, fillvalue=None):
                result = compare(l, r)
                if result != 0:
                    return result

    return 0
    

def solve_part1(data: list, ) -> None:

    pairs = []
    for i in range(0, len(data),2):
        pairs.append(data[i:i+2])

    right_order_indexes = []

    for index, pair in enumerate(pairs, 1):
        left = pair[0]
        right = pair[1]

        right_order_indexes.append(compare(left, right))
    

    sum = 0
    for index, right_order in enumerate(right_order_indexes, 1):
        if right_order < 0:
            sum += index
    print(f'part1: {sum}')

    assert sum in [13, 5529]


def solve_part2(data: list) -> None:
    # first, we add divider packets to the data
    data.append([[2]])
    data.append([[6]])
    # then we order the data
    ordered_packets = []

    for item in data:
        if not ordered_packets:
            ordered_packets.append(item)
        else:
            for index, ordered in enumerate(ordered_packets):
                if compare(item, ordered) < 0:
                    ordered_packets.insert(index, item)
                    break
                # else we add item to the end of the list
                if index == len(ordered_packets) - 1:
                    ordered_packets.append(item)
                    break
    
    # find list index for value [[2]]
    divider_index1 = ordered_packets.index([[2]]) + 1
    # find list index for value [[6]]
    divider_index2 = ordered_packets.index([[6]]) + 1

    part2 = divider_index1 * divider_index2

    print(f'part2: {part2}')

    assert part2 in [140, 27690]

def solve() -> None:
    data = read_input()

    solve_part1(data)
    solve_part2(data)

if __name__ == '__main__':
    test_compare()
    solve()
