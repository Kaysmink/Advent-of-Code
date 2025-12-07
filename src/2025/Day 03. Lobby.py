Input = open("data/2025/dag 03. input.txt", "r").read().split("\n")[0:-1]
batteries = [list(map(int,line)) for line in Input]

def find_batteries(battery, b_num, max_num):
    if b_num == max_num:
        return str(max(battery))

    new_b = max(battery[0:(b_num-max_num)])
    remainder = battery[battery[0:(b_num-max_num)].index(new_b)+1::]

    return str(new_b) + find_batteries(remainder, b_num+1, max_num)


part1, part2 = [sum([int(find_batteries(battery,1,lb)) for battery in batteries]) for lb in [2,12]]

print(part1, part2)