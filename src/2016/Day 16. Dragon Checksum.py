Input = open("data/2016/dag 16. input.txt", "r").read().strip()

def generate_data(data, length):
    while len(data) < length:
        b = data[::-1]
        b = b.replace("1", "2").replace("0", "1").replace("2", "0")

        data = data + "0" + b

    return data

def checksum(data):
    bigrams = [data[i:i+2] for i in range(0, len(data) - 1, 2)]
    data = "".join(["1" if n1 == n2 else "0" for n1,n2 in bigrams])

    while len(data) % 2 == 0:
        bigrams = [data[i:i + 2] for i in range(0, len(data) - 1, 2)]
        data = "".join(["1" if n1 == n2 else "0" for n1, n2 in bigrams])

    return data

def run_program(length):
    data = generate_data(Input, length)

    return checksum(data[0:length])

part1 = run_program(272)
part2 = run_program(35651584)

print(part1, part2)