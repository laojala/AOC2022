import os


HEAD_MASK = {'R':(1,0), 'L':(-1,0), 'D':(0,-1), 'U':(0,1)}
DIFF_MASK = {2:-1, -2:1}


class Rope:
    def __init__(self, motions, length=1):
        self.motions = motions
        self.length = length
        self.head = (0,0)
        self.knots = self._create_knots(self.length)
        self.tail_visited = {(0,0)}  # set

    def run_instructions(self):
        for motion in self.motions:
            self._move(motion)

    def _create_knots(self, length):
        return dict.fromkeys(range(length), (0,0))

    def _move(self, instruction):
        # pylint: disable=consider-using-dict-items
        for index in range(int(instruction[1])):
            # new position for head:
            self.head = tuple(map(sum,zip(self.head, HEAD_MASK[instruction[0]])))

            # loop tail and set new positions:
            for key in self.knots:
                if key == 0:
                    previous = self.head
                else:
                    previous = self.knots[key-1]

                # loop knots and check if there is difference in between the previous
                diff = (previous[0]-self.knots[key][0], previous[1]-self.knots[key][1])

                mask0, mask1 = 0, 0
                if abs(diff[0]) > 1:
                    mask0 = DIFF_MASK[diff[0]]
                if abs(diff[1]) > 1:
                    mask1 = DIFF_MASK[diff[1]]

                if mask0 != 0 or mask1 != 0:
                    self.knots[key] = tuple(map(sum,zip(previous, (mask0, mask1))))
                else:
                    # rest of the nots do not move if previous knot does not move
                    break
            self.tail_visited.add(self.knots[self.length-1])

def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    #file_path = (os.path.dirname(__file__)) + "/" + 'larger_test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        all_lines = [d.rstrip() for d in file.readlines()]
    all_lines = [x.split(' ') for x in all_lines]
    return all_lines

def solve() -> None:
    motions = read_input()
    rope = Rope(motions)
    rope.run_instructions()
    part1 = len(rope.tail_visited)
    print(f'part1: {part1}')
    assert part1 in (13, 88, 5710)

    rope_part2 = Rope(motions, 9)
    rope_part2.run_instructions()
    part2 = len(rope_part2.tail_visited)
    print(f'part2: {part2}')
    assert part2 in (1, 36, 2259)

if __name__ == '__main__':
    solve()
