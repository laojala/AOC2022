import os

HEAD_MASK = {'R':(1,0), 'L':(-1,0), 'D':(0,-1), 'U':(0,1)}
TAIL_MASK = {'R':(-1,0), 'L':(1,0), 'D':(0,1), 'U':(0,-1)}

class Rope:
    def __init__(self):
        self.head = (0,0)
        self.tail = (0,0)
        self.tail_visited = {(0,0)}  # set

    def move(self, instruction):
        for i in range(int(instruction[1])):
            #print(f'begin round {i} - H:{self.head}, T:{self.tail}')
            self.head = tuple(map(sum,zip(self.head, HEAD_MASK[instruction[0]])))
            #count difference
            difference = (abs(self.head[0]-self.tail[0]), abs(self.head[1]-self.tail[1]))
            #print(f'diff: {difference}')
            if not (difference[0] <= 1 and difference[1] <= 1):
                self.tail = tuple(map(sum,zip(self.head, TAIL_MASK[instruction[0]])))
            self.tail_visited.add(self.tail)
            #print(f'end round {i} - H:{self.head}, T:{self.tail}')

    @staticmethod
    def is_adjanced(x, y):
        return abs(x[0] - y[0]) <= 1 and abs(x[1] - y[1]) <= 1

def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        all_lines = [d.rstrip() for d in file.readlines()]
    all_lines = [x.split(' ') for x in all_lines]
    return all_lines

def solve() -> None:
    motions = read_input()
    rope = Rope()
    for motion in motions:
        #print(f'instruction: {motion}')
        rope.move(motion)
    part1 = len(rope.tail_visited)
    print(part1)
    assert part1 in (13, 5710)

if __name__ == '__main__':
    solve()
