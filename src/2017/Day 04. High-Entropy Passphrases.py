from collections import Counter

Input = open("data/2017/dag 04. input.txt", "r").read().split("\n")[0:-1]
passphrases = [line.split() for line in Input]

part1 = sum([max(Counter(passphrase).values()) == 1 for passphrase in passphrases])
passphrases = [["".join(sorted(value)) for value in passphrase] for passphrase in passphrases]
part2 = sum([max(Counter(passphrase).values()) == 1 for passphrase in passphrases])

print(part1, part2)