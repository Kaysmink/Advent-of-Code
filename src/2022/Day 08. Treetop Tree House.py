Input = open("data/dag 08. input.txt", "r").read().split("\n")[:-1]
trees = [list(map(int, list(line))) for line in Input]

def find_vissible_trees():
    global vissible
    for x, y in toCheck:
        height = trees[y][x]
        west = height > max([trees[y][xn] for xn in range(0,x)])
        east = height > max([trees[y][xn] for xn in range(x+1,len(Input))])
        north = height > max([trees[yn][x] for yn in range(0,y)])
        south = height > max([trees[yn][x] for yn in range(y+1,len(Input))])
    
        if any([west, east, north, south]):
            vissible.append([x,y])

def check_score(x,y):
    height = trees[y][x]
    
    west = [height > value for value in [trees[y][xn] for xn in range(0,x)][::-1]]
    east = [height > value for value in [trees[y][xn] for xn in range(x+1,len(Input))]]
    north = [height > value for value in [trees[yn][x] for yn in range(0,y)][::-1]]
    south = [height > value for value in [trees[yn][x] for yn in range(y+1,len(Input))]]
    
    westScore = len(west) if False not in west else west.index(False)+1
    eastScore = len(east) if False not in east else east.index(False)+1
    northScore = len(north) if False not in north else north.index(False)+1
    southScore = len(south) if False not in south else south.index(False)+1
        
    return westScore * eastScore * northScore * southScore

vissible = [[xn, yn] for xn in range(0,len(Input)) for yn in range(0,len(Input)) if (xn in [0,len(Input)-1] or yn in [0,len(Input)-1])]
toCheck = [[xn, yn] for xn in range(1,len(Input)-1) for yn in range(1,len(Input)-1)]

find_vissible_trees()      
print(len(vissible))       
print(max([check_score(x, y) for x,y in toCheck]))
