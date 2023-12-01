Input= open("data/Day 21. input.txt", "r").read().split("\n")[:-1]

playerIndex = list(map(int,[line[-1] for line in Input]))
#playerIndex = [4,8]
playerIndex = [index -1 for index in playerIndex]

def playGamePart1():
    turn = 0 
    playboard = [1,2,3,4,5,6,7,8,9,10]
    scores = [0,0]
    draw = 0
    while True:
        for player in [0,1]:
            turn = turn +3
            drawNumbers = [draw+1, draw+2, draw+3]
            drawNumbers = [draw%100 if draw >=100 else draw for draw in drawNumbers]
            steps = sum(drawNumbers)
            newPos = playerIndex[player] + steps if playerIndex[player] + steps <=9 else (playerIndex[player] + steps)%10
            valueAdPos = playboard[newPos]
            
            draw = drawNumbers[-1]
            scores[player] = scores[player] + valueAdPos
            playerIndex[player] = newPos
            
            if scores[player] >= 1000:
                return [scores, turn]
        
scores, numOfTurns = playGamePart1()
print(min(scores) * numOfTurns)

playboard = [1,2,3,4,5,6,7,8,9,10]
wins = [0,0]
def playGame(scores, playerIndex):
    while True:
        for player in [0,1]:
              possDraw = [1,2,3]
              for draw in possDraw:
                  newPos = playerIndex[player] + draw if playerIndex[player] + draw <=9 else (playerIndex[player] + draw)%10
                  valueAdPos = playboard[newPos]
                  scores[player] = scores[player] + valueAdPos
                  playerIndex[player] = newPos
                  
                  if scores[player] >= 21:
                      print(scores)
                      wins[player] = wins[player] + 1
                      return player
                  
                  playGame(scores.copy(), playerIndex.copy())


playerIndex = list(map(int,[line[-1] for line in Input]))
playerIndex = [index -1 for index in playerIndex]

playGame([0,0], playerIndex)