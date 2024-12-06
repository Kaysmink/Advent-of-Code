from collections import defaultdict

rules, updates = open("data/2024/dag 05. input.txt", "r").read().split("\n\n")

rules = [list(map(int, rule.split("|"))) for rule in rules.split("\n")]
updates = [list(map(int, update.split(","))) for update in updates.split("\n")[0:-1]]

ruleBefore = defaultdict(list)
ruleAfter = defaultdict(list)

for key, value in rules:
    ruleBefore[key].append(value)
    ruleAfter[value].append(key)


def check_update(update):
    for index, value in enumerate(update):
        before = update[0:index]
        after = update[index + 1::]

        correct_before = 1 if index == 0 else min([valueB in ruleAfter[value] for valueB in before])
        correct_after = 1 if index == len(update) - 1 else min([valueA in ruleBefore[value] for valueA in after])

        if correct_after + correct_before != 2:
            return False
    return update


def correct_update(update):
    while True:
        for index in range(len(update) - 1):
            first, second = update[index:index + 2]

            if second not in ruleBefore[first]:
                update[index], update[index + 1] = update[index + 1], update[index]

            if check_update(update):
                return update
    return False


# Part 1
correct = [check_update(update) for update in updates]
part1 = sum([update[len(update) // 2] for update in correct if update != False])

# Part 2
wrong = [updates[index] for index, value in enumerate(correct) if value == False]
corrected = [correct_update(update) for update in wrong]
part2 = sum([update[len(update) // 2] for update in corrected])

print(part1, part2)
