Input = open("data/2024/dag 02. input.txt", "r").read().split("\n")[0:-1]
reports = [list(map(int, line.split())) for line in Input]


def check_report(report):
    changes = [report[x] - report[x - 1] for x in range(1, len(report))]
    return min([not (min(changes) < 0 < max(changes)),
                max(changes) <= 3,
                min(changes) >= -3,
                0 not in changes])


part1 = sum([check_report(report) for report in reports])
part2 = sum([max([check_report([value for index, value in enumerate(report) if index != x])
                  for x in range(len(report))]) for report in reports])

print(part1, part2)
