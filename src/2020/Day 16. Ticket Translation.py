from collections import defaultdict

Input=open("data/Day 16. input.txt", "r").read().split("\nnearby tickets:\n")

# parse Input
rules = Input[0].split("\n\nyour ticket:\n")[0].split("\n")
rulesDict = defaultdict(list)
for rule in rules:
        key = rule.split(":")[0]
        values = rule.split(": ")[1].split(" or ")
        
        for value in values:
            Min = int(value.split("-")[0])
            Max = int(value.split("-")[1])
            
            for number in range(Min, Max +1):
               rulesDict[key].append(number) 

yourTickets = list(map(int,Input[0].split("\n\nyour ticket:\n")[1].strip() .split(",")))  
nearbyTickets = [list(map(int, ticket.split(","))) for ticket in Input[1].split("\n")[:-1]]

# deel 1 
validNumbers = list(map(int,list(set(",".join(list(map(str,list(rulesDict.values())))).replace("[", " ").replace("]", " ").strip().split(", ")))))
unvalidTickets = defaultdict()

result1 = 0 
ticketNumber = 0
for ticket in nearbyTickets:    
    for number in ticket:
        if number not in validNumbers:
            result1 = result1 + number
            unvalidTickets[ticketNumber] = False
    ticketNumber = ticketNumber + 1
    
print(result1)

# deel 2 
ticketsToDiscard = list(unvalidTickets.keys())
validTickets = [ticket for index, ticket in enumerate(nearbyTickets) if index not in ticketsToDiscard]

indexDict = defaultdict(list)
for ticket in validTickets:
    for index, number in enumerate(ticket):
        indexDict[index].append(number)    

possibleFields = defaultdict(list)
for key, value in indexDict.items():
    for ruleKey, ruleValue in rulesDict.items():
        if(all(elem in ruleValue for elem in value)):
            possibleFields[ruleKey].append(key)

definitiveField = defaultdict()
while True: 
    delete = []
    for key, possibles in possibleFields.items():
        if len(possibles) == 1:
            definitiveField[key] = possibles[0]
            delete.append(possibles[0])
    for key, possibles in possibleFields.items():
        for values in delete:
            if values in possibleFields[key]:
                possibleFields[key].remove(values)
    if len(definitiveField.keys()) == len(possibleFields.keys()):
        break
    
result2 = 1
for key, value in definitiveField.items():
    if "departure" in key:
        result2 = result2 * yourTickets[value]

print(result2)  