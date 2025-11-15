from collections import defaultdict

replacement, goal = open("data/2015/dag 19. input.txt", "r").read().split("\n\n")

replacements = defaultdict(list)
for line in replacement.split("\n"):
    old,new = line.split(" => ")
    replacements[old].append(new)

def create_molecules(string):
    poss_replacements = [sub for sub in replacements.keys() if sub in string]
    molecules = [string[:i] + new_value + string[i + len(char):] for i in range(len(string))
                for char in poss_replacements for new_value in replacements[char] if string.startswith(char, i)]

    return set(molecules)


def create_medicine(medicine):
    global replacements
    medicine = medicine.strip()
    replacements = [(key,value) for key,values in replacements.items() for value in values]

    count = 0
    while medicine != "e":
        for old, new in replacements:
            if new in medicine:
                medicine = medicine.replace(new,old,1)
                count = count + 1
    return count

molecules = create_molecules(goal)
part1 = len(molecules)
part2 = create_medicine(goal)

print(part1, part2)
