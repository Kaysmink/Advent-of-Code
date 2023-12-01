import math
from dijkstar import Graph, find_path

Input= open("data/Day 15. input.txt", "r").read().split("\n")[:-1]
riskPerStep = [list(map(int,list(line))) for line in Input]

def findNeighbors(x,y):
    indexNeighbors = [[xn, yn] for xn in range(x-1,x+2) for yn in range(y-1,y+2) if 0<=xn<dim and 0<=yn<dim and (abs(x-xn) + abs(y-yn) == 1)]
    return indexNeighbors

def makeGraph(riskPerStep):
    graph = Graph()
    for x in range(0,dim):
        for y in range(0,dim):
            nodeNum = y*dim + x
            neighbors = findNeighbors(x,y)
            
            for xn,yn in neighbors:
                neighborNum = yn*dim + xn
                graph.add_edge(nodeNum, neighborNum, riskPerStep[yn][xn])
    return graph

def expandGrid():
    expandedGridColumn = riskPerStep.copy()
    for expand in range(0,4):
        newColumns =  [[risk+expand+1 for risk in line] for line in riskPerStep]
        newColumns =  [[risk if risk <10 else 1+(risk-10) for risk in line] for line in newColumns]
        
        expandedGridColumn = [expandedGridColumn[i] + newColumns[i] for i, row in enumerate(newColumns)]
    
    expandedGridRow = expandedGridColumn.copy()
    for expand in range(0,4):   
        newRows =  [[risk+1+expand for risk in row] for row in expandedGridColumn] 
        newRows =  [[risk if risk <10 else 1+(risk-10) for risk in line] for line in newRows]
    
        for row in newRows:
            expandedGridRow.append(row)
    return expandedGridRow

dim = len(Input)
riskToCoord = [[math.inf for x in range(0,dim)] for y in range(0,dim)]

graph = makeGraph(riskPerStep)
print(find_path(graph, 0, dim*dim-1)[3])

expandedGrid = expandGrid()
dim = len(expandedGrid)
graph = makeGraph(expandedGrid)
print(find_path(graph, 0, dim*dim-1)[3])
