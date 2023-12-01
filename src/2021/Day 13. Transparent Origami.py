import pandas as pd 

Input= open("data/Day 13. input.txt", "r").read().split("\n\n", 1)
coords = [list(map(int,line.split(","))) for line in Input[0].split("\n")]
folds = [[line.split("=")[0][-1], int(line.split("=")[1])]  for line in Input[1][:-1].split("\n")]

def fold(coords, direction, value):
    main = [coord for coord in coords if coord[1] < value] if direction == "y" else [coord for coord in coords if coord[0] < value]
    foldPart = [coord for coord in coords if coord[1] > value] if direction == "y" else [coord for coord in coords if coord[0] > value]
    foldPart = [[coord[0], value-(coord[1]-value)] for coord in foldPart] if direction == "y" else [[value-(coord[0]-value), coord[1]] for coord in foldPart]
    
    main = main + foldPart
    
    return main


for foldParameters in folds:
    direction, value = foldParameters
    coords = fold(coords, direction, value)
    
    # Deel 1 
    if fold == folds[0]:
        print(len(coords))

# deel 2 
coordsMatrix = [["" if [xn,yn] not in coords else "#" for xn in range(0,max(coords, key=lambda x: x[0])[0] + 1)] for yn in range(0, max(coords, key=lambda x: x[1])[1] +1 )]
      
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
print(pd.DataFrame(coordsMatrix))
