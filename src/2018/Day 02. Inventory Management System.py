Input=open("data/day 02. input.txt", "r").read().split("\n")[:-1]

# deel 1 
counter2 = 0 
counter3 = 0 
for ID in Input: 
    countList = [ID.count(character) for character in ID]
    if 2 in countList:
        counter2 = counter2 + 1
    if 3 in countList:
        counter3 = counter3 + 1

print(counter2 * counter3)        

# deel 2 
for ID1 in Input:
    for ID2 in Input:
        countDif = 0 
        for i in range(0,len(ID1)):
            if ID1[i] is not ID2[i]:
                countDif = countDif +1 
                index = i
            if countDif > 2 :
                break
        if countDif == 1:
            break 
    if countDif == 1:
            break

result = list(ID1)
result[index] = ""
print("".join(result))