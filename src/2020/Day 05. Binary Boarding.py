Input=open("data/Day 05. input.txt", "r").read().split("\n")[:-1]

highestID = 0 
IDs = []

# deel 1 
for line in Input: 
    maxRow = 127
    minRow = 0
    maxCol = 7 
    minCol = 0
    for letter in line[0:7]:
        
        if letter == "F":
            maxRow = (maxRow + minRow) // 2
        else: 
            minRow = (maxRow + minRow) // 2 + 1
    
    for letter in line[7:11]:
        if letter == "L":
            maxCol = (maxCol + minCol) // 2
        else: 
            minCol = (maxCol + minCol) // 2 + 1
    
    seatID = maxRow*8 + maxCol
    IDs.append(seatID)
    
    if seatID > highestID:
        highestID = seatID
        
# deel 2 
for ID in IDs: 
    if (ID + 2) in IDs and (ID + 1) not in IDs:
        result = ID + 1
        
print(highestID)
print(result)
        