import re

Input = open("data/dag 14. input.txt", "r").read().split("\n")[:-1]
path_of_rocks = [re.findall(r'\d+,\d+', line) for line in Input]
path_of_rocks = [[list(map(int,coord.split(","))) for coord in line] for line in path_of_rocks]


def get_rocks():
    """
    save all rocks in a list of coords. 
    """
    allRocks = []
    for rocks in path_of_rocks:
        for index, rock in enumerate(rocks):
            if index == len(rocks)-1:
                break
            if rock[0] == rocks[index+1][0]:
                line_of_rocks = [[rock[0], y] for y in range(min(rock[1], rocks[index+1][1]), max(rock[1], rocks[index+1][1]) +1)]
                allRocks.extend(line_of_rocks)
            if rock[1] == rocks[index+1][1]:
                line_of_rocks = [[x, rock[1]] for x in range(min(rock[0], rocks[index+1][0]), max(rock[0], rocks[index+1][0]) +1)]
                allRocks.extend(line_of_rocks)

    allRocks = set([tuple(coord) for coord in allRocks])
    allRocks = [list(coord) for coord in allRocks]
    return allRocks

def drop_new_sand_part1(x,y):
    """
    drop new sand and while true get to the next row. if there are no rocks in the current column below the current coord 
    then the sand will fall infinitely so return false
    """
    while True:
        rocks_in_column = [[xn,yn] for xn,yn in rock_positions if xn == x and yn>y]      
        if len(rocks_in_column) == 0:
            return False
        
        new_coord = [x,y+1]
        left = [new_coord[0]-1,new_coord[1]]
        right = [new_coord[0]+1,new_coord[1]]
        
        if new_coord in sand_positions or new_coord in rock_positions:
            left = [new_coord[0]-1,new_coord[1]]
            right = [new_coord[0]+1,new_coord[1]]
            if left not in rock_positions and left not in sand_positions:
                x,y = left
            elif right not in rock_positions and right not in sand_positions:
                x,y = right
            else:
                sand_positions.append([x,y])
                return True
        else:
            x,y = new_coord


def max_sand():
    """
    it's impossible to get sand on a place which is below 3 rocks. so for [x,y]
    its only possible to contain sand if [x-1,y-1] [x,y-1] and [x+1,y-1] are not blocked by rocks. 
    also, if there are three coords above which cannot contain sand. than it is also impossible 
    
    therefore:
        loop over number of rows and for each row check the possible x value if above is true or false.
    """
    no_sand = [] 
    total_sand = 1
    for y in range(1, maxY):
        for x in range(500-y, 500+y+1):
            if [x,y] in rock_positions:
                continue
            three_above = [[xn,y-1] for xn in range(x-1,x+2)]
            blocked = [coord in rock_positions or coord in no_sand for coord in three_above]
            if all(blocked):
                no_sand.append([x,y])
                continue
            else:
                total_sand = total_sand+1
                
    return total_sand
            
rock_positions = get_rocks()
sand_positions = []
numOfSand = 0

while True:
    possible = drop_new_sand_part1(500, 0)
    if not possible:
        break
    numOfSand = numOfSand +1
print(numOfSand)    

# Deel 2
maxY = max([y for x,y in rock_positions]) + 2
print(max_sand())
