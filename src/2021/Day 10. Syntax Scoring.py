Input = open("data/Day 10. input.txt", "r").read().split("\n")[:-1]
Input = [list(line) for line in Input]

matchingDict = {"(": ")", "[": "]", "{": "}", "<": ">"}
scoreDictPart1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
scoreDictPart2 = {")": 1,"]": 2, "}": 3, ">": 4}
openingSymbols = ["(", "[", "{", "<"]

def scoreLine(line):
    global errorSum
    openingOrder = []

    for char in line:
        if char in openingSymbols:
            openingOrder.append(char)
            continue
        
        lastOpening = openingOrder.pop()
        if matchingDict[lastOpening] != char:
            errorSum = errorSum + scoreDictPart1[char]
            break
    else:   
        incompleteScores.append(scoreIncomplete(openingOrder))

def scoreIncomplete(line):
    line = line[::-1]
    score = 0 
    for char in line:
        score = score*5 + scoreDictPart2[matchingDict[char]]
    return score

# Deel 1/ Deel 2 
incompleteScores = []
errorSum = 0

for line in Input:
    scoreLine(line)

print(errorSum)
print(sorted(incompleteScores)[len(incompleteScores)//2])
