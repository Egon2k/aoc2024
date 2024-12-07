import os
from itertools import product

operations = ['+','*']

def calculate_combinations(numbers, operators):
    num_operators = len(numbers) - 1  # Number of operators needed is one less than the number of numbers
    operator_combinations = list(product(operators, repeat=num_operators))  # All combinations of operators
    
    results = []
    for operator_set in operator_combinations:
        # Build the expression as a string
        expression = [int(numbers[0])]
        for num, op in zip(numbers[1:], operator_set):
            expression.append(op)
            expression.append(int(num))
        results.append(expression)
    return results

def part1(data):
    sum = 0
    for eq in data:
        formulas = calculate_combinations(eq[1], operations)
        for formula in formulas:
            res = 0
            next_op = "+"
            for element in formula:
                if element in operations:
                    next_op = element
                    continue
                if next_op == "+":
                    res += element
                if next_op == "*":
                    res *= element
            if int(eq[0]) == res:
                sum += int(eq[0])
                break
    return sum    

def part2(data):
    pass

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()
    data = [[x.split(":")[0], x.split(":")[1].split()] for x in data]
    
    print(part1(data))
    print(part2(data))