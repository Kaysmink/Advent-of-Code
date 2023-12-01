from collections import defaultdict
Input=open("data/Day 01. input.txt", "r").read().split("\n")[:-1]
Input = list(map(int, Input))

# deel 1
print(sum(Input))

# deel 2 
freq = 0 
freqList = defaultdict()
freqList[0] = True

found = False
while found is False:
    for value in Input: 
        freq = freq + value 
        if freq in freqList.keys():
            print(freq)
            found = True
            break
        else: 
            freqList[freq] = True