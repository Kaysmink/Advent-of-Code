Input = open("data/2017/dag 01. input.txt", "r").read().strip()

seq = Input + Input[0]
part1 = sum([int(seq[i]) for i in range(len(seq)-1) if seq[i] == seq[i+1]])

seq = Input + Input
part2 = sum([int(seq[i]) for i in range(len(Input)) if seq[i] == seq[i+len(Input)//2]])

print(part1, part2)