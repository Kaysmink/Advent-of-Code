import collections

Input=open("data/Day 08. input.txt", "r").read().split("\n")[:-1]
actions = [line.split(" ")[0] for line in Input]
values = [line.split(" ")[1] for line in Input]

def infinitLoop(actions, values):
    instructionNumber = 0 
    iteration = 1
    accumulator = 0 
    
    visitedDictionary = collections. defaultdict(list)
    
    while True:
        if instructionNumber >= len(actions):
            return (False, accumulator)
    
        action = actions[instructionNumber]
        value = values[instructionNumber]
        
        if(instructionNumber not in visitedDictionary.keys()):
            visitedDictionary[instructionNumber].append(iteration)
        else: 
            return(True, accumulator)
            
        if action == "acc":
            accumulator = accumulator + int(value)
            instructionNumber = instructionNumber + 1 
            
        if action == "jmp":
            instructionNumber = instructionNumber + int(value)
            
        if action == "nop":
            instructionNumber = instructionNumber + 1
            
        iteration = iteration + 1

# deel 1   
print(infinitLoop(actions, values)[1])

# deel 2 
for i in range(0, len(actions)):
    actionsCopy = actions.copy()
    if actionsCopy[i] == "nop":
        actionsCopy[i] = "jmp"
    if actionsCopy[i] == "jmp":
        actionsCopy[i] = "nop"

    infinite, accumulator = infinitLoop(actionsCopy, values)  
    
    if infinite == False:
        print(accumulator)
        break
        
