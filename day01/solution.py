import os

def part1(l1,l2):
    sum = 0
    for n, _ in enumerate(sorted(l1)):
        sum += abs(sorted(l1)[n] - sorted(l2)[n])
    return sum

def part2(l1,l2):
    sum = 0
    for i in l1:
        sum += i * l2.count(i)
    return sum

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()

    l1 = []
    l2 = []        
    for d in data:
        l1.append(int(d.split()[0]))
        l2.append(int(d.split()[1]))

    print(part1(l1,l2))
    print(part2(l1,l2))