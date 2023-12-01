from collections import defaultdict 

Input = open("data/Day 08. input.txt", "r").read().split("\n")[:-1]
Input = [[string.split(" ") for string in line.split(" | ")] for line in Input]

entries = [entry for entry, output in Input] 
output = [output for entry, output in Input] 

numberSegmentDict = {
    "abcefg": 0, 
    "cf": 1, 
    "acdeg": 2, 
    "acdfg": 3, 
    "bcdf": 4, 
    "abdfg": 5, 
    "abdefg": 6,
    "acf": 7, 
    "abcdefg": 8, 
    "abcdfg": 9}

# Deel 1
allOutput = [value for line in output for value in line]
print(len([value for value in allOutput if len(value) in [2,3,4,7]]))

# Deel 2 
resultSum = 0
for i in range(0,len(entries)):

    entry = [list(value) for value in entries[i]]
    oldOutput = [list(value) for value in output[i]]
    
    lengthEntries = [len(value) for value in entries[i]]
    indexLength5 = [index for index, value in enumerate(lengthEntries) if value == 5]
    indexLength6 = [index for index, value in enumerate(lengthEntries) if value == 6]
    
    segmentMapping = defaultdict()

    # Get "a" --> "a" is de difference tussen de characters van 1 en 7 
    segmentMapping["a"] = list(set(entry[lengthEntries.index(3)]).difference(set(entry[lengthEntries.index(2)])))[0]
    entry = [[value for value in entries if value != segmentMapping["a"]] for entries in entry]
    
    # Get "f" --> "f" is de intersect tussen de chars van 7 en de chars van alle getallen met 6 chars 
    segmentMapping["f"] = list(set(entry[lengthEntries.index(3)]).intersection(entry[indexLength6[0]],entry[indexLength6[1]],entry[indexLength6[2]]))[0]
    entry = [[value for value in entries if value != segmentMapping["f"]] for entries in entry]
    
    # Get "c" --> na het verwijderen van eerder bekende chars is "c" de char die is overgebleven in het enige getal die nog 1 char heeft. 
    segmentMapping["c"] = list(set([value[0] for value in entry if len(value) == 1]))[0]
    entry = [[value for value in entries if value != segmentMapping["c"]] for entries in entry]
    
    # Get "d" --> "d" is nu de intersection tussen de enige 2 getallen die nog 2 chars over hebben (34)
    index34 = [index for index, value in enumerate([len(value) for value in entry]) if value == 2]
    segmentMapping["d"] = list(set(entry[index34[0]]).intersection(entry[index34[1]]))[0]
    entry = [[value for value in entries if value != segmentMapping["d"]] for entries in entry]
    
    # Get "e" --> "e" is nu de char die maar 1 keer voorkomt in de overgebleven getallen die nog 3 chars hebben  (259)
    index259 = [index for index, value in enumerate([len(value) for value in entry]) if value == 2]
    values259 = entry[index259[0]] + entry[index259[1]] + entry[index259[2]]
    segmentMapping["e"] = [value for value in set(values259) if values259.count(value) == 1][0]
    entry = [[value for value in entries if value != segmentMapping["e"]] for entries in entry]
    
    # get "b" --> "b" is nu de char die maar 1 keer voorkomt is de getallen die nog 1 char over hebben (234)
    index234 = [index for index, value in enumerate([len(value) for value in entry]) if value == 1]
    values234 = entry[index234[0]] + entry[index234[1]] + entry[index234[2]]
    segmentMapping["b"] = [value for value in set(values234) if values234.count(value) == 1][0]
    entry = [[value for value in entries if value != segmentMapping["b"]] for entries in entry]
    
    # get "g" --> "g" is nu de enig overgebleven char
    lastValue = list(set([value for line in entry for value in line]))[0]
    segmentMapping["g"] = lastValue
    entry = [[value for value in entries if value != segmentMapping["g"]] for entries in entry]
    
    reverseSegmentMapping = defaultdict()
    for key, value in segmentMapping.items():
        reverseSegmentMapping[value] = key
    
    # map de output met de gevonden mappingstabel 
    newOutput = [[reverseSegmentMapping[oldChar] for oldChar in list(output)] for output in oldOutput]
    newOutput = [sorted(output) for output in newOutput]
    newOutput = int("".join([str(numberSegmentDict["".join(output)]) for output in newOutput]))
    resultSum = resultSum + newOutput
    
print(resultSum)