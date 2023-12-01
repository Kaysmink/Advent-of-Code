import itertools as it

Input=open("data/Day 09. input.txt", "r").read().split("\n")[:-1]
Input=list(map(int, Input))

lowestIndex = 0
index = 25
preamble = Input[lowestIndex:lowestIndex + 25]

def isValid(numbers, goal):
    for combination in it.combinations(numbers, 2):
        if sum(combination) == goal:
            return(True)
    return(False)

# Deel 1           
for number in Input[25::]:
    numbers = Input[lowestIndex:index]
    goal = Input[index]
    
    if isValid(numbers, goal) == False:
        print(goal)
        break
    
    lowestIndex = lowestIndex + 1 
    index = index + 1

# Deel 2
numbers = [x for x in Input if x<goal]

index = 0
numOfNumbers = 2
found = False

while found == False:
    for i in range(0,len(numbers) - numOfNumbers):
        combination = numbers[i:i + numOfNumbers]
        if sum(combination) == goal:
            print(min(combination) + max(combination))
            found = True
            break
    numOfNumbers = numOfNumbers + 1 
    