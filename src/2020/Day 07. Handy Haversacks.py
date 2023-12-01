from collections import defaultdict
Input=open("data/Day 07. input.txt", "r").read().split("\n")[:-1]

bagDictionary = defaultdict(list) 
searching = "shiny gold"


# deel 1  
for line in Input: 
    line = line.split("bags contain ")
    headBag = line[0].strip()
    content = [x.strip().replace(".", "") for x in line[1].strip().split(",")]
    for bag in content:
        bag = bag.split(" ", 1)
        bagDictionary[headBag].append(bag[1].replace(" bags", "").replace(" bag", "").strip())
    
allColours = list(bagDictionary.keys())
possible = [colour for colour in allColours if searching in bagDictionary[colour]]

while True:
    newPossible    = []
    for colours in possible:
        new = [colour for colour in allColours if colours in bagDictionary[colour] and colour not in possible]
        newPossible.extend(new)

    if len(newPossible) == 0:
        break
    
    possible.extend(newPossible)
    possible = list(set(possible))

print(len(possible))

# deel 2 
# opnieuw inlezen aangezien ik delen heb overgeslagen welke niet nodig waren in 1 
bagDictionary = defaultdict(lambda: defaultdict(int)) 
for line in Input: 
    contentDict = defaultdict() 
    line = line.split("bags contain ")
    headBag = line[0].strip()
    content = [x.strip().replace(".", "") for x in line[1].strip().split(",")]
    for bag in content:
        bag = bag.split(" ", 1)
        contentDict[bag[1].replace(" bags", "").replace(" bag", "").strip()] = bag[0]
        bagDictionary[headBag] = contentDict

emptyBags = [bags for bags in allColours if "other" in bagDictionary[bags].keys()]

def countBags(colour):
    Total = 1
    
    if colour in emptyBags: 
        return Total
    
    for key, value in bagDictionary[colour].items(): 
        Total = Total + (countBags(key) * int(value))
        
    return Total

print(countBags(searching) - 1)


    