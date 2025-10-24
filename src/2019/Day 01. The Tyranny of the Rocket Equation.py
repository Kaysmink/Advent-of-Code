Input = open("data/2019/dag 01. input.txt", "r").read().split("\n")[0:-1]
Input = list(map(int, Input))

def get_fuel(value):
    if value <=6:
        return value

    return value + get_fuel(value//3-2)


part1 = sum([value//3-2 for value in Input])
part2 = sum([get_fuel(value) - value for value in Input])

print(part1, part2)
