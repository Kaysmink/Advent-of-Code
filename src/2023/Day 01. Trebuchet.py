import regex as re

Input = open("data/2023/dag 01. input.txt", "r").read().split("\n")[0:-1]

numbers = [re.findall(r'\d', line) for line in Input]
part1 = sum([int(number[0] + number[-1]) for number in numbers])


numberdict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
              "seven": 7, "eight": 8, "nine": 9}

numbers = [re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine',
                      line, overlapped=True) for line in Input]
numbers = [[number if number.isnumeric() else str(numberdict[number])
            for number in line] for line in numbers]
part2 = sum([int(number[0] + number[-1]) for number in numbers])
