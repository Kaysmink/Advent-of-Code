Input = open("data/2017/dag 21. input.txt", "r").read().split("\n")[0:-1]
patterns = [line.split(" => ") for line in Input]
replace_pattern = {l1:l2 for l1, l2 in patterns}

grid = [".#.","..#","###"]

def split_grid(grid, dim, block_size):
    blocks = [[None for _ in range(dim)] for _ in range(dim)]

    for br in range(dim):
        for bc in range(dim):
            block = [
                grid[r][bc * block_size:(bc + 1) * block_size]
                for r in range(br * block_size, (br + 1) * block_size)
            ]
            blocks[br][bc] = block

    return blocks

def rotate(block):
    return [''.join(row) for row in zip(*block[::-1])]

def flip_horizontal(block):
    return [row[::-1] for row in block]

def find_variations(block):
    results = set()

    for _ in range(4):
        results.add(tuple(block))
        results.add(tuple(flip_horizontal(block)))
        block = rotate(block)

    return ["/".join(list(r)) for r in results]

def find_replacements(block):
    return [replace_pattern[pattern] for pattern in find_variations(block) if pattern in replace_pattern][0].split("/")

def merge_blocks(grid, dim, size):
    return [''.join(grid[br][bc][r] for bc in range(dim)) for br in range(dim) for r in range(size+1)]

def enhance_grid(grid, iterations):
    for it in range(iterations):
        if it == 5:
            part1 = sum([line.count("#") for line in grid])

        block_size = 2 if len(grid)%2 == 0 else 3
        dim = len(grid) // block_size

        blocks = split_grid(grid, dim, block_size)
        new_blocks = [[find_replacements(blocks[y][x]) for x in range(dim)] for y in range(dim)]
        grid = merge_blocks(new_blocks, dim, block_size)

    return part1, sum([line.count("#") for line in grid])

part1, part2 = enhance_grid(grid, 18)

print(part1, part2)