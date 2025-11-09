import re

Input = open("data/2015/dag 14. input.txt", "r").read().split("\n")[0:-1]
instructions = [re.findall(r"([a-zA-z]+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)[0] for line in Input]

possibilities = {reindeer:[int(speed), int(time), int(rest)] for reindeer, speed, time, rest in instructions}
current_state = {reindeer:["active", 0] for reindeer, speed, time, rest in instructions}
distances = {reindeer:0 for reindeer, speed, time, rest in instructions}
points = {reindeer:0 for reindeer, speed, time, rest in instructions}

def run_second():
    for reindeer, [speed, time, rest] in possibilities.items():
        state, state_time = current_state[reindeer]

        if state == "active":
            if state_time < time:
                distances[reindeer] = distances[reindeer] + speed
                current_state[reindeer] = ["active", state_time + 1]
            if state_time == time:
                current_state[reindeer] = ["rest", 1]
        if state == "rest":
            if state_time < rest:
                current_state[reindeer] = ["rest", state_time + 1]
            if state_time == rest:
                distances[reindeer] = distances[reindeer] + speed
                current_state[reindeer] = ["active", 1]


def give_points():
    winners = [key for key, distance in distances.items() if distance == max(distances.values())]

    for winner in winners:
        points[winner] = points[winner] + 1


for second in range(2503):
    run_second()
    give_points()

part1 = max(distances.values())
part2 = max(points.values())

print(part1, part2)

