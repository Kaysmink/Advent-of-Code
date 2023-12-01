import copy

Input=open("data/Day 12. input.txt", "r").read().split("\n")[:-1]
Input = [[instruction[0], instruction[1::]] for instruction in Input]

newDirectionDict = {
        "R": {"NE": {"90": "ES", "180": "SW", "270": "WN"}, 
              "NW": {"90": "EN", "180": "SE", "270": "WS"}, 
              "SE": {"90": "WS", "180": "NW", "270": "EN"}, 
              "SW": {"90": "WN", "180": "NE", "270": "ES"}, 
              "EN": {"90": "SE", "180": "WS", "270": "NW"}, 
              "ES": {"90": "SW", "180": "WN", "270": "NE"}, 
              "WN": {"90": "NE", "180": "ES", "270": "SW"}, 
              "WS": {"90": "NW", "180": "EN", "270": "SE"}}, 
        "L": {"NE": {"90": "WN", "180": "SW", "270": "ES"}, 
              "NW": {"90": "WS", "180": "SE", "270": "EN"}, 
              "SE": {"90": "EN", "180": "NW", "270": "WS"}, 
              "SW": {"90": "ES", "180": "NE", "270": "WN"}, 
              "EN": {"90": "NW", "180": "WS", "270": "SE"}, 
              "ES": {"90": "NE", "180": "WN", "270": "SW"}, 
              "WN": {"90": "SW", "180": "ES", "270": "NE"}, 
              "WS": {"90": "SE", "180": "EN", "270": "NW"}}}

def executeInstruction1(instruction, value):
    global northSouth
    global eastWest
    global DirectionOfShip
    
    if instruction == "N":
      northSouth = northSouth + value
    if instruction == "S":
        northSouth = northSouth - value
    if instruction == "E":
        eastWest = eastWest + value
    if instruction == "W":
        eastWest = eastWest - value
    if instruction == "L":
        DirectionOfShip = DirectionOfShip - value
        if DirectionOfShip < 0:
            DirectionOfShip = DirectionOfShip + 360
    if instruction == "R":
        DirectionOfShip = DirectionOfShip + value
        if DirectionOfShip >= 360:
            DirectionOfShip = DirectionOfShip - 360
    if instruction == "F":
        if DirectionOfShip == 0:
            executeInstruction1("N", value)
        if DirectionOfShip == 90:
            executeInstruction1("E", value)
        if DirectionOfShip == 180:
            executeInstruction1("S", value)
        if DirectionOfShip == 270:
            executeInstruction1("W", value)

def newUnits(old, new):
    global waypointUnits     
    old = list(old) 
    new = list(new)
    
    waypointUnitsCopy = copy.deepcopy(waypointUnits)
    for i in range(0,2):
        if(old[i] in ["N", "S"]):
            if new[i] in ["E", "W"]:
               waypointUnits["EW"] = abs(waypointUnitsCopy["NS"])
        if(old[i] in ["E", "W"]):
            if new[i] in ["N", "S"]:
               waypointUnits["NS"] = abs(waypointUnitsCopy["EW"])  
               
def executeInstruction2(instruction, value):
    global waypointUnits
    global waypointDirection
    global location
    
    waypointDirectionCopy = waypointDirection
    if instruction == "N": 
        if "N" in list(waypointDirectionCopy):
            waypointUnits["NS"] = abs(waypointUnits["NS"] + value)
        else:
            if value > waypointUnits["NS"]:
                waypointDirection = waypointDirection.replace("S", "N")
            waypointUnits["NS"] = abs(waypointUnits["NS"] - value)
    if instruction == "S":
        if "S" in list(waypointDirectionCopy):
            waypointUnits["NS"] = waypointUnits["NS"] + value
        else:
            if value > waypointUnits["NS"]:
                waypointDirection = waypointDirection.replace("N", "S")
            waypointUnits["NS"] = abs(waypointUnits["NS"] - value)
    if instruction == "E":
        if "E" in list(waypointDirectionCopy):
            waypointUnits["EW"] = waypointUnits["EW"] + value
        else:
            if value > waypointUnits["EW"]:
                waypointDirection = waypointDirection.replace("W", "E")
            waypointUnits["EW"] = abs(waypointUnits["EW"] - value)
    if instruction == "W":
        if "W" in list(waypointDirectionCopy):
            waypointUnits["EW"] = waypointUnits["EW"] + value
        else: 
            if value > waypointUnits["EW"]:
                waypointDirection = waypointDirection.replace("E", "W")
            waypointUnits["EW"] = abs(waypointUnits["EW"] - value)
        
    if instruction in ["R", "L"]:
        oldDirections = waypointDirection
        waypointDirection = newDirectionDict[instruction][waypointDirection][str(value)] 
        newUnits(oldDirections, waypointDirection)   
        
    if instruction == "F":
        if "N" in waypointDirection: 
            location["NS"] = location["NS"] + (abs(waypointUnits["NS"]) * value) 
        if "S" in waypointDirection: 
            location["NS"] = location["NS"] - (abs(waypointUnits["NS"]) * value)
        if "E" in waypointDirection: 
            location["EW"] = location["EW"] + (abs(waypointUnits["EW"]) * value)
        if "W" in waypointDirection: 
            location["EW"] = location["EW"] - (abs(waypointUnits["EW"]) * value)

# set parameters deel 1
DirectionOfShip = 90
eastWest = 0 
northSouth = 0 

# set parameters deel 2 
location = {"NS": 0, "EW": 0}
waypointUnits = {"NS": 1, "EW": 10}
waypointDirection = "NE"

for instruction, value in Input:
    # deel 1 
    executeInstruction1(instruction, int(value))
    # deel 2
    executeInstruction2(instruction, int(value))
 
print(abs(eastWest) + abs(northSouth))
print(abs(location["NS"]) + abs(location["EW"]))
