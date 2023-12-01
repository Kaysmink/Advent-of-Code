from collections import defaultdict, deque

Input=open("data/day 09. input.txt", "r").read().split("\n")[0]

numOfPlayers = int(Input.split(";")[0].split(" ")[0])
maxWorth = int(Input.split("; ")[1].split(" ")[4])


def play(numOfPlayers, maxWorth):
    scores = defaultdict(int)
    circle = deque([0])
    for turn in range(1, maxWorth + 1): 
        player = turn%numOfPlayers if turn%numOfPlayers != 0 else numOfPlayers
        
        if turn%23 == 0:  
            circle.rotate(7)
            scores[player] = scores[player] + turn + circle.pop()
            circle.rotate(-1)
        
        else:
            circle.rotate(-1)
            circle.append(turn)
    return max(scores.values())
    
print(play(numOfPlayers, maxWorth))
print(play(numOfPlayers, maxWorth*100))