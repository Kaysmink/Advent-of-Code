Input = open("data/Day 01. input.txt", "r").read().split("\n")[:-1]
Input = list(map(int,Input))

print(sum([Input[i] > Input[i-1] for i in range(1, len(Input))]))
print(sum([sum(Input[i:i+3]) > sum(Input[i-1:i+3-1]) for i in range(1, len(Input))]))
