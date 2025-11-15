goal = int(open("data/2015/dag 20. input.txt", "r").read().strip())

def getDivs(N):
    factors = {1}
    maxP  = int(N**0.5)
    p,inc = 2,1
    while p <= maxP:
        while N%p==0:
            factors.update([f*p for f in factors])
            N //= p
            maxP = int(N**0.5)
        p,inc = p+inc,2
    if N>1:
        factors.update([f*N for f in factors])
    return sorted(factors)


house_number = 100000
part1 = 0
part2 = 0
while part1 == 0 or part2 == 0:
    divs = getDivs(house_number)
    presents_part1 = sum(divs)*10
    presents_part2 = sum([div for div in divs if house_number/div <= 50]) * 11

    if presents_part1 >= goal and part1 == 0:
        part1 = house_number
    if presents_part2 >= goal:
        part2 = house_number

    house_number = house_number + 1

print(part1, part2)
