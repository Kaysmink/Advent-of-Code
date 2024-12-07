import re
import itertools as it

Input = open("data/2024/dag 07. input.txt", "r").read().split("\n")[0:-1]

equations = [re.findall(r'\d+', line) for line in Input]


def check_possible_equations(line, part):
    operators = "+*" if part == 1 else "+*|"
    outcome, equation = line[0], line[1::]

    for possOperators in it.product(operators, repeat=len(equation)-1):
        result = equation[0]
        for index in range(len(possOperators)):
            if possOperators[index] == "|":
                result = result+equation[index+1]
            else:
                result = str(eval(result + possOperators[index] + equation[index+1]))
        if result == outcome:
            return int(outcome)

    return 0


print(sum([check_possible_equations(equation, 1) for equation in equations]))
