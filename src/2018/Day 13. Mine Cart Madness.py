# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 11:39:08 2021

@author: kaysm
"""

from collections import defaultdict 

Input = open("data/day 13. input.txt", "r").read().split("\n")[:-1]
Input = [list(line) for line in Input]

numOfTurns = defaultdict(int)

turnDirection = {"/,>" : "^", 
                 "/,<" : "v", 
                 "/,^" : ">", 
                 "/,v" : "<", 
                 "\,>" : "v", 
                 "\,<" : "^", 
                 "\,^" : "<", 
                 "\,v" : ">"}

turn_intersection = {"<,0" : "v", 
                     "<,1" : "<", 
                     "<,2" : "^", 
                     ">,0" : "^", 
                     ">,1" : ">",
                     ">,2" : "v", 
                     "^,0" : "<", 
                     "^,1" : "^",
                     "^,2" : ">", 
                     "v,0" : ">", 
                     "v,1" : "v",
                     "v,2" : "<"}


def find_first_positions():
    positions = []
    cart_id = 1
    for rowNum, line in enumerate(Input):
        for charNum, coord in enumerate(line):
            if coord in ["<", ">"]:
                positions.append([rowNum, charNum, coord, cart_id])
                Input[rowNum][charNum] = "-"
                numOfTurns[cart_id] = 0 
                cart_id = cart_id + 1
            if coord in ["v", "^"]:
                positions.append([rowNum, charNum, coord, cart_id])
                Input[rowNum][charNum] = "|"
                numOfTurns[cart_id] = 0
                cart_id = cart_id + 1
                
    return positions

def check_new_direction(rowNum, x, direction, cart_id):
    coord = Input[rowNum][x]
    
    directComb = coord + "," + direction
    if directComb in turnDirection.keys():
        new_direction = turnDirection[directComb]
        return new_direction
    
    if coord == "+":
        turnNumber = numOfTurns[cart_id]%3
        intersectionComb = direction + "," + str(turnNumber)
        new_direction = turn_intersection[intersectionComb]
        numOfTurns[cart_id] +=1
        return new_direction
    
    return direction

def move_cart(cart):
    rowNum, x, direction, cart_id = cart
    
    if direction == "<":
        x = x - 1
    if direction == ">":
        x = x + 1
    if direction == "v":
        rowNum = rowNum + 1
    if direction == "^":
        rowNum = rowNum - 1   
        
    direction = check_new_direction(rowNum, x, direction, cart_id)
    
    return [rowNum, x, direction, cart_id]

def check_collision(positions):
    cartPositions = [str(x) + "," + str(rowNum) for rowNum, x, direction, cart_id in positions]
    crashCoord = set([position for position in cartPositions if cartPositions.count(position) > 1])

    cart_ids = [cart[3] for cart in positions if str(cart[1]) + "," + str(cart[0]) in crashCoord]
    
    if crashCoord:
        return crashCoord, cart_ids
    return False

def remove_crashed_carts(ids, positions):
    new_positions = [[rowNum, x, direction, cart_id] for [rowNum, x, direction, cart_id] in positions if cart_id not in ids]

    return new_positions
    
def tick():
    global firstCrash
    new_positions = positions.copy()
    for cart in positions:
        if cart not in new_positions:
            continue
        
        new_positions.remove(cart)
        new_position = move_cart(cart)
        new_positions.append(new_position)
        
        crash = check_collision(new_positions)
        if crash != False:
            new_positions = remove_crashed_carts(crash[1], new_positions) 
            if firstCrash:
                print(crash[0])
                firstCrash = False
                    
    return new_positions

# Deel 1 en Deel 2  
positions = find_first_positions()
firstCrash = True

while len(positions) != 1:
    positions = tick() 
    positions = sorted(positions) 

print(str(positions[0][1]) + "," +  str(positions[0][0])) 


