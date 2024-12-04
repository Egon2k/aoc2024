import os
from sys import exception

NORTH      = (-1,  0)
SOUTH      = ( 1,  0)
WEST       = ( 0, -1)
EAST       = ( 0,  1)
NORTH_WEST = (-1, -1)
NORTH_EAST = (-1,  1)
SOUTH_WEST = ( 1, -1)
SOUTH_EAST = ( 1,  1)

dirs = [NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST]


def add_tuple(a, b, len):
    out = [sum(z) for z in zip(a, b)]
    if out[0] < 0 or out[0] > len or out[1] < 0 or out[1] > len:
        raise exception
    else:
        return out

def check_xmas(data, start, dir):
    pos = start
    try:
        pos = add_tuple(pos, dir, len(data))
        if data[pos[0]][pos[1]] == "M":
            pos = add_tuple(pos, dir, len(data))
            if data[pos[0]][pos[1]] == "A":
                pos = add_tuple(pos, dir, len(data))
                if data[pos[0]][pos[1]] == "S":
                    return True
    except:
        return False
    return False

def check_x_mas(data, start):
    if start[0] > 0 and start[0] < len(data)-1 and start[1] > 0 and start[1] < len(data)-1:
        positions = [
                    add_tuple(start, NORTH_WEST, len(data)),
                    add_tuple(start, NORTH_EAST, len(data)),
                    add_tuple(start, SOUTH_WEST, len(data)),
                    add_tuple(start, SOUTH_EAST, len(data)),
                    ]
        if  data[positions[0][0]][positions[0][1]] == "M" and \
            data[positions[1][0]][positions[1][1]] == "M" and \
            data[positions[2][0]][positions[2][1]] == "S" and \
            data[positions[3][0]][positions[3][1]] == "S":
            return True
        elif data[positions[0][0]][positions[0][1]] == "M" and \
             data[positions[1][0]][positions[1][1]] == "S" and \
             data[positions[2][0]][positions[2][1]] == "M" and \
             data[positions[3][0]][positions[3][1]] == "S":
            return True
        elif data[positions[0][0]][positions[0][1]] == "S" and \
             data[positions[1][0]][positions[1][1]] == "M" and \
             data[positions[2][0]][positions[2][1]] == "S" and \
             data[positions[3][0]][positions[3][1]] == "M":
            return True
        elif data[positions[0][0]][positions[0][1]] == "S" and \
             data[positions[1][0]][positions[1][1]] == "S" and \
             data[positions[2][0]][positions[2][1]] == "M" and \
             data[positions[3][0]][positions[3][1]] == "M":
            return True
        else:
            return False
    else:
        return False
    
def part1(data):
    sum = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == 'X':
                for dir in dirs:
                    if check_xmas(data, (row, col), dir):
                        sum += 1
    return sum


def part2(data):
    sum = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == 'A':
                if check_x_mas(data, (row, col)):
                    sum += 1
    return sum

if __name__ == "__main__":
    data = []
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        row = f.read().splitlines()
        for r in row:
            data.append(list(r))

    check_x_mas(data, (3, 4))
    print(part1(data))
    print(part2(data))