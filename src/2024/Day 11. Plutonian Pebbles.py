import re
from collections import defaultdict

Input = open("data/2024/dag 11. input.txt", "r").read().split("\n")[0]

numbers = list(map(int, re.findall(r'\d+', Input)))
numbersDict = {key: 1 for key in numbers}


def new_num(number):
    if number == 0:
        return [1]
    if len(str(number)) % 2 == 0:
        number = str(number)
        return [int(number[0:len(number) // 2]), int(number[len(number) // 2::])]
    return [number * 2024]


def blink(numbersDict):
    new_numbersDict = defaultdict(int)
    for number, num in numbersDict.items():
        for value in new_num(number):
            new_numbersDict[value] = new_numbersDict[value] + num
    return new_numbersDict


for blinkNum in range(75):
    if blinkNum == 25:
        part1 = sum(numbersDict.values())
    numbersDict = blink(numbersDict)

print(part1, sum(numbersDict.values()))
