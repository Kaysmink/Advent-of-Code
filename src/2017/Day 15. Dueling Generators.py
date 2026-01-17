import re

a, b = list(map(int, re.findall(r"\d+", open("data/2017/dag 15. input.txt", "r").read().strip())))
multi_a, multi_b = [16807, 48271]

def check_numbers(a, b):
    return str(bin(a))[-16:] == str(bin(b))[-16:]

def get_generators(gen, number, multiplier, part):
    size = 40000000 if part == 1 else 5000000

    numbers = []
    while len(numbers) < size:
        number = (number*multiplier)%2147483647

        if part == 2:
            if (gen == "a" and number % 4 == 0) or (gen == "b" and number%8 == 0):
                numbers.append(number)
        else:
            numbers.append(number)

    return numbers


generator_a = get_generators("a", a, multi_a, 1)
generator_b = get_generators("b", b, multi_b, 1)
part1 = sum([check_numbers(a, b) for a, b in zip(generator_a, generator_b)])

generator_a = get_generators("a", a, multi_a, 2)
generator_b = get_generators("b", b, multi_b, 2)
part2 = sum([check_numbers(a, b) for a, b in zip(generator_a, generator_b)])

print(part1, part2)