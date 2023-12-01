Input = open("data/Day 22. input.txt", "r").read().split("\n\n")
player1 = list(map(int,Input[0].split("\n")[1::]))[::-1]
player2 = list(map(int,Input[1].split("\n")[1::][:-1]))[::-1]

def playGamePart1():
    global player1
    global player2
    
    card1 = player1.pop()
    card2 = player2.pop()
    if card1 > card2:
        result = [card2, card1]
        player1 = result + player1
    if card1 < card2:
        result = [card1, card2]
        player2 = result + player2

# Deel 1 
while len(player1) > 0 and len(player2) > 0:
    playGamePart1()

if len(player1) == 0:
    winner = player2
else:
    winner = player1
    
result = sum([(index+1)*value for index, value in enumerate(winner)])
print(result)

def playRecursive(deck1, deck2):
    deck1 = deck1.copy()
    deck2 = deck2.copy()
    
    player1Decks = []
    player2Decks = []
    
    while len(deck1) > 0 and len(deck2) > 0:
        if deck1 in player1Decks or deck2 in player2Decks:
            deck2 = list([])
        else:
            player1Decks.append(deck1.copy())
            player2Decks.append(deck2.copy())
        
            card1 = deck1.pop()
            card2 = deck2.pop()

            if card1 <= len(deck1) and card2 <= len(deck2):
                winner = playRecursive(deck1[len(deck1) - card1:len(deck1)], deck2[len(deck2) - card2:len(deck2)])
                if winner[0] == "player1":
                    result = [card2, card1]
                    deck1 = result + deck1
                else:
                    result = [card1, card2] 
                    deck2 = result + deck2
            else:
                if card1 > card2:
                    result = [card2, card1]
                    deck1 = result + deck1
                else:  
                    result = [card1, card2]
                    deck2 = result + deck2
                    
    if len(deck1) == 0:
        return ["player2", deck1, deck2]
    if len(deck2) == 0:
        return ["player1", deck1, deck2]
    
player1 = list(map(int,Input[0].split("\n")[1::]))[::-1]
player2 = list(map(int,Input[1].split("\n")[1::][:-1]))[::-1]  
winner, player1, player2 = playRecursive(player1, player2)
    
if len(player1) == 0:
    winner = player2
else:
    winner = player1
    
result2 = sum([(index+1)*value for index, value in enumerate(winner)])
print(result2)    
    
    

    
