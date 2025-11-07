Input = list(open("data/2015/dag 03. input.txt", "r").read())

step_dict = {">": [1, 0],
             "<": [-1, 0],
             "^": [0, -1],
             "v": [0, 1]}


def walk(part):
    if part == 1:
        poss = (0,0)
        visited = [(0,0)]

        for direction in Input:
            x,y = poss
            xn, yn = step_dict[direction]
            poss = (x + xn, y + yn)
            visited.append(poss)

        return visited
    else:
        poss1 = poss2 = (0,0)
        visited = [(0,0)]

        while Input:
            dir1, dir2 = [Input.pop(0), Input.pop(0)]
            [x1,y1],[x2,y2] = poss1, poss2
            xn1, yn1 = step_dict[dir1]
            xn2, yn2 = step_dict[dir2]
            poss1 = (x1 + xn1, y1 + yn1)
            poss2 = (x2 + xn2, y2 + yn2)

            visited.extend([poss1, poss2])
        return visited

part1 = len(set(walk(1)))
part2 = len(set(walk(2)))

print(part1, part2)