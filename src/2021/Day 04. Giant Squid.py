drawnNumbers, cards = open("data/Day 04. input.txt", "r").read().split("\n\n", 1)
drawnNumbers = list(map(int, drawnNumbers.split(",")))

def checkRow(card):
    for row in card:
        if row.count("x") == 5:
            return True
    return False

def getColumn(card, col):
    return [row[col] for row in card]

def checkColumn(card):
    for i in range(0,len(card[0])):
        column = getColumn(card, i)
        if column.count("x") == 5:
            return True
    return False

def checkBingo(card):
    return True if True in [checkRow(card), checkColumn(card)] else False

def countNumbers(card):
    return sum([sum([number for number in row if number != "x"]) for row in card])

def playBingo(cards, part):
    for draw in drawnNumbers:
        cards = [[["x" if number == draw else number for number in row] for row in card] for card in cards]
        bingo = [checkBingo(card) for card in cards]
        
        if part == "part1":
            if True in bingo:
                bingoCard = bingo.index(True)
                print(countNumbers(cards[bingoCard]) * draw)
                break
        
        if part == "part2":
            if True in bingo:
                bingoCard = [index for index,value in enumerate(bingo) if value == True]
                
                if len(cards) == 1:
                    print(countNumbers(cards[bingoCard[0]]) * draw)
                    break 
                
                for index in sorted(bingoCard, reverse=True):
                    del cards[index]
                        
    return cards, draw
            
cards = [[number.split(" ") for number in card.split("\n")] for card in cards.split("\n\n")]
cards = [[[int(number) for number in row if number != ""] for row in card] for card in cards]
       
playBingo(cards, "part1")
playBingo(cards, "part2")
