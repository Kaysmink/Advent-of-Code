Input=open("data/Day 10. input.txt", "r").read().split("\n")[:-1]
Input=list(map(int, Input))

# Deel 1 
distribution = [0 for i in range(0,4)]
order = []
possibleAdapters = Input.copy()
currentJoltage = 0 

while len(possibleAdapters) > 0:
    possibles = list(range(currentJoltage + 1,currentJoltage+4))
    for joltage in possibles:
        if joltage in possibleAdapters:
            difference = joltage - currentJoltage
            order.append(difference)
            distribution[difference] = distribution[difference] + 1
            currentJoltage = joltage
            possibleAdapters.remove(joltage)
            break
        
print(distribution[1] * (distribution[3] + 1))
        
# Deel 2    
possibleAdapters = Input.copy()

tribonacci = [0 for i in range(0,max(possibleAdapters) +1)]
tribonacci[0] = 1
tribonacci[1] = 1
tribonacci[2] = 2

for i in range(3,len(tribonacci)):
    if i not in possibleAdapters:
        continue
    else:
        numOfWays = 0
        for value in [i-3, i-2, i-1]:
            numOfWays = numOfWays + tribonacci[value]  
            tribonacci[i] = numOfWays

print(tribonacci[-1])
        


