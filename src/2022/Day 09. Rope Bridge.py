Input = open("data/dag 09. input.txt", "r").read().split("\n")[:-1]
motions = [line.split() for line in Input]
    
def rope(length):
    positions = [[0,0] for value in range(length)]
    visited = [[0,0]]
    
    def move_head(direction):
        if direction == "D":
            positions[0][1] = positions[0][1] - 1
        if direction == "U":
            positions[0][1] = positions[0][1] + 1
        if direction == "L":
            positions[0][0] = positions[0][0] - 1
        if direction == "R":
            positions[0][0] = positions[0][0] + 1
            
    def check_if_move():
        # check for each idx if they are still adjacent to idx-1. break if this is True
        for idx in range(1,length):
            if not check_adjacent(idx-1, idx):
                move_idx(idx)
            else:
                break
        
    def check_adjacent(idx1, idx2):
        # return True if the current position of idx is a direct neighbor of idx-1
        neighbors = [[xn, yn] for xn in range(positions[idx1][0]-1, positions[idx1][0]+2) for yn in range(positions[idx1][1]-1, positions[idx1][1]+2)]
        return positions[idx2] in neighbors
    
    def move_idx(idx):
        possible_positions = [[xn, yn] for xn in range(positions[idx-1][0]-1, positions[idx-1][0]+2) for yn in range(positions[idx-1][1]-1, positions[idx-1][1]+2)]
        
        # same x than move 1 up or down
        if positions[idx-1][0] == positions[idx][0]:
            possible_positions = [[xn, yn] for xn, yn in possible_positions if xn == positions[idx-1][0]]
        # same y than move 1 right or left    
        elif positions[idx-1][1] == positions[idx][1]:
            possible_positions = [[xn, yn] for xn, yn in possible_positions if yn == positions[idx-1][1]]
        # different x and y than move 1 diagonal    
        else:
            possible_positions = [[xn, yn] for xn, yn in possible_positions if yn != positions[idx][1] and xn != positions[idx][0]]
            
        neigbors_idx = [[xn, yn] for xn in range(positions[idx][0]-1, positions[idx][0]+2) for yn in range(positions[idx][1]-1, positions[idx][1]+2)]
        
        # since the neigbor always have 1 neighbor in common with possible position that are neighbors of idx-1 there is only one TRUE in neigbors_idx
        new_position = neigbors_idx[[value in possible_positions for value in neigbors_idx].index(True)]
        positions[idx] = new_position
        
        # add new position of tail if not yet visited
        if idx == length-1 and new_position not in visited:
            visited.append(new_position)
            
    for direction, steps in motions:
        for step in range(int(steps)):
            move_head(direction)
            check_if_move()

    return len(visited)

print(rope(2))
print(rope(10))
