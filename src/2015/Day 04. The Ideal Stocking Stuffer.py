import hashlib

Input = "bgvyzdsv"

def find_value(leading):
    num = 0
    while True:
        res = hashlib.md5(f"{Input}{num}".encode()).hexdigest()
        if res.startswith(leading):
            break
        num = num + 1
    return num

part1 = find_value("00000")
part2 = find_value("000000")

print(part1, part2)