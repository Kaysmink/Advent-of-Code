import re
from copy import deepcopy
from itertools import groupby

password = open("data/2015/dag 11. input.txt", "r").read().strip()


def seq_to_password(seq):
    number = "".join([chr(value+96) for value in seq])

    return number


def next_seq(seq):
    seq = deepcopy(seq)

    curr_pos = len(seq) - [value != 26 for value in seq[::-1]].index(True) - 1
    seq[curr_pos] = seq[curr_pos] + 1

    for x in range(curr_pos+1,len(seq)):
        seq[x] = 1

    return seq.copy()


def check_password(new_password, seq):
    incr = [(char, sum(1 for _ in group)) for char, group in groupby([seq[i] == seq[i-1] +1 for i in range(1, len(seq))])]
    increasing = len([(value, count) for value, count in incr if value and count >=2]) >=1

    forbidden = not any([char in new_password for char in "iol"])
    double = len(re.findall(r"(.)\1", new_password)) >=2

    return all([increasing, forbidden, double])


def new_password(password):
    curr_seq = [ord(char)-96 for char in password]
    while True:
        curr_seq = next_seq(curr_seq)
        new_password = seq_to_password(curr_seq)
        if check_password(new_password, curr_seq):
            return new_password

part1 = new_password(password)
part2 = new_password(part1)

print(part1, part2)


