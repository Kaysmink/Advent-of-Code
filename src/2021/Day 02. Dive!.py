Input = open("data/Day 02. input.txt", "r").read().split("\n")[:-1]

# Deel 1 
posHorizontal = 0 
posDepth = 0

for command in Input:
    direction, value = command.split(" ")
    
    if direction == "forward":
        posHorizontal = posHorizontal + int(value)
        continue 
    
    posDepth = posDepth + int(value) if direction == "down" else posDepth - int(value)
    
print(posHorizontal * posDepth)
    
# Deel 2 
posHorizontal = 0 
posDepth = 0
aim = 0 

for command in Input:
    direction, value = command.split(" ")
    
    if direction == "forward":
        posHorizontal = posHorizontal + int(value)
        posDepth = posDepth + (int(value) * aim)
        continue 
    
    aim = aim + int(value) if direction == "down" else aim - int(value)
    
print(posHorizontal * posDepth)