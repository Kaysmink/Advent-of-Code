from collections import deque

Input = int(open("data/2017/dag 17. input.txt", "r").read().strip())

def insert_values(steps, max_number, part):
    buffer = deque([0])

    for number in range(1,max_number+1):
        buffer.rotate(-steps)
        buffer.insert(1,number)
        buffer.rotate(-1)

    if part == 1:
        buffer.rotate(-buffer.index(max_number))
    else:
        buffer.rotate(-buffer.index(0))

    return buffer[1]

part1 = insert_values(Input, 2017,1)
part2 = insert_values(Input, 50000000,2)

print(part1, part2)
