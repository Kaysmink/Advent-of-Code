import re

from sympy import symbols, Eq, solve

Input = open("data/2024/dag 13. input.txt", "r").read().split("\n\n")
games = [list(map(int, re.findall(r'\d+', line))) for line in Input]


def play_game(game, part):
    xIncA, yIncA, xIncB, yIncB, xGoal, yGoal = game
    if part == 2:
        xGoal, yGoal = xGoal + 10000000000000, yGoal + 10000000000000

    A, B = symbols('A,B')

    eq1 = Eq((xIncA * A + xIncB * B), xGoal)
    eq2 = Eq((yIncA * A + yIncB * B), yGoal)

    answer = solve((eq1, eq2), (A, B))

    if all([float(eval(str(ans))).is_integer() for ans in answer.values()]):
        return answer.values()
    else:
        return [0, 0]


result = [play_game(game, 2) for game in games]
result = sum([A * 3 + B for A, B in result])

print(result)
