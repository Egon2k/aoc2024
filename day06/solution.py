import os

UP    = (-1, 0)
RIGHT = ( 0, 1)
DOWN  = ( 1, 0)
LEFT  = ( 0,-1)

dirs = [UP, RIGHT, DOWN, LEFT]

def find_char_in_grid(char, grid):
    findings = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == char:
                findings.append((row,col))
    return findings

def count_char_in_grid(char, grid):
    sum = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == char:
                sum += 1
    return sum

def part1(grid):
    pos = find_char_in_grid("^", grid)[0]
    dir_idx = 0
    obst = find_char_in_grid("#", grid)
    dist_pos = grid[:] # to keep track of distinct positions

    while pos[0] != 0 and pos[0] != len(grid) and \
          pos[1] != 0 and pos[1] != len(grid[0]):
        
        # go one step in current direction
        new_pos = tuple(sum(z) for z in zip(pos, dirs[dir_idx]))

        if new_pos in obst:
            dir_idx = (dir_idx + 1) % len(dirs) # make a right turn
        else:
            dist_pos[pos[0]][pos[1]] = "X"
            pos = new_pos

    return count_char_in_grid("X", grid)

def part2(grid):
    pass

if __name__ == "__main__":
    grid = []
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        row = f.read().splitlines()
        for r in row:
            grid.append(list(r))

    print(part1(grid))
    print(part2(grid))