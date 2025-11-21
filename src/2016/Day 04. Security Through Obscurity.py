import re
from collections import Counter

Input = open("data/2016/dag 04. input.txt", "r").read().split("\n")[0:-1]
rooms = [re.findall(r"[a-z]+|\d+", line) for line in Input]

def check_room(room):
    name = "".join(room[0:-2])
    counts = Counter(name)
    top_5 = "".join([char for char, freq in sorted(counts.items(), key=lambda x: (-x[1], x[0]))][0:5])

    return room[-2], top_5 == room[-1]


def decrypt_room(room):
    name = "".join(room[0:-2])
    ID = int(room[-2])
    result = "".join([chr((ord(char)-96+(ID%26))%26+96) if (ord(char)-96+(ID%26))%26 != 0 else "z" for char in name])

    return ID, result


is_real = [check_room(room) for room in rooms]
part1 = sum([int(ID) for ID, real in is_real if real])

decrypted = [decrypt_room(room) for room in rooms]
part2 = [ID for ID, decr in decrypted if "pole" in decr][0]

print(part1, part2)