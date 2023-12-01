# super lang gedaan over het feit dat het kopieren van een list niet goed ging. 
from copy import deepcopy

Input = open("data/Day 22. input.txt", "r").read().split("\n")[:-1]

def parseInput(Input):
    cubes = []
    for line in Input:
        action, cuboids = line.split(" ",1)
        x,y,z = cuboids.split(",",2)
        x,y,z = x[2:].split(".."), y[2:].split(".."), z[2:].split("..")
        x,y,z = list(map(int,x)), list(map(int,y)), list(map(int, z))        
        cubes.append([action,x,y,z])
    return cubes

def rebootStep(step, lightsOn):
    step_lightsOn = []
    action,x,y,z = step
    for light in lightsOn:
        xn,yn,zn = light
        if xn[0] > x[1] or x[0] > xn[1] or yn[0] > y[1] or y[0] > yn[1] or zn[0] > z[1] or z[0] > zn[1]:
            step_lightsOn.append(deepcopy([xn, yn, zn]))
            continue
        
        if x[0] - xn[0] > 0:
            step_lightsOn.append(deepcopy([[xn[0], x[0] - 1], yn, zn]))
            xn[0] = x[0]
        if xn[1] - x[1] > 0:
            step_lightsOn.append(deepcopy([[x[1] + 1, xn[1]], yn, zn]))
            xn[1] = x[1]
        if y[0] - yn[0] > 0:
            step_lightsOn.append(deepcopy([xn, [yn[0], y[0] - 1], zn]))
            yn[0] = y[0]
        if yn[1] - y[1] > 0:
            step_lightsOn.append(deepcopy([xn, [y[1] + 1, yn[1]], zn]))
            yn[1] = y[1]
        if z[0] - zn[0] > 0:
            step_lightsOn.append(deepcopy([xn, yn, [zn[0], z[0] - 1]]))
        if zn[1] - z[1] > 0:
            step_lightsOn.append(deepcopy([xn, yn, [z[1] + 1, zn[1]]]))
   
    if action == "on":
        step_lightsOn.append(deepcopy([x,y,z]))  
    return deepcopy(step_lightsOn)

def countCubes(lightsOn):
    result = 0 
    for cube in lightsOn:
        x,y,z = cube
        numOfCubes = (x[1]-x[0]+1) * (y[1]-y[0]+1) *(z[1]-z[0]+1)
        result = result + numOfCubes
    return result

cubes = parseInput(Input)
lightsOn = []
for index, step in enumerate(cubes):
    lightsOn = rebootStep(step, lightsOn)
    if index == 19:
        print(countCubes(lightsOn))
print(countCubes(lightsOn))
