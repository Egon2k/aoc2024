import os
from collections import Counter

def check_rule(update, rule):
    return update.index(rule[0]) > update.index(rule[1])

def check_rules(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if check_rule(update, rule):
                return False
    return True

def get_middle_page(update):
    return update[len(update) // 2]

def make_update_from_rules(update, rules):
    fixed_update = []
    relevant_rules = []

    for rule in rules:
        if rule[0] in update and rule[1] in update:
            relevant_rules.append(rule)
    
    # reverse sort the relevant rules by the number of occurances of the first element
    # the rule with highest number of occurance in position 0 is the first page in the
    # update (and so on, with decending number of occurances)
    frequency = Counter(x[0] for x in relevant_rules) # stackoverflow
    sorted_rules = sorted(relevant_rules, key=lambda x: frequency[x[0]], reverse=True)
    
    for rule in sorted_rules:
        if rule[0] not in fixed_update:
            fixed_update.append(rule[0])
            # we actually do not append the last page to the page but it doesnt matter
            # for finding the middle page later
    return fixed_update

def part1(rules, updates):
    sum = 0
    for update in updates:
        if check_rules(update, rules):
            sum += get_middle_page(update)
    return sum

def part2(rules, updates):
    sum = 0
    count_incorrect_updates = 0 # debug
    count_incorrect_fixes = 0 # debug
    for update in updates:
        if not check_rules(update, rules):
            count_incorrect_updates += 1 # debug
            fixed = make_update_from_rules(update, rules)
            if not check_rules(fixed, rules): # debug
                count_incorrect_fixes += 1 # debug
            sum += get_middle_page(fixed)

    print(f'{count_incorrect_updates = }') # debug
    print(f'{count_incorrect_fixes = }') # debug
    return sum

if __name__ == "__main__":
    rules = []
    updates = []
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()

    for line in data:
        if "|" in line:
            rules.append([int(x) for x in line.split("|")])
        elif "," in line:
            updates.append([int(x) for x in line.split(",")])

    print(part1(rules, updates))
    print(part2(rules, updates))