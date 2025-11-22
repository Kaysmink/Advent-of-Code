import re

Input = open("data/2016/dag 09. input.txt", "r").read().strip()

def decompress(part, string):
    if "(" not in string:
        return len(string)

    index = result = 0
    while index < len(string):
        next_char = string[index]
        if next_char == "(":
            n1, n2 = list(map(int,re.findall(r"\d+", string[index::])[0:2]))
            start_index_doubling = index + string[index::].index(")")+1
            doubling_string = string[start_index_doubling:start_index_doubling+n1]
            if part == 1:
                result = result + len(doubling_string) * n2
            if part ==2:
                result = result + decompress(2, doubling_string) * n2
            index = start_index_doubling + n1
        else:
            result = result + 1
            index = index + 1

    return result

part1 = decompress(1, Input)
part2 = decompress(2, Input)

print(part1, part2)