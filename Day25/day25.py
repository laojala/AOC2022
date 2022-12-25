import os

class Decimal:

    def __init__(self, decimal):
        self.snafu = self.get_snafu(decimal)

    @staticmethod
    def get_snafu(decimal:int) -> str:
        ''' int -> snafu conversion copied from this solution:
            https://github.com/radosz99/aocd/blob/main/solutions/25.py '''

        snafu = ""
        rest = 0

        while decimal !=0 or rest:
            remainder = decimal % 5 + rest
            rest = 0
            if remainder > 2:
                rest = 1
            snafu = {0: "0", 1: "1", 2: "2", 3: "=", 4: "-", 5: "0"}[remainder] + snafu
            decimal //= 5
        return snafu


class Snafu:

    def __init__(self, snafu):
        self.decimal = self.get_decimal(snafu)

    @staticmethod
    def get_decimal(code:str) -> int:
        code = code[::-1]
        counter = 0
        for index in range(len(code)-1, -1, -1):
            element = code[index]
            match element:
                case '1':
                    counter += 5 ** index
                case '2':
                    counter += 2 * (5 ** index)
                case '-':
                    counter -= 5 ** index
                case '=':
                    counter -= 2 * (5 ** index)
        return counter


def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        return [d.rstrip() for d in file.readlines()]

def solve() -> None:
    program = read_input()
    decimals = map(Snafu.get_decimal, program)
    decimal = sum(list(decimals))
    solution = Decimal.get_snafu(decimal)
    print(f'Day25: {solution}')
    assert solution in ('2=-1=0', '2=1-=02-21===-21=200')


if __name__ == '__main__':
    solve()
