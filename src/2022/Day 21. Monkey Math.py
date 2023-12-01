from sympy import symbols

Input = open("data/dag 21. input.txt", "r").read().split("\n")[:-1]
operations = [line.split(":") for line in Input]
operations = dict([(key, value) for key, value in operations])

def equation(key):
    equation = operations[key]
    while True:
        equation = equation.split(" ")
        for index, word in enumerate(equation):
            if word in operations.keys():
                equation[index] = "( " + operations[word] + " )"
        length = [len(word) < 4 or word.isnumeric() for word in equation]
        equation = " ".join(equation)
        
        if all(length):
            return equation

 
# Deel 1
result = equation("root")
print(int(eval(result)))

# Deel 2
operations["humn"] = "X"
result1 = equation("jsrw")
result2 = equation("ptvl")

eq = result1 + " - " + result2
X = symbols("X")

eval(eq)
# 46106821067730.9 - 7.49512987012987*X
# humm = 1 --> result1 = 53720282808016
# (53720282808016 - result2) / 7.49512987012987 = 3617613952376  --> answer is around this value

result2 = eval(result2)
for x in range(3617613952376-1000, 3617613952376+1000):
    new = result1.replace("X", str(x))
    new = eval(new)
    if new == result2:
        print(x)
        break