import hashlib
import re

from tqdm import tqdm

Input = open("data/2016/dag 14. input.txt", "r").read().strip()

def key_stretch(part, num):
    string = hashlib.md5(f"{Input}{num}".encode()).hexdigest()
    if part == 1:
        return string

    for i in range(2016):
        string = hashlib.md5(string.encode()).hexdigest().lower()
    return string

def find_value(part, key_num):
    keys = []
    num = 0

    while True:
        res = hashes[num] if part == 1 else stretched_hashes[num]
        triple_match = re.findall(r"(.)\1\1", res)

        if triple_match:
            char = triple_match[0]
            for num2 in range(num+1, num+1001):
                res2 = hashes[num2] if part == 1 else stretched_hashes[num2]
                if char*5 in res2:
                    keys.append(num)
                    if len(keys) == key_num:
                        return num
                    continue

        num = num + 1

hashes = [key_stretch(1,num) for num in tqdm(range(25000))]
stretched_hashes = [key_stretch(2,num) for num in tqdm(range(25000))]

part1 = find_value(1, 64)
part2 = find_value(2, 64)

print(part1, part2)