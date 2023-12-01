# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 14:35:16 2021

@author: kaysm
"""

Input = int(open("data/day 14. input.txt", "r").read())

scores = "37"
current_index = [0,1]
currentRecipes = [int(scores[index]) for index in current_index]
part1 = True
while True:   
    currentRecipes = [int(scores[index]) for index in current_index]
    newRecipe = sum(currentRecipes)

    scores = scores + str(newRecipe)    
    
    steps_forward = [1 + currentRecipes[x] for x in range(2)]
    new_index = [index%len(scores) + current_index[x] for x, index in enumerate(steps_forward)]
    new_index = [index if index  < len(scores) else index-len(scores) for index in new_index]
    current_index = new_index
    
    # Deel 1 
    if len(scores) >= Input + 10 and part1 == True:
        print(scores[Input:Input+10])
        part1 = False
        
    # deel 2
    if str(Input) in scores[-10::]:
        print(len(scores.split(str(Input))[0]))
        break
    

