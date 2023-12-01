Input = open("data/dag 06. input.txt", "r").read()

print([len(set(pair)) == 4 for pair in [Input[i-3:i+1] for i in range(3,len(Input))]].index(True) + 4)
print([len(set(pair)) == 14 for pair in [Input[i-13:i+1] for i in range(13,len(Input))]].index(True) + 14)