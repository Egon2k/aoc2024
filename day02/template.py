import os

def check_safe(numbers):
    if sorted(numbers) == numbers: # increasing
        for i in range(len(numbers) - 1):
            if numbers[i + 1] == numbers[i] or numbers[i + 1] > numbers[i] + 3:
                return False
    elif sorted(numbers, reverse=True) == numbers: # decreasing    
        for i in range(len(numbers) - 1):
            if numbers[i + 1] == numbers[i] or numbers[i + 1] < numbers[i] - 3:
                return False
    else:
        return False
        
    return True

def part1(data):
    safe_reports = 0
    for line in data:
        numbers = [int(n) for n in line.split()]
        
        if check_safe(numbers):
            safe_reports += 1
    return safe_reports

def part2(data):
    safe_reports = 0
    for line in data:
        numbers = [int(n) for n in line.split()]
        
        for i in range(len(numbers)):
            temp_numbers = numbers[:]
            temp_numbers.pop(i) # remove i-th element from list
            if check_safe(temp_numbers):
                safe_reports += 1
                break
    return safe_reports

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))