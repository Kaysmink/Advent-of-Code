from itertools import groupby

Input = list(open("data/2024/dag 09. input.txt", "r").read())[0:-1]

emptyPlaces = [int(value) for index, value in enumerate(Input) if index % 2 == 1]
ids = [[index // 2] * int(value) for index, value in enumerate(Input) if index % 2 == 0]


def file_fragmentation_part1(ids, emptyPlaces):
    file = []
    index = 0
    numIds = sum(list(map(int, Input))) - sum(emptyPlaces)

    while emptyPlaces:
        nids = len([value for sub in file for value in sub])
        if nids == numIds:
            break
        n = emptyPlaces.pop(0)
        fill = []
        for _ in range(n):
            if len(ids[-1]) == 0:
                ids.pop()
            fill.append(ids[-1].pop())
        if index < len(ids):
            file.append(ids[index])

        file.append(fill)
        index = index + 1

    file = [value for sub in file for value in sub]
    return file


file1 = file_fragmentation_part1(ids, emptyPlaces)
part1 = sum([value * index for index, value in enumerate(file1)])


def file_fragmentation_part2(file):
    for idNum in range(len(ids) - 1, 0, -1):
        nID = len(ids[idNum])

        current_index = (list(g) for key, g in groupby(enumerate(file), lambda t: t[1]) if key == idNum)
        current_index = min([(g[0][0]) for g in current_index if len(g) >= nID])

        new_index = (list(g) for key, g in groupby(enumerate(file), lambda t: t[1]) if key == ".")
        new_index = [(g[0][0]) for g in new_index if len(g) >= nID]

        if new_index:
            new_index = min(new_index)
            if new_index < current_index:
                for index in range(new_index, new_index + nID):
                    file[index] = idNum
                for index in range(current_index, current_index + nID):
                    file[index] = "."

    return file


emptyPlaces = [int(value) for index, value in enumerate(Input) if index % 2 == 1]
ids = [[index // 2] * int(value) for index, value in enumerate(Input) if index % 2 == 0]

file2 = [ids[index] + ["."] * emptyPlaces[index] for index in range(len(ids) - 1)] + [ids[-1]]
file2 = [value for sub in file2 for value in sub]
file2 = file_fragmentation_part2(file2)
part2 = sum([int(value) * index for index, value in enumerate(file2) if value != "."])

print(part1, part2)
