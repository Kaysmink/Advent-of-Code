import re

Input = open("data/dag 15. input.txt", "r").read().split("\n")[:-1]
Input = open("data/test.txt", "r").read().split("\n")[:-1]
coords = [list(map(int,re.findall(r'[-]?\d+', line))) for line in Input]
beacons = [list(map(int,re.findall(r'[-]?\d+', line)))[2:] for line in Input]
sensors = [list(map(int,re.findall(r'[-]?\d+', line)))[:2] for line in Input]


def impossible_in_row(y):
    row = []
    for line in coords:
        sx, sy, bx, by = line
        distance = abs(sx-bx) + abs(sy-by)

        rangeFromS = [[x, y] for x in range(sx-distance, sx+distance+1) if abs(sx-x) + abs(sy-y) <= distance]
        row.extend(rangeFromS)
        
    row = set([tuple(coord) for coord in row if coord not in beacons and coord not in sensors])
    return row

# Deel 1
result = impossible_in_row(10)
print(len(result))



def man_distance(x,y,sx,sy):
    return abs(sx-x) + abs(sy-y)

def find_possible(maxValue):
    for x in range(maxValue+1):
        for y in range(maxValue+1):
            in_range=[]
            for sx,sy,bx,by in coords:
                maxDistance = abs(sx-bx) + abs(sy-by)
                distance = abs(sx-x) + abs(sy-y)
                
                if distance <= maxDistance:
                    in_range.append(True)
                else:
                    in_range.append(False)
            if sum(in_range) == 0:
                return [x,y]
    return ["NIET GEVONDEN"]

# Deel 2
find_possible(20)

                
    