Input = open("data/dag 02. input.txt", "r").read().split("\n")[:-1]
hands = [[values for values in line.split(" ")] for line in Input]

mappingOpponnents = {"A": "R", "B": "P", "C": "S"}
mappingHand = {"X": "R", "Y": "P", "Z": "S"}
mappingScore = {"R": 1, "P": 2, "S": 3}
winMap = {"R": "S", "P": "R", "S": "P"}
loseMap = {"R": "P", "P": "S", "S": "R"}

def score_hand(hand):
    score = 0 
    opp, u = hand[0], hand[1]
    
    score = score + mappingScore[u]
    if opp == u:
        score = score + 3
    elif winMap[u] == opp:
            score = score + 6
    
    return score 

def newHand(hand):
    opp = mappingOpponnents[hand[0]] 
    if hand[1] == "X":
        u = winMap[opp]
    elif hand[1] == "Z":
        u = loseMap[opp]
    else:
        u = opp
        
    return [opp, u]

# Deel 1 
handsPart1 = [[mappingOpponnents[hand[0]], mappingHand[hand[1]]] for hand in hands]
print(sum([score_hand(hand) for hand in handsPart1]))

# Deel 2
handsPart2 = [newHand(hand) for hand in hands]
print(sum([score_hand(hand) for hand in handsPart2]))
