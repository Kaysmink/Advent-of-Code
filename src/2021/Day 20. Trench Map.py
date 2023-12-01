from copy import deepcopy

Input = open("data/Day 20. input.txt", "r").read().split("\n\n")
enhancement = Input[0]
inputImage = [list(line) for line in Input[1].split("\n")][:-1]

def findNeighbors(x,y, Input):
    neighbors = [Input[yn][xn] for yn in range(y-1,y+2) for xn in range(x-1,x+2) if 0<=xn<len(Input[0]) and 0<=yn<len(Input)]
    return neighbors

def extendImage(inputImage, iteration):
    if enhancement[0] == "#" and iteration%2 == 1:
        inputImage = [["#", "#", "#"] + line + ["#", "#", "#"] for line in inputImage]
        
        for _ in range(3):
            inputImage = [["#"]*len(inputImage[0])] + inputImage
            inputImage = inputImage + [["#"]*len(inputImage[0])]
    else:
        inputImage = [[".", ".", "."] + line + [".", ".", "."] for line in inputImage]
            
        for _ in range(3):
            inputImage = [["."]*len(inputImage[0])] + inputImage
            inputImage = inputImage + [["."]*len(inputImage[0])]
            
    return deepcopy(inputImage)

def getNewValue(x,y, inputImage, iteration): 
    if x <= 1 or y <= 1 or x >= len(inputImage)-2 or y >=len(inputImage)-2:
        if enhancement[0] == "#" and iteration%2 == 1:
            newValue = enhancement[511]
        else:
            newValue = enhancement[0]
    else:
        neighbors = findNeighbors(x,y, inputImage)
        binary = int("".join(neighbors).replace(".", "0").replace("#", "1"),2)
        newValue = enhancement[binary]
        
    return newValue

def enhanceAlgo(inputImage, iteration):
    inputImage = extendImage(inputImage, iteration)
    newImage = deepcopy(inputImage)
    
    for x in range(0,len(inputImage[0])):
        for y in range(0,len(inputImage)):
            newImage[y][x] = getNewValue(x,y, inputImage, iteration)
    return newImage

def countLitPixels(inputImage):
    lit = sum([line.count("#") for line in inputImage])
    return lit
    
for iteration in range(0,50):
    inputImage = enhanceAlgo(inputImage, iteration)
    if iteration in [1,49]:
        print(countLitPixels(inputImage))

