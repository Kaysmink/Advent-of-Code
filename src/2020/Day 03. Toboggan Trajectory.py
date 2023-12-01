Input = open('data/Day 03. input.txt' , 'r')
Input = [line.split() for line in Input]

maxY = len(Input) -1 
maxX = len(Input[1][0]) -1

def numberOfTrees(slopeX, slopeY):
    x = 0
    y = 0
    trees = 0 
    
    while y<= maxY:    
        if x > maxX:
            verschil = x - maxX -1
            x = verschil
        
        if Input[y][0][x] == "#":
            trees = trees + 1
        
        x = x+slopeX
        y = y+slopeY
        
    return(trees)

# deel 1  
print(numberOfTrees(3,1))

# deel 2 
print(numberOfTrees(1,1) * numberOfTrees(3,1) * numberOfTrees(5,1) * numberOfTrees(7,1) * numberOfTrees(1,2))