Input = list(map(int,open("data/Day 06. input.txt", "r").read().split(",")))
timer = [Input.count(time) if time in Input else 0 for time in range(0,9)]

def getAnswer(maxDay, timer):
    for day in range(0,maxDay):
        newFishes = timer[0]
        
        timer = [timer[index+1] if index != 6 else timer[7] + timer[0] for index in range(0,8)]    
        timer.append(newFishes)
    
    print(sum(timer))
    
getAnswer(80, timer.copy())
getAnswer(256, timer.copy())