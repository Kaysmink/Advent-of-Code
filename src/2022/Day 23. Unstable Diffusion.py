from collections import deque

Input = open("data/dag 23. input.txt", "r").read().split("\n")[:-1]

lines = [list(line) for line in Input]
elves = [(x,y) for y in range(len(lines)) for x in range(len(lines[y])) if lines[y][x] == "#"]

check_order = deque(["N", "S", "W", "E"])
check_elfs = {"N":[0,3,5], "S":[2,4,7], "E":[5,6,7], "W":[0,1,2]}
move_direction = {"N":"(x,y-1)", "S":"(x,y+1)", "W":"(x-1,y)", "E":"(x+1,y)"}

def get_new_pos(elf):
    x,y = elf
    all_neighbors = [(xn,yn) not in elves for xn in range(x-1, x+2) for yn in range(y-1, y+2) if (xn,yn) != elf]

    if all(all_neighbors):
        return elf
    
    for value in check_order:
        neighbors = [all_neighbors[index] for index in check_elfs[value]]

        if all(neighbors):
            return eval(move_direction[value])
    
    return elf

def move_elves(new_positions, elves):
    counts = [new_positions.count(position) == 1 for position in new_positions]

    new_positions = [new_positions[index] if value else elves[index] for index, value in enumerate(counts)]
    movingNum = sum([new_positions[index] != elves[index] for index, value in enumerate(new_positions)])
    
    return [new_positions, movingNum]

iteration = 1
while True: 
    new_positions = [get_new_pos(elf) for elf in elves]
    elves, movingNum = move_elves(new_positions, elves)
    
    if iteration == 10:
        xCoords = [x for x,y in elves]
        yCoords = [y for x,y in elves]
        print((max(xCoords) - min(xCoords) +1) * (max(yCoords) - min(yCoords)+1) - len(elves))
        
    if movingNum == 0:
        print(iteration)
        break
    
    check_order.rotate(-1)
    iteration = iteration +1
