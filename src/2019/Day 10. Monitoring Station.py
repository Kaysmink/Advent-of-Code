from math import gcd
from math import atan2, pi
from collections import deque

Input = open("data/2019/dag 10. input.txt", "r").read().split("\n")[0:-1]

Map = [list(line) for line in Input]
astroids = [(x, y) for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == "#"]
directions = set([(x//gcd(x,y), y//gcd(x,y)) for x in range(-len(Map[0]),len(Map[0])) for y in range(-len(Map),len(Map)) if abs(x) + abs(y) >0])

def detect_astroids(x,y):
    astroids = []
    for direction in directions:
        poss_positions = [(x+direction[0]*n, y+direction[1]*n) for n in range(1,len(Map[0]))]
        poss_positions = [(x,y) for x,y in poss_positions if 0<=x<len(Map[0]) and 0<=y<len(Map)]

        if any([Map[y][x] == "#" for x,y in poss_positions]):
            astroids.append([direction, poss_positions])

    return astroids


def vaporize(astroids):
    clockwise_directions = [[x, y, atan2(x, y) / pi * 180, coords] for [[x, y],coords] in astroids]
    clockwise_directions = sorted(clockwise_directions, key=lambda x: (x[2]), reverse=True)

    seen_astroids = deque([astroids for [x,y,degree,astroids] in clockwise_directions])

    vape_count = 0
    while True:
        if seen_astroids[0]:
            x,y = seen_astroids[0].pop(0)
            vape_count += 1
            if vape_count == 200:
                return x*100+y
        seen_astroids.rotate(-1)



detected_astroids = [detect_astroids(x,y) for x,y in astroids]
part1 = max(len(astroids) for astroids in detected_astroids)

astroids = [astroids for astroids in detected_astroids if len(astroids) == part1][0]
part2 = vaporize(astroids)

print(part1, part2)