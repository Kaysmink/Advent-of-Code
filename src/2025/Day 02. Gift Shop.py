import re

Input = open("data/2025/dag 02. input.txt", "r").read().split(",")[0:-1]
ranges = [list(map(int,re.findall(r"\d+", line))) for line in Input]

def check_invalid_numbers_in_range(n1,n2):
    return [[number for number in range(n1,n2+1) if str(number)[0:len(str(number))//2] == str(number)[len(str(number))//2::]],
            [number for number in range(n1, n2 + 1) if re.match(r"^(.+?)\1+$", str(number))]]


invalid_numbers = [check_invalid_numbers_in_range(n1,n2) for n1,n2 in ranges]
part1, part2 = [sum([sum(values[i]) for values in invalid_numbers]) for i in range(2)]

print(part1, part2)
