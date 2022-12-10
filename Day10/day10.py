class Handheld:
    def __init__(self, program):
        self.cycles = [20,60,100,140,180,220] 
        self.signal_strength = dict.fromkeys(self.cycles, 0)
        self.register = 1   # sprite
        self.cycle = 0
        self.program = program
        # image related parameters
        self.image_row = ''
        self.image_row_max = 40
        self.image = []

    def _add_cycle(self):
        Handheld._draw_pixel(self)
        self.cycle += 1
        Handheld._store_signal_strength(self)

    def _store_signal_strength(self):
        if self.cycle in self.signal_strength:
            self.signal_strength[self.cycle] = self.register * self.cycle

    def _draw_pixel(self):
        if len(self.image_row) == self.image_row_max:
            self.image.append(self.image_row)
            self.image_row = ''
        # I could not add the last row otherwise
        if len(self.image) == 5 and len(self.image_row) == self.image_row_max-1:
            self.image.append(self.image_row)
            self.image_row = ''

        row_index = self.cycle % self.image_row_max
        sprite = [self.register-1, self.register, self.register+1]
        if row_index in sprite:
            self.image_row = self.image_row + '■'
            #self.image_row = self.image_row + '#'
        else:
            self.image_row = self.image_row + ' '
            #self.image_row = self.image_row + '.'

    def execute_program(self):
        for command in self.program:
            print(command)
            self._add_cycle()
            if command[0] == 'noop':
                continue
            # else command is addx
            self._add_cycle()
            self.register += int(command[1])

    def raster(self):
        print(len(self.image))
        for line in self.image:
            print(line)

import os

def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        all_lines = [d.rstrip() for d in file.readlines()]
    return [x.split(' ') for x in all_lines]

def solve() -> None:
    program = read_input()

    # part 1
    handheld = Handheld(program)
    handheld.execute_program()
    part1 = sum(handheld.signal_strength.values())
    print(part1)
    assert part1 in (13140, 17180)

    # part 2 is REHPRLUB
    handheld.raster()

if __name__ == '__main__':
    solve()
