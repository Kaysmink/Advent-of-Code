import math

Input=open("data/Day 13. input.txt", "r").read().split("\n")[:-1]
arrivalTime = int(Input[0])
possibleBusses = [int(bus) for bus in Input[1].split(",") if bus != "x"]

# deel 1 
minimumWaitTime = math.inf
bestBus = None

for bus in possibleBusses:
    waittime = bus - (arrivalTime%bus)
    if waittime < minimumWaitTime:
        minimumWaitTime = waittime
        bestBus = bus
result = bestBus * minimumWaitTime
        
print(result)

# deel 2 
possibleBusses = [[int(bus), Input[1].split(",").index(bus)] for bus in Input[1].split(",") if bus != "x"]

time = possibleBusses[0][0]
addTime = possibleBusses[0][0]
addBusInTime = [possibleBusses[0][0]]

for bus, index in possibleBusses[1::]:
    while True:
        waittime = bus - (time%bus)
        if index > bus:
            index = index%bus
        if waittime == index:
            addBusInTime.append(bus)
            addTime = addTime * bus
            #print(time, waittime, index, addBusInTime)
            break
        
        time = time + addTime
print(time)
        