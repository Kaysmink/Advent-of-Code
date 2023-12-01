Input = open("data/dag 18. input.txt", "r").read().split("\n")[:-1]
coords = [list(map(int,line.split(","))) for line in Input]
coords = [tuple(coord) for coord in coords]

def check_sides(x,y,z):
    global checked_coords
    neighbors = [(xn,yn,zn) for xn in range(x-1, x+2) for yn in range(y-1, y+2) for zn in range(z-1, z+2) 
             if abs(xn-x) + abs(yn-y) + abs(zn-z) == 1]
    
    not_blocked = [neighbor not in coords for neighbor in neighbors]
    
    coord_not_blocked = [neighbors[index] for index, value in enumerate(not_blocked) if value == True and neighbors[index] not in checked_coords]
    
    checked_coords.extend(coord_not_blocked)
    checked_coords = list(set(checked_coords))
        
    return sum(not_blocked)

# Deel 1
checked_coords = []
values = [check_sides(x, y, z) for x,y,z in coords]
print(sum(values))


# Deel 2
def external():
    to_check = [(0,0,0)]
    checked = set()
    result = 0
    
    while to_check:
        x,y,z = to_check.pop(0)
        checked.add((x,y,z))
        
        if x < minX or x > maxX or y < minY or y > maxY or z < minZ or z > maxZ:
            continue
        
        neighbors = [(xn,yn,zn) for xn in range(x-1, x+2) for yn in range(y-1, y+2) for zn in range(z-1, z+2) 
             if abs(xn-x) + abs(yn-y) + abs(zn-z) == 1]
        
        for neighbor in neighbors:
            if neighbor not in checked and neighbor not in to_check:
                if neighbor in coords:
                    result = result +1
                else:
                    to_check.append(neighbor)
    return result 

minX = min([x for x,y,z in coords])-1
minY = min([y for x,y,z in coords])-1
minZ = min([z for x,y,z in coords])-1
maxX = max([x for x,y,z in coords])+1
maxY = max([y for x,y,z in coords])+1
maxZ = max([z for x,y,z in coords])+1

result = external()
print(result)

