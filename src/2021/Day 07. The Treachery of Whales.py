import statistics

Input = list(map(int,open("data/Day 07. input.txt", "r").read().split(",")))

print(int(sum([abs(number-statistics.median(Input)) for number in Input])))

poss1 = sum([sum(range(1,abs(number-(int(statistics.mean(Input))+1))+1)) for number in Input])
poss2 = sum([sum(range(1,abs(number-(int(statistics.mean(Input))))+1)) for number in Input])

print(min(poss1, poss2))