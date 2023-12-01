Input = open("data/dag 03. input.txt", "r").read().split("\n")[:-1]

# Deel 1
compartments = [[list(line[0:len(line)//2]), list(line[len(line)//2:])] for line in Input]
intersections = [list(set(com1).intersection(set(com2)))[0] for com1, com2 in compartments]
print(sum([ord(char) - 96 if char.islower() else ord(char)-38 for char in intersections]))

# Deel 2
groups = [Input[i:i+3] for i in range(0,len(Input), 3)]
intersections = [list(set(elf1).intersection(set(elf2), set(elf3)))[0] for elf1, elf2, elf3 in groups]
print(sum([ord(char) - 96 if char.islower() else ord(char)-38 for char in intersections]))


# oneline monsters
print(sum([ord(char) - 96 if char.islower() else ord(char)-38 for char in [list(set(com1).intersection(set(com2)))[0] for com1, com2 in [[list(line[0:len(line)//2]), list(line[len(line)//2:])] for line in Input]]]))
print(sum([ord(char) - 96 if char.islower() else ord(char)-38 for char in [list(set(elf1).intersection(set(elf2), set(elf3)))[0] for elf1, elf2, elf3 in [Input[i:i+3] for i in range(0,len(Input), 3)]]]))
