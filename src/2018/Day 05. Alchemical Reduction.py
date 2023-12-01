import string

Input=open("data/Day 05. input.txt", "r").read().split("\n")[0]

def react(polymer):   
    position = 0 
    while position < len(polymer)-1:
        firstChar = polymer[position]
        secondChar = polymer[position +1]
        
        if firstChar.lower() == secondChar.lower() and firstChar != secondChar:
            polymer = (polymer[:position] + polymer[position + 2:]).strip()
            if position >0:
                position = position -1
        else:
            position = position + 1
    return polymer

# Deel 1 
print(len(react(Input)))

# Deel 2 
minPolymer = len(Input)
for char in list(string.ascii_lowercase):
    polymer = Input
    polymer = polymer.replace(char, "").replace(char.capitalize(), "") 
    polymer = react(polymer)
    if len(polymer) < minPolymer:
        minPolymer = len(polymer)

print(minPolymer)
    
    
