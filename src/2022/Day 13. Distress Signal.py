Input = open("data/dag 13. input.txt", "r").read().split("\n\n")#[:-1]
pairs = [line.split("\n")[:2] for line in Input]


def check_order(line1, line2):
    index = 1
    if line1 == line2:
        return
    for index in range(len(line1)): 
        if index >= len(line2):
            return False
        value1 = line1[index]
        value2 = line2[index]
        if type(value1) == int and type(value2) == int:
            if value1 < value2:
                return True
            if value1 > value2:
                return False
            if value1 == value2:
                continue
        if type(value1) == list and type(value2) == int:
            value2 = [value2]
        if type(value2) == list and type(value1) == int:
            value1 = [value1]
        child = check_order(value1, value2)
        if child == False:
            return False
        if child == True:
            return True     
    
    if line1 == [] and line2 != []:
        return True
    
    if index == len(line1)-1:
        return True

# Deel 1 
result = []        
for index, pair in enumerate(pairs):
    line1, line2 = pair
    line1 = eval(line1)
    line2 = eval(line2)
    
    rightOrder = check_order(line1, line2)
    if rightOrder == True:
        result.append(index +1)

print(sum(result))

# Deel 2 
Input = open("data/dag 13. input.txt", "r").read().split("\n")
pairs = [pair for pair in Input if pair != ""]
pairs.append("[[2]]")
pairs.append("[[6]]")

pairs = sorted(pairs)
sorted_packets = [pairs.pop()]

while pairs:
    new = pairs.pop()
    
    for index, pair in enumerate(sorted_packets):
        infront = check_order(eval(new), eval(pair))
        if infront:
            sorted_packets.insert(index, new)
            break    
    else:
        sorted_packets.append(new)

print((sorted_packets.index("[[2]]")+1) * (sorted_packets.index("[[6]]")+1))
