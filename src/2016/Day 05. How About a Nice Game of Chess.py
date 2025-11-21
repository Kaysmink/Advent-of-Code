import hashlib

# very similar to 2015 day 4
Input = open("data/2016/dag 05. input.txt", "r").read().strip()

def find_password(part, string, leading, size):
    password = "" if part == 1 else [""]*size
    num = 0
    while True:
        res = hashlib.md5(f"{string}{num}".encode()).hexdigest()
        if res.startswith(leading):
            if part ==1:
                password = password + res[5]
            else:
                if res[5].isdigit() and int(res[5]) <size and password[int(res[5])] == "":
                    password[int(res[5])] = res[6]
        num = num + 1

        if (part == 1 and len(password) == size) or (part == 2 and len("".join(password)) == size):
            break

    return password if part == 1 else "".join(password)

part1 = find_password(1, Input,"00000", 8)
part2 = find_password(2, Input,"00000", 8)

print(part1, part2)