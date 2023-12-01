from collections import deque

Input = list(map(int,open("data/dag 20. input.txt", "r").read().split("\n")[:-1]))


def decrypt(Input, numOfIterations):
    arrangement = deque([(index, value) for index, value in enumerate(Input)])

    for iteration in range(numOfIterations):
        step = 0
        while True:
            index_first = [index for index, value in arrangement]
            if step not in index_first:
                break
            else:
                index_first = index_first.index(step)
                arrangement.rotate(-index_first)
                value = arrangement.popleft()
                arrangement.rotate(-value[1])
                arrangement.insert(0,(step, value[1]))
            step = step + 1
    return arrangement


def score(arrangement):
    idxZero = [value for step, value in arrangement].index(0)
    arrangement.rotate(-idxZero)
    result = 0

    for x in range(3):
        arrangement.rotate(-1000)
        value = arrangement[0][1]
        result = result + value
    print(result)


# Deel 1
arrangement = decrypt(Input, 1)
score(arrangement)

# Deel 2
Input = [value * 811589153 for value in Input]
arrangement = decrypt(Input, 10)
score(arrangement)