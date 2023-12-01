Input=open("data/Day 02. input.txt", "r").read().split("\n")[:-1]

valid1 = 0
valid2 = 0

for line in Input:
    line = line.split(":")
    voorwaarden = line[0].split(" ")
    letter = voorwaarden[1]
    Min = int(voorwaarden[0].split("-")[0])
    Max = int(voorwaarden[0].split("-")[1])
    tekst = line[1].strip()
    
    # deel 1 
    if Min <= tekst.count(letter) <= Max:
        valid1 = valid1 + 1
    
    # deel 2 
    if (tekst[Min -1] == letter) is not (tekst[Max -1] == letter):
        valid2 = valid2 + 1

print(valid1)
print(valid2)