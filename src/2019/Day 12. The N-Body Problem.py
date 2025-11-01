import re
from math import lcm

Input = open("data/2019/dag 12. input.txt", "r").read().split("\n")[0:-1]

start = [list(map(int,re.findall(r'[-\d]+', line))) for line in Input]
moons = [list(map(int,re.findall(r'[-\d]+', line))) for line in Input]
velocity = [[0,0,0] for line in enumerate(Input)]

def calculate_velocity():
    xPos, yPos, zPos = map(list, zip(*moons))
    for index, moon in enumerate(moons):
        x,y,z = moon
        xv,yv,zv = velocity[index]

        xn = xv + sum([1 if xn > x else -1 for xn in xPos if x != xn])
        yn = yv + sum([1 if yn > y else -1 for yn in yPos if y != yn])
        zn = zv + sum([1 if zn > z else -1 for zn in zPos if z != zn])

        velocity[index] = [xn,yn,zn]

def calculate_new_positions():
    for index, [xn,yn,zn] in enumerate(velocity):
        x,y,z = moons[index]
        moons[index] = [x+xn,y+yn,z+zn]


def calculate_energy():
    pot_energy = [abs(x)+abs(y)+abs(z) for x,y,z in moons]
    kin_energy = [abs(x)+abs(y)+abs(z) for x,y,z in velocity]

    result = sum([pot_energy[index]*kin_energy[index] for index in range(len(moons))])

    return result


def check_state():
    global xSeen, ySeen, zSeen

    xState, yState, zState = map(list, zip(*moons))
    xVel, yVel, zVel = map(list, zip(*velocity))
    if xState == xStart and xVel == [0,0,0,0] and xSeen == False:
        xSeen = count
        print("X seen", count)
    if yState == yStart and yVel == [0,0,0,0] and ySeen == False:
        ySeen = count
        print("Y seen", count)
    if zState == zStart and zVel == [0,0,0,0] and zSeen == False:
        zSeen = count
        print("Z seen", count)


def simulate_step():
    calculate_velocity()
    calculate_new_positions()
    check_state()


xStart, yStart, zStart = map(list, zip(*start))
xSeen = ySeen = zSeen = False

count = 0
while True:
    count += 1
    simulate_step()

    if count == 1000:
        part1 = calculate_energy()

    if xSeen and ySeen and zSeen:
        part2 = lcm(xSeen, ySeen, zSeen)
        break

print(part1, part2)
