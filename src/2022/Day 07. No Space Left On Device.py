from collections import defaultdict

Input = open("data/dag 07. input.txt", "r").read().split("\n")[:-1]

def run_command():
    global lineNumber
    global filesInDirectories
    global cwd

    command = Input[lineNumber].strip().split(" ")[1]
    if command == "cd":
        folder = Input[lineNumber].strip().split(" ")[2].strip()
        if folder == "..":
            cwd = "//".join(cwd.split("//")[0:-1])
            if cwd.replace("/", "") == "":
                cwd = "//"
        elif folder == "/":
            cwd = "//"
        else:
            cwd = cwd + "//" + folder

    if command == "ls":
        lineNumber = lineNumber + 1
        while not Input[lineNumber].startswith("$"):
            line = Input[lineNumber].split(" ")
            if line[0].isnumeric():
                filesInDirectories[cwd].append(int(line[0]))
            lineNumber = lineNumber + 1
            if lineNumber == len(Input):
                break
        lineNumber = lineNumber - 1
 

def add_value(value, folder):
    sizeDict[folder] = sizeDict[folder] + value
    while True:
        folder = "//".join(folder.split("//")[0:-1])
        if folder == "":
            break
        else:
            sizeDict[folder] = sizeDict[folder] + value
     
            
filesInDirectories = defaultdict(list)
lineNumber = 0
cwd = "//"

while lineNumber < len(Input):
    if lineNumber == 0:
        lineNumber = lineNumber + 1
        continue
    
    line = Input[lineNumber]
    if line.startswith("$"):
        run_command()
        
    lineNumber = lineNumber + 1

# Deel 1
sizeDict = defaultdict(int)
for folder, values in filesInDirectories.items():
    for value in values:
        add_value(value, folder)

print(sum([SOM for SOM in sizeDict.values() if SOM <= 100000]))

# Deel 2
needed = 30000000 - (70000000 - sizeDict["//"])
print(sorted([value for folder, value in sizeDict.items() if value >= needed])[0])
