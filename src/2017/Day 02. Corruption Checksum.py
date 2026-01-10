import re

Input = open("data/2017/dag 02. input.txt", "r").read().split("\n")[0:-1]
numbers = [sorted(list(map(int,re.findall(r"\d+", line)))) for line in Input]

def get_result(numbers):
    return numbers[-1] - numbers[0], [int(n1/n2) for n1 in numbers for n2 in numbers if n1%n2 == 0 and n1 != n2][0]

results = [get_result(number) for number in numbers]
part1 = sum([p1 for p1,p2 in results])
part2 = sum([p2 for p1,p2 in results])

print(part1, part2)