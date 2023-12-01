Input = open("data/Day 03. input.txt", "r").read().split("\n")[:-1]

# Deel 1 
bitsOnPosition = [[number[i] for number in Input] for i in range(0,len(Input[1]))]
gamma = int("".join(["0" if line.count("0") > len(Input)/2 else "1" for line in bitsOnPosition]),2)
epsilon = int("".join(["0" if line.count("0") < len(Input)/2 else "1" for line in bitsOnPosition]),2)

print(gamma*epsilon)

# deel 2 
validOxygen = Input.copy()
validCo2 = Input.copy()

for i in range(0,len(bitsOnPosition)):
    bitsOnPositionOxygen = [[number[i] for number in validOxygen] for i in range(0,len(Input[1]))]
    bitsOnPositionCo2 = [[number[i] for number in validCo2] for i in range(0,len(Input[1]))]
    
    mostCommon = "0" if bitsOnPositionOxygen[i].count("0") > bitsOnPositionOxygen[i].count("1") else "1"
    leastCommon = "1" if bitsOnPositionCo2[i].count("0") > bitsOnPositionCo2[i].count("1") else "0"
    
    if len(validOxygen) > 1:
        validOxygen = [number for number in validOxygen if number[i] == mostCommon]
    if len(validCo2) > 1:    
        validCo2 = [number for number in validCo2 if number[i] == leastCommon]
    
oxygen = int(validOxygen[0],2)
co2 = int(validCo2[0],2)

print(oxygen * co2)