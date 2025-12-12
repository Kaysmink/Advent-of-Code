import re
from scipy.optimize import linprog

Input = open("data/2025/dag 10. input.txt", "r").read().split("\n")[0:-1]
instructions = [re.findall(r"[.#]+|[\d+,]+", line) for line in Input]


def find_fewest_buttons(instruction):
    goal = tuple(value == "#" for value in instruction[0])
    buttons = [list(map(int,re.findall(r"\d+", line))) for line in instruction[1:-1]]

    seen = {tuple(False for value in goal)}
    current_states = {tuple(False for value in goal)}

    presses = 0
    while True:
        presses += 1
        new_states = set()
        for state in current_states:
            poss_states = [tuple([value if index not in button else not value for index, value in enumerate(state)]) for button in buttons]
            poss_states = [value for value in poss_states if value not in seen]

            seen.update(poss_states)
            new_states.update(poss_states)

        current_states = new_states

        if goal in current_states:
            return presses


def solve(instruction):
    buttons = [list(map(int, re.findall(r"\d+", line))) for line in instruction[1:-1]]
    goal = list(map(int, re.findall(r"\d+", instruction[-1])))

    c = [1] * len(buttons)

    A_eq = [[i in button for button in buttons] for i in range(len(goal))]
    bounds = [(0, None)] * len(buttons)

    return linprog(c, A_eq=A_eq, b_eq=goal, bounds=bounds, integrality=1).fun

part1 = sum([find_fewest_buttons(instruction) for instruction in instructions])
part2 = int(sum(solve(instruction) for instruction in instructions))

print(part1, part2)