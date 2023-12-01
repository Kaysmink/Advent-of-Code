Input = open("data/dag 10. input.txt", "r").read().split("\n")[:-1]
instructions = [line.split() for line in Input]

def check_cycleNum():
    if cycleNum in [20,60,100,140,180, 220]:
        X_on_cyleNum.append(X * cycleNum)


def check_pixel():
    row, colum = divmod(cycleNum,40)
    if cycleNum%40 == 0:
        row = row - 1
        colum = 40
    
    if colum-1 in sprite:
        pixels[row][colum-1] = "X"      
    else: 
        pixels[row][colum-1] = "."
        

X = 1
cycleNum = 0
X_on_cyleNum = []
sprite = [0,1,2]
pixels = [["" for i in range(40)] for j in range(6)]

for instruction in instructions:
    if instruction[0] == "noop":
        cycleNum = cycleNum + 1
        check_cycleNum()
        check_pixel()
    else: 
        for num in range(2):
            cycleNum = cycleNum + 1
            check_cycleNum()
            check_pixel()
        X = X + int(instruction[1])    
        sprite = [X-1,X,X+1]
        
print(sum(X_on_cyleNum))

for line in pixels:
    print("".join(line))
