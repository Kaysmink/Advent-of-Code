from collections import defaultdict

Input = open("data/Day 24. input.txt", "r").read().split("\n")[:-1]

monadAlgo = [line.split(" ") for line in Input]

def runMonad(number):
    number = list(str(number)[::-1])
    values = defaultdict(int)
    
    for index, instruction in enumerate(monadAlgo):
        action, parameters = instruction[0], instruction[1::]
        
        if action == "inp":
            print(parameters[0])
            values[parameters[0]] = int(number.copy().pop())
            continue
        
        a,b = parameters.copy()
        if action == "add":
            values[a] = values[a] + int(b) if b.isnumeric() else values[a] + values[b]
        elif action == "mul":
            values[a] = values[a] * int(b) if b.isnumeric() else values[a] * values[b]
        elif action == "div":
            values[a] = int(values[a] / int(b)) if b.isnumeric() else int(values[a] / values[b])
        elif action == "mod":
            values[a] = values[a]%int(b) if b.isnumeric() else values[a]%values[b]
        elif action == "eql":
            if b.isnumeric():
                values[a] = 1 if values[a] == int(b) else 0
            else:
                values[a] = 1 if values[a] == values[b] else 0
                
    if values["z"] == 0:
        return True
    return False

number = 99999999999999
runMonad(number)