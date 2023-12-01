import re 

Input = open("data/dag 05. input.txt", "r").read().split("\n\n")[1].split("\n")
procedures = [list(map(int,re.findall(r'\d+', line))) for line in Input][:-1]

# handmatig de start stacks in list gezet. Aangezien parsen meer tijd kost
stacks = [list(string) for string in ["HCR", "BJHLSF", "RMDHJTQ", "SGRHZBJ", "RPFZTDCB", "THCG", "SNVZBPWL", "RJQGC", "LDTRHPFS"]]

# Deel 1 
[[stacks[to-1].append(stacks[fro-1].pop()) for step in range(n)] for n, fro, to in procedures]
print("".join([stack[-1] for stack in stacks]))

# Deel 2
stacks = [list(string) for string in ["HCR", "BJHLSF", "RMDHJTQ", "SGRHZBJ", "RPFZTDCB", "THCG", "SNVZBPWL", "RJQGC", "LDTRHPFS"]]

for n, fro, to in procedures:
    popped = [] 
    for step in range(n):
        popped.append(stacks[fro-1].pop())
    popped = list("".join(popped)[::-1])
    stacks[to-1].extend(popped)
        
print("".join([stack[-1] for stack in stacks]))
