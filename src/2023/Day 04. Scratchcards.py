import regex as re

Input = open("data/2023/dag 04. input.txt", "r").read().split("\n")[0:-1]
cards = [re.findall(r'\d+', line)[1:] for line in Input]
cards = [[line[0:10], line[10::]] for line in cards]


# Part1
winning = [[number for number in hand if number in winning] for winning, hand in cards]
part1 = sum([2**(len(numbers)-1) for numbers in winning if len(numbers) > 0])

# Part 2
winning_cards = [len(numbers) for numbers in winning]
instances = [1 for x in range(0, len(Input))]

for index, num_winning in enumerate(winning_cards):
    for x in range(index+1, index+num_winning+1):
        if x < len(instances):
            instances[x] = instances[x] + instances[index]

print(part1, sum(instances))
