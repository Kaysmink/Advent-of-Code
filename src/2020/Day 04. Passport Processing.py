import collections as co
import re

Input=open("data/Day 04. input.txt", "r").read().split("\n\n")

all_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"] 

valid1 = 0
valid2 = 0 
for paspoort in Input: 
    fields = re.split(" |\n", paspoort)
    if "" in fields: 
        fields.remove("")
    
    fieldsDict = co.defaultdict()
    for pair in fields:
        pair = pair.split(":")
        fieldsDict[pair[0]]=pair[1]
    
    # deel 1 
    alle_aanwezig = True
    for field in all_fields:
        if field not in fieldsDict.keys():
            if(field == "cid"):
                continue
            alle_aanwezig = False
    
    if alle_aanwezig == True: 
        valid1 = valid1 + 1
    
        # deel 2
        all_true = True
        # check byr
        if fieldsDict["byr"].isnumeric() == False:
            all_true = False
        else:
            if(int(fieldsDict["byr"]) < 1920 or int(fieldsDict["byr"]) > 2002):
                all_true = False
        
        # check iyr
        if fieldsDict["iyr"].isnumeric() == False:
            all_true = False
        else:
            if(int(fieldsDict["iyr"]) < 2010 or int(fieldsDict["iyr"]) > 2020):
                all_true = False
                
        # check eyr
        if fieldsDict["eyr"].isnumeric() == False:
            all_true = False
        else:
            if(int(fieldsDict["eyr"]) < 2020 or int(fieldsDict["eyr"]) > 2030):
                all_true = False
        
        # check hgt
        if "cm" in fieldsDict["hgt"]: 
            number = fieldsDict["hgt"].replace("cm", "")
            if number.isnumeric() == False:
                all_true = False
            else: 
                if(int(number) < 150 or int(number) > 193):
                    all_true = False
        if "in" in fieldsDict["hgt"]: 
            number = fieldsDict["hgt"].replace("in", "")
            if number.isnumeric() == False:
                all_true = False
            else: 
                if(int(number) < 59 or int(number) > 76):
                    all_true = False
        if "in" not in fieldsDict["hgt"] and "cm" not in fieldsDict["hgt"]:
            all_true = False
        
        # check hcl
        if fieldsDict["hcl"][0] != "#":
            all_true = False
        else: 
            waarde = fieldsDict["hcl"].replace("#", "")
            if bool(re.match("^[a-z0-9]{6}$", waarde.strip())):
                None
            else:
                all_true = False
        
        # check ecl
        if fieldsDict["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            all_true = False
        
        # check pid
        if bool(re.match("[0-9]{9}$", fieldsDict["pid"].strip())):
            None
        else: 
           all_true = False 
        
        if all_true == True:
            valid2 = valid2 + 1
                
print(valid1)
print(valid2)
    
    
    
