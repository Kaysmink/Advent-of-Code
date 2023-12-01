Input = list(open("data/dag 17. input.txt", "r").read())[:-1]
Input = list(open("data/test.txt", "r").read())

possible_rocks = [[[x,0] for x in range(2,6)], 
                  [[3,2], [2,1], [3,1],[4,1], [3,0]], 
                  [[4,2], [4,1], [2,0], [3,0], [4,0]], 
                  [[2,y] for y in range(0,4)], 
                  [[x,y] for x in range(2,4) for y in range(0,2)]]

push_dict = {"<":-1, ">":1}

def move_rock(rocks, x=0, y=0):
    x_values = [x for x,y in rocks]
    if 6 in x_values and x == 1:
        return rocks, False
    if 0 in x_values and x == -1:
        return rocks, False
    
    new_rock = [[xn+x, yn+y] for xn, yn in rocks]
    if any([rock in allRocks for rock in new_rock]):
        if y != 0:
            return rocks, True
        if x != 0:
            return rocks, False
    return new_rock, False
    
def drop_rock(rock_type):
    global idx_direction
    new_rock = possible_rocks[rock_type]
    start_y = max([y for x,y in allRocks]) + 4
    new_rock, end = move_rock(new_rock, y = start_y)
    
    while True:
        direction = Input[idx_direction%len(Input)]
        idx_direction = idx_direction + 1
        
        new_rock, end = move_rock(new_rock, x = push_dict[direction])
        new_rock, end = move_rock(new_rock, y = -1)
        
        if end:
            allRocks.extend(new_rock)
            return True
 
def needed_rocks():
    maxValues = []
    for x in range(0,6):
        maxY = max([y for xn,y in allRocks if xn == x])
        maxValues.append(maxY)
    needed = [[xn,yn] for xn,yn in allRocks if yn >= min(maxValues)-50]     
    
    topRow = [[xn,yn] for xn, yn in allRocks if yn == max(maxValues)]
    if len(topRow) == 7:
        print(rockNum)
        toprow.append(rockNum)
    return needed

idx_direction = 0
allRocks = [[x,0] for x in range(0,7)]

height = []
toprow = []
for rockNum in range(0,2022):
    print(rockNum)
    rock_type = rockNum%5
    drop_rock(rock_type)
    allRocks = needed_rocks()
    maxH = max([y for x,y in allRocks])
    height.append(maxH)

print(max([y for x,y in allRocks]))

