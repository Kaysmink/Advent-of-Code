from collections import defaultdict

Input=open("data/day 12. input.txt", "r").read().split("\n")[:-1]

def get_starting_state():
    initialState = Input[0].split(": ")[1]
    currentState = defaultdict(bool)
    for index, pot in enumerate(initialState):
        if pot == "#":
            currentState[index] = True
    return currentState

def get_rules():
    rulesList = Input[2::]
    rules = defaultdict(str)
    for rule in rulesList:
        rule, outcome = rule.split(" => ")
        seq = []
        start = -2
        while start <3:
            pot = rule[start+2]
            if pot == "#":
                seq.append(str(start))
            start = start + 1
        key = ",".join(seq)
        rules[key] = True if outcome == "#" else False
    return rules

def check_neighbors(pot):
    neighbors = [pot for pot in range(pot-2, pot+3)]
    ruleSeq = []
    for index, neighbor in enumerate(neighbors):
        if neighbor in currentState.keys():
            ruleSeq.append(str(index-2))
    key = ",".join(ruleSeq)
    return key

def next_generation():
    minPot = min(currentState.keys())
    maxPot = max(currentState.keys())
    
    nextState = defaultdict(bool)
    for pot in range(minPot-2, maxPot+3):
        neighborSituation = check_neighbors(pot)  
        nextPotState = rules[neighborSituation]
        if nextPotState == True:
            nextState[pot] = True
    return nextState

currentState = get_starting_state()
rules = get_rules()
for generation in range(1,150):
    old_sum = sum(currentState.keys())
    currentState = next_generation()
    
    if generation == 20:
        print(sum(currentState.keys()))
        
    if generation == 129:
        keepGeneration = currentState
        
    #print(generation, sum(currentState.keys()), sum(currentState.keys()) - old_sum)


# because we see that after generation 129 the differences between each generation 
# stays constant we can simply add this constant value untill we reach 
# 50 billion generations
result = sum(keepGeneration.keys()) + 52*(50000000000 - 129) 
print(result)

















