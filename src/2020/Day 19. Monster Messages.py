from collections import defaultdict

Input=open("data/Day 19. input.txt", "r").read().split("\n\n")

def read_input(Input):
    rules = Input[0].split("\n")
    messages = Input[1].split("\n")[:-1]
    
    rulesDict = defaultdict(list)
    
    for rule in rules:
        ruleNumber = rule.split(": ")[0]
        ruleList = rule.split(": ")[1]
        rulesDict[ruleNumber] = ruleList
    return rulesDict, messages

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def remove_known():
    global rulesDict
    
    remove_keys = []
    for key, rule in rulesDict.items():
        #print(key, rule, has_numbers(rule))
        if has_numbers(rule) == False:
            remove_keys.append(key)
            knownRules[key] = "".join(rule.replace('"', '').split(" "))
            
    for key in remove_keys:
        del rulesDict[key]

def check_new_known():
    for ruleKey, ruleRule in rulesDict.items():
        for key, rule in knownRules.items():
            ruleRule = ruleRule.replace(key, rule)
            rulesDict[ruleKey] = ruleRule
            
            
knownRules = defaultdict()
rulesDict, messages = read_input(Input)    

while rulesDict:
    print(len(rulesDict))
    remove_known()
    check_new_known()


