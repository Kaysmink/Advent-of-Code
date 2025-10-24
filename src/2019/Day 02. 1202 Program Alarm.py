def run_program(noun, verb):
    Input = list(map(int, open("data/2019/dag 02. input.txt", "r").read().split(",")))
    Input[1] = noun
    Input[2] = verb

    values = {index:value for index, value in enumerate(Input)}

    while Input:
        opcode = Input.pop(0)
        if opcode == 99:
            break

        value1, value2, newIndex = [Input.pop(0), Input.pop(0), Input.pop(0)]

        if opcode == 1:
            values[newIndex] = values[value1]+values[value2]
        if opcode == 2:
            values[newIndex] = values[value1]*values[value2]
    return values[0]


part1 = run_program(12, 2)

results = [[noun, verb, run_program(noun, verb)] for noun in range(100) for verb in range(100)]
part2 = [100 * noun + verb for noun, verb, value in results if value == 19690720][0]

print(part1, part2)
