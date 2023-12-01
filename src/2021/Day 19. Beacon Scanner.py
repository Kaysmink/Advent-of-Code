import itertools

Input = open("data/Day 19. input.txt", "r").read().split("\n\n")
#Input = open("data/test.txt", "r").read().split("\n\n")


def parseInput(Input):
    scannerReport = []
    for scanner in Input:
        subReport = []
        report = scanner.split("\n")[1:]
        for line in report:
            if line != "":
                subReport.append(list(map(int,line.split(","))))
        scannerReport.append(subReport)
    return scannerReport

def allOrientation(scanner):
    orientationList = [] 
    for x,y,z in itertools.permutations("012",3):
        x,y,z = [int(x), int(y), int(z)]
        newOrientation = [[line[x], line[y], line[z]] for line in scanner]
        orientationList.append(newOrientation)
    return orientationList

def relativeOrientation(scanner, xn, yn, zn):
    scanner = [[x+xn, y+yn, z+zn] for x,y,z in scanner]
    return scanner

def findOverlapping(scanner1, scanner2):
    overlap = [x for x in scanner2 if x in scanner1]
    
    if len(overlap) >= 12:
        return [True, overlap]
    return [False, overlap]

def checkOverlapping(scanner1, scanner2):
    orientations = allOrientation(scanner2)
    for x in range(-1000,1000):
        for y in range(-5,5):
            for z in range(-5,5):
                for orientatiation in orientations:
                    relativePos = relativeOrientation(orientatiation, x, y, z) 
                    overlapping = findOverlapping(scanner1, relativePos)
                    print(overlapping)
                    if overlapping[0]:
                        print(overlapping[1])
                        return True




scannerReport = parseInput(Input)
checkOverlapping(scanner1, scanner2)
