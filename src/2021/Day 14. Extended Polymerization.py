from collections import defaultdict 

startPolymer, insertions = open("data/Day 14. input.txt", "r").read().split("\n\n", 1)
insertions = [line.split(" -> ") for line in insertions.split("\n")][:-1]
insertions = {key: value for key, value in insertions}

startingPairs = [startPolymer[i] + startPolymer[i+1] for i in range(0,len(startPolymer)-1)]

countPairs = defaultdict(int)
for pair in startingPairs:
    countPairs[pair] +=1

def step(countPairs):
    newCountPairs = defaultdict(int)
    for key, value in countPairs.items():
        insert = insertions[key] 
        newPairs = [key[0] + insert, insert + key[1]]
        
        for pair in newPairs:
            newCountPairs[pair] = newCountPairs[pair] + value
            
    return newCountPairs

for numOfstep in range(1,41):
    countPairs = step(countPairs)
    
    if numOfstep in [10,40]:
        allChars = set(list("".join(list(countPairs.keys()))))
        
        countChars = defaultdict(int)
        for char in allChars:
            count = sum([value for key, value in countPairs.items() if key[0] == char])
            countChars[char] = count
       
        countChars[startPolymer[-1]] += 1
        
        sortedValues = sorted(countChars.values())
        print(sortedValues[-1] - sortedValues[0])
        