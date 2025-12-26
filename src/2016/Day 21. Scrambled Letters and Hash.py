from itertools import permutations
from collections import deque

instructions = open("data/2016/dag 21. input.txt", "r").read().split("\n")[0:-1]

def scramble_password(password):
    for instruction in instructions:
        instruction = instruction.split(" ")
        if instruction[0] == "swap":
            if instruction[1] == "position":
                i1, i2 = int(instruction[2]), int(instruction[5])
                password = list(password)
                password[i1], password[i2] = password[i2], password[i1]
                password = "".join(password)
            if instruction[1] == "letter":
                c1, c2 = instruction[2], instruction[5]
                password = password.replace(c1, '#').replace(c2, c1).replace('#', c2)
        if instruction[0] == "rotate":
            password = deque(password)
            if instruction[1] == "left":
                n = int(instruction[2])
                password.rotate(-n)
            if instruction[1] == "right":
                n = int(instruction[2])
                password.rotate(n)
            if instruction[1] == "based":
                index = password.index(instruction[6])
                n = index+1 if index < 4 else index+2
                password.rotate(n)
            password = "".join(password)
        if instruction[0] == "reverse":
            i1, i2 = int(instruction[2]), int(instruction[4])
            password = password[:i1] + password[i1:i2+1][::-1] + password[i2+1:]
        if instruction[0] == "move":
            i1, i2 = int(instruction[2]), int(instruction[5])
            password = list(password)
            char = password.pop(i1)
            password.insert(i2, char)
            password = "".join(password)

    return password

part1 = scramble_password("abcdefgh")
part2 = ["".join(perm) for perm in permutations("abcdefgh") if scramble_password("".join(perm)) == "fbgdceah"][0]

print(part1, part2)