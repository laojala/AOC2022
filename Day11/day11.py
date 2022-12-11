import os
from math import lcm, floor


class Monkey:
    def __init__(self, items:list, operation, test, test_number, test_true, test_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.test_number = test_number
        self.test_true = test_true
        self.test_false = test_false
        self.inspections = 0

    def __str__(self):
        return f'{self.items}, {self.inspections}'

class Barrel:  # group of monkeys is called barrel or troop
    def __init__(self, chill=False):
        self.barrel = []
        self.modulo_divider = 1
        self.chill = chill

    def add_monkey(self, monkey:Monkey):
        self.barrel.append(monkey)
        # modulo_divider is is the least common multiple. Explained here:
        # https://github.com/Hamatti/adventofcode-2022/blob/main/src/day_11.ipynb
        tests = [monkey.test_number for monkey in self.barrel]
        least_common_multiple = lcm(*tests)
        self.modulo_divider = least_common_multiple

    def round(self):
        for monkey in self.barrel:
            for item in monkey.items:
                monkey.inspections += 1
                if self.chill:
                    worry_level = monkey.operation(item) % self.modulo_divider
                else:
                    worry_level = floor(monkey.operation(item) / 3)
                if monkey.test(worry_level):
                    self.barrel[monkey.test_true].items.append(worry_level)
                else:
                    self.barrel[monkey.test_false].items.append(worry_level)
            monkey.items = []

    def monkey_business(self):
        all = [monkey.inspections for monkey in self.barrel]
        all.sort()
        return all[-1]*all[-2]

    def __str__(self):
        return "\n".join(map(str,self.barrel))

def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        lines = [d.rstrip() for d in file.readlines()]
    lines = [x.replace(',', '').split(' ') for x in lines]
    return lines


def create_monkeys(input: list, chill: bool = False) -> Barrel:

    # functions for operations
    def multiply_input(number):
        return lambda x : x * number

    def add_input(number):
        return lambda x : x + number
    
    def create_test(number):
        return lambda x : x % number == 0

    barrel = Barrel(chill)
    # monkey consist of 7 lines. Loop input in chunks of 7 and create monkey:
    for iteration in range(0, len(input), 7):
        items = []
        operation = None
        test = None
        test_true = None
        test_false = None

        for index in range(7):
            i = iteration + index
            if index == 1:
                for x in input[i]:
                    if x.isdigit():
                        items.append(int(x))
            if index == 2:
                if input[i][6] == '*':
                    if input[i][7] == 'old':
                        operation = lambda x : x * x
                    else:
                        operation = multiply_input(int(input[i][7]))
                if input[i][6] == '+':
                    operation = add_input(int(input[i][7]))
            if index == 3:
                test = create_test(int(input[i][5]))
                test_number = int(input[i][5])
            if index == 4:
                test_true = int(input[i][-1])
            if index == 5:
                test_false = int(input[i][-1])
        barrel.add_monkey(Monkey(items, operation, test, test_number, test_true, test_false))

    return barrel

def solve() -> None:
    notes = read_input()

    barrel_part1 = create_monkeys(notes)
    for i in range(20):
        barrel_part1.round()
    part1 = barrel_part1.monkey_business()
    print(f'part1: {part1}')
    assert part1 in (10605,112815)

    barrel_part2 = create_monkeys(notes, chill=True)
    for i in range(10000):
        barrel_part2.round()
    part2 = barrel_part2.monkey_business()
    print(f'part2: {part2}')
    assert part2 in (2713310158, 25738411485)

if __name__ == '__main__':
    solve()
