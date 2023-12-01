from collections import defaultdict

Input = open("data/Day 12. input.txt", "r").read().split("\n")[:-1]
edges = [[x for x in line.split("-")] for line in Input]

neighborsDict = defaultdict(list)
for start, end in edges:
    neighborsDict[start].append(end)
    neighborsDict[end].append(start)

def findNextPath(path, part):
    lastCave = path[-1]
    neighbors = neighborsDict[lastCave]
    
    for neighbor in neighbors:
        newPath = path.copy()
        if neighbor == "end":
            newPath.append(neighbor)
            allPaths.append(newPath)
            continue
        
        if part == "part1":
            if neighbor.islower() and neighbor in newPath:
                continue 
            
        if part == "part2":
            smallCaves = [cave for cave in set(newPath) if cave.islower()]
            visitedTwice = False if max([newPath.count(cave) for cave in smallCaves]) <2 else True
            if (neighbor.islower() and visitedTwice == True and newPath.count(neighbor) > 0) or neighbor == "start":
                continue             
        
        newPath.append(neighbor)
        findNextPath(newPath, part)


firstPaths = [["start", neighbor] for neighbor in neighborsDict["start"]]
for part in ["part1", "part2"]:
    allPaths = []
    for path in firstPaths:
        findNextPath(path, part)
    print(len(allPaths))
