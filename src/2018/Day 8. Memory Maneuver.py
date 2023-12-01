Input = list(map(int,open("data/day 08. input.txt", "r").read().strip().split(" ")))
Input = list(map(int,open("data/test.txt", "r").read().strip().split(" ")))

def parseNode(node):
    global allMetas
    global metaEnd
    
    print(currentParrent)
    numOfChilds, numOfMeta = node[0], node[1]
    node = node[2:]
    meta = []
    
    if numOfChilds == 0:
        meta = meta + node[0:numOfMeta]
        allMetas = allMetas + meta
        node = node[numOfMeta:]
        node = parseNode(node)
    else:
        metaEnd += numOfMeta
        node = parseNode(node)
        
    return node


metaEnd = 0 
currentParrent = 1
node = Input.copy()
allMetas = []
test = parseNode(node)
