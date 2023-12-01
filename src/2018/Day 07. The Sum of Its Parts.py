from collections import defaultdict 

Input=open("data/day 07. input.txt", "r").read().split("\n")[:-1]

def checkReady(takenStep):
    global stepsToWaitFor
    global stepsReady
    
    for key, value in stepsToWaitFor.items():
        if takenStep in value:
            stepsToWaitFor[key].remove(takenStep)
            if len(stepsToWaitFor[key]) == 0:
                stepsReady.append(key)
                stepsReady= sorted(stepsReady)

def freeWorker():
    for worker, busy in enumerate(workersBusyOnStep):
        if busy == False:
            return worker
    return "busy"

def updateBusyTime():
    global workersBusyTime
    workersBusyTime = [max(0, time-1) for time in workersBusyTime]

def checkIfDone():
    global stepsDone
    global workersBusyOnStep
    global stepsToTake

    for index, step in enumerate(workersBusyOnStep):
        if step != False and workersBusyTime[index] == 0:
            stepsDone.append(step)
            workersBusyOnStep[index] = False
            stepsToTake.remove(step)
            checkReady(step)

def putWorkersToWork():
    global workersBusyOnStep
    global stepsReady
    global workersBusyTime
    
    while freeWorker() != "busy" and len(stepsReady) > 0:
        worker = freeWorker()
        step = stepsReady[0]
        workersBusyOnStep[worker] = step
        workersBusyTime[worker] = 60 + (ord(step)-64)
        stepsReady.remove(step)
        
# deel 1 
stepsToTake = set()
stepsToWaitFor = defaultdict(list)
for rule in Input:
    step = rule.split(" ")[7]
    waitFor = rule.split(" ")[1]
    
    stepsToTake.update([step, waitFor])
    stepsToWaitFor[step].append(waitFor)

stepsToTake = list(stepsToTake)
stepsReady = sorted([step for step in stepsToTake if step not in stepsToWaitFor.keys()])

stepsInOrder = []
while len(stepsToTake) != 0:
    takeStep = stepsReady[0]
    stepsReady.remove(takeStep)
    stepsInOrder.append(takeStep)
    stepsToTake.remove(takeStep)
    checkReady(takeStep)

print("".join(stepsInOrder))

# deel 2 
stepsToTake = set()
stepsToWaitFor = defaultdict(list)
for rule in Input:
    step = rule.split(" ")[7]
    waitFor = rule.split(" ")[1]
    
    stepsToTake.update([step, waitFor])
    stepsToWaitFor[step].append(waitFor)

stepsToTake = list(stepsToTake)
stepsReady = sorted([step for step in stepsToTake if step not in stepsToWaitFor.keys()])

stepsDone = []
numOfWorkers = 5
maxSteps = len(stepsToTake)
        
workersBusyTime = [0] * numOfWorkers
workersBusyOnStep = [False] * numOfWorkers

secondsPassed = 0 
while len(stepsDone) != maxSteps:    
    updateBusyTime()
    checkIfDone()
    putWorkersToWork()
    
    secondsPassed = secondsPassed + 1

print(secondsPassed -1)

    
    
    
    
