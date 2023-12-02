import regex as re
import pandas as pd
import numpy as np

Input = open("data/2023/dag 02. input.txt", "r").read().split("\n")[0:-1]

max_dict = {"red": 12, "green": 13, "blue": 14}

games_colours = [re.findall(r'[a-zA-Z]+', line)[1:] for line in Input]
games_values = [re.findall(r'\d+', line)[1:] for line in Input]

possible = [[int(games_values[y][x]) <= max_dict[colour]
             for x, colour in enumerate(game)] for y, game in enumerate(games_colours)]
part1 = sum([game_num+1 for game_num, game in enumerate(possible) if all(game)])

part2 = sum([np.prod(pd.DataFrame(list(map(int, games_values[y])), games_colours[y]).reset_index(
).groupby("index").max()[0].tolist()) for y, game in enumerate(games_colours)])
