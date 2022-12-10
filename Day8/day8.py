import os
from functools import reduce

def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        all_lines = [[int(num) for num in line.strip()] for line in file.readlines()]
    return all_lines

def solve() -> None:
    forest = read_input()
    transposed = list(map(list, zip(*forest)))
    part1 = 0
    scenic_scores = []
    last_row = len(forest)-1
    last_in_row = len(forest[0])-1

    for line_index, line in enumerate(forest):
        if line_index in [0, last_row]:
            part1 += len(line)
            continue
        for index, tree in enumerate(line):
            if index in [0,last_in_row]:
                part1 += 1
                continue

            # make lists for different projections
            p1 = forest[line_index][index+1:]
            p2 = forest[line_index][:index]
            p3 = transposed[index][:line_index]
            p4 = transposed[index][line_index+1:]

            # reverse projections for part2
            p2.reverse()
            p3.reverse()

            # part 1
            for view in [p1, p2, p3, p4]:
                if tree > max(view):
                    part1 += 1
                    break

            # part2
            scores = [0,0,0,0]
            for proj_index, projection in enumerate([p1,p2,p3,p4]):
                for neighbour in projection:
                    scores[proj_index] += 1
                    if tree <= neighbour:
                        break

            score = reduce((lambda x, y: x * y), scores)
            scenic_scores.append(score)

    print(f'part1: {part1}')
    assert part1 in (1679, 21)

    part2 = max(scenic_scores)
    print(f'part2: {part2}')
    assert part2 in (8, 536625)


if __name__ == '__main__':
    solve()
