Input=open("data/Day 18. input.txt", "r").read().split("\n")[:-1]
Tokenizer = [line.replace("(", "( ").replace(")", " )") for line in Input]
Tokenizer = [line.split(" ") for line in Tokenizer]

operators = ["+", "*"]

# voor deel1 beide op 0, voor deel2 PLUS hoger dan KEER
operatorPrecedence = {"+": 1, 
                      "*": 0}

def ShuntingYard(opdracht):
    resultList = []
    operatorList = []
    for token in opdracht:
        if token.isnumeric():
            resultList.append(token)
        elif token in operators:
            while len(operatorList) > 0 and operatorList[-1] is not "(" and operatorPrecedence[operatorList[-1]] >= operatorPrecedence[token]:
                resultList.append(operatorList.pop())
            operatorList.append(token)
        elif token == "(":
            operatorList.append(token)
        elif token == ")":
            while len(operatorList) > 0 and operatorList[-1] is not "(":
                resultList.append(operatorList.pop())
            if len(operatorList) > 0:
                operatorList.pop()
    while len(operatorList) > 0:
        resultList.append(operatorList.pop())

    return list(resultList)

def RPN(opdracht):
    resultList =[]
    for token in opdracht:
        if token.isnumeric():
            resultList.append(int(token))
        elif token in operators:
            number1 = resultList.pop()
            number2 = resultList.pop()
            resultList.append(performOperation(token, number1, number2))
    return int(resultList[0])

def performOperation(operator, number1, number2):
    if operator == "*":
        return number1 * number2
    if operator == "+":
        return number1 + number2
    
result = 0
for opdracht in Tokenizer:
    result = result + RPN(ShuntingYard(opdracht))

print(result)