from collections import defaultdict

Input = list(map(int, open("data/2024/dag 22. input.txt", "r").read().split("\n")[0:-1]))


def mix_prune(n1, n2):
    return (n1 ^ n2) % 16777216


def next_number(number, n, part):
    numbers = [number]
    for i in range(n):
        number = mix_prune(number, number * 64)
        number = mix_prune(number, number // 32)
        number = mix_prune(number, number * 2048)
        numbers.append(number)

    if part == 1:
        return numbers

    seq_dict = defaultdict(int)
    prices = [int(str(number)[-1]) for number in numbers]
    changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]

    for i in range(4, len(changes) + 1):
        seq = tuple(changes[i - 4:i])
        if seq not in seq_dict.keys():
            seq_dict[seq] = prices[i]

    return seq_dict


part1 = sum([next_number(number, 2000, 1)[-1] for number in Input])

changes_seq = [next_number(number, 2000, 2) for number in Input]
poss_seq = set([key for sub in changes_seq for key in sub.keys()])
part2 = max([sum([changes[seq] for changes in changes_seq]) for seq in poss_seq])

print(part1, part2)
