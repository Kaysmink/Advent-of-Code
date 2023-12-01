from collections import defaultdict
from collections import Counter

Input=open("data/day 04. input.txt", "r").read().split("\n")[:-1]
chronolog = sorted(Input)

guardsSleeping = defaultdict(list)
for event in chronolog:
    date, time, event = event.split(" ", 2)
    if event.startswith("Guard"):
        guard = event.split(" ")[1][1:]
    if event == "falls asleep":
        sleepTime = time[3:5]
    if event == "wakes up":
        wakeupTime = time[3:5]
        minutesAsleep = list(range(int(sleepTime), int(wakeupTime)))
        guardsSleeping[guard].extend(minutesAsleep)

# deel 1 
mostSleepGuard = max(guardsSleeping, key= lambda x: len(guardsSleeping[x]))
mostCommonMinute = [value for value, amount in Counter(guardsSleeping[mostSleepGuard]).most_common(1)][0]

print(int(mostSleepGuard) * mostCommonMinute)

# deel 2
maxMinute = 0
for guard, sleepingMinutes in guardsSleeping.items():
        minute, amount = [[value, amount] for value, amount in Counter(guardsSleeping[guard]).most_common(1)][0]
        if amount > maxMinute:
            chosenGuard = guard 
            chosenMinute = minute
            maxMinute = amount
            
print(int(chosenGuard) * chosenMinute)
