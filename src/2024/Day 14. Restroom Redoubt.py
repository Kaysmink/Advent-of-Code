import re


Input = open("data/2024/dag 14. input.txt", "r").read().split("\n")[0:-1]
Input = [list(map(int, re.findall(r'[\d-]+', line))) for line in Input]
current_positions = [(x, y) for x, y, xn, yn in Input]
steps = [(xn, yn) for x, y, xn, yn in Input]


def do_step(position, step, sec):
    x, y = position
    xn, yn = step

    newX = (x + xn*sec) % maxX
    newY = (y + yn*sec) % maxY

    return (newX, newY)


def safety_factor(positions):
    q1 = len([(x, y) for x, y in positions if x < maxX//2 and y < maxY//2])
    q2 = len([(x, y) for x, y in positions if x > maxX//2 and y < maxY//2])
    q3 = len([(x, y) for x, y in positions if x < maxX//2 and y > maxY//2])
    q4 = len([(x, y) for x, y in positions if x > maxX//2 and y > maxY//2])

    return q1*q2*q3*q4


maxX = 101
maxY = 103

part1 = safety_factor([do_step(position, steps[index], 100) for index, position in enumerate(current_positions)])

# Part 2
sec = 1
minScore = 1000000000000000000000
while True:
    safety_score = safety_factor([do_step(position, steps[index], sec)
                                 for index, position in enumerate(current_positions)])

    if safety_score < minScore:
        minScore = safety_score
        part2 = sec

    if sec > 10000:
        break

    sec = sec + 1

print(part1, part2)
