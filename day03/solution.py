import os
import re

def part1(data):
    sum = 0
    results = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    for result in results:
        sum += int(result[0]) * int(result[1])
    return sum

def part2(data):
    cmds = []
    results = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", data)
    for result in results:
        for r in result:
            if r != '': # remove all empty strings and append them to cmds list
                cmds.append(r)

    sum = 0
    i = 0
    dont_flag = False
    while i < len(cmds):
        if cmds[i] == "don't()":
            dont_flag = True
        elif cmds[i] == "do()":
            dont_flag = False
        elif cmds[i].isnumeric():
            if dont_flag == False:
                sum += int(cmds[i]) * int(cmds[i + 1])
                i += 1 # additional increase of i to skip both numbers
        i += 1
        
    return sum

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().replace("\r\n", "")

    print(part1(data))
    print(part2(data))