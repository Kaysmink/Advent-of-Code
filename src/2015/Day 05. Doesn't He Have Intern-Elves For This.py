import re

Input = open("data/2015/dag 05. input.txt", "r").read().split("\n")[0:-1]

vowels = ['a', 'e', 'i', 'o', 'u']
forbidden = ["ab", "cd", "pq", "xy"]


def check_nice(part, string):
    num_vowels = sum([string.count(vowel) for vowel in vowels]) >=3
    is_forbidden = all([comb not in string for comb in forbidden])
    double = re.search(r"(.)\1", string)
    repeat = re.search(r'([a-zA-Z]{2}).*?\1', string)
    twice = re.search(r'([a-zA-Z]).\1', string)

    if part == 1:
        if all([num_vowels, is_forbidden, double]):
            return True

        return False

    if part == 2:
        if all([repeat, twice]):
            return True

        return False


part1 = sum([check_nice(1, string) for string in Input])
part2 = sum([check_nice(2, string) for string in Input])

print(part1, part2)
