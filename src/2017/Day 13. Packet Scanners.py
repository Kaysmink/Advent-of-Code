import re

Input = open("data/2017/dag 13. input.txt", "r").read().split("\n")[0:-1]
scanners = [list(map(int,re.findall(r"\d+", line))) for line in Input]
scanners_dict = {d:r for d,r in scanners}

def check_depth(scanner, delay):
    cycle_num = scanners_dict[scanner] + scanners_dict[scanner] - 2

    if (scanner+delay)%cycle_num == 0:
        return True, scanner * scanners_dict[scanner]

    return False, 0

def breach_firewall():
    delay = 0
    while True:
        scanner_check = [check_depth(scanner, delay) for scanner in scanners_dict.keys()]
        caught = sum([scanner[0] for scanner in scanner_check])

        if delay == 0:
            part1 = sum([scanner[1] for scanner in scanner_check])
        if caught == 0:
            break

        delay = delay+1

    return part1, delay

part1, part2 = breach_firewall()

print(part1, part2)