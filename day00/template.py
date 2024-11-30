import os

def part1(data):
    pass

def part2(data):
    pass

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))