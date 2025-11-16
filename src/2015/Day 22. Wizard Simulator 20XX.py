import re
from functools import cache

hitpoints_boss, damage_boss = list(map(int,re.findall(r"\d+", open("data/2015/dag 22. input.txt", "r").read())))
spells = {"Missile":[53,4,0,0], "Drain":[73,2,2,0], "Shield":[113,0,0,6], "Poison":[173,0,0,6], "Recharge":[229,0,0,5]}


def timer_spells(mana, hitpoints_b ,timer_s, timer_p, timer_r):
    if timer_s > 0:
        armor = 7
        timer_s = timer_s - 1
    else:
        armor = 0

    if timer_p > 0:
        hitpoints_b = hitpoints_b - 3
        timer_p = timer_p - 1
    if timer_r > 0:
        mana = mana + 101
        timer_r = timer_r - 1

    return timer_s, timer_p, timer_r, armor, hitpoints_b, mana

@cache
def fight(part, state):
    global result
    mana_spend, mana, hitpoints_p, hitpoints_b ,timer_s, timer_p, timer_r = state

    if part == 2:
        hitpoints_p = hitpoints_p - 1
        if hitpoints_p <=0:
            results.append((mana_spend, False))
            return False

    # calculate all new states which are affected by the timer spells
    timer_s, timer_p, timer_r, armor, hitpoints_b, mana = timer_spells(mana, hitpoints_b ,timer_s, timer_p, timer_r)

    if hitpoints_b <=0:
        results.append((mana_spend, True))
        return True

    if mana < 53:
        results.append((mana_spend, False))
        return False

    for spell, (cost,damage,heal,timer) in spells.items():
        if (spell == "Shield" and timer_s >0) or (spell == "Poison" and timer_p > 0) or (spell == "Recharge" and timer_r > 0) or (mana < cost):
            continue

        new_mana_spend = mana_spend + cost
        new_mana = mana - cost

        new_hitpoints_b = hitpoints_b - damage if timer == 0 else hitpoints_b
        new_hitpoints_p = hitpoints_p + heal if timer == 0 else hitpoints_p

        new_timer_s = timer if spell == "Shield" else timer_s
        new_timer_p = timer if spell == "Poison" else timer_p
        new_timer_r = timer if spell == "Recharge" else timer_r

        if new_hitpoints_b <= 0:
            results.append((new_mana_spend, True))
            continue

        # Bosses turn
        new_timer_s, new_timer_p, new_timer_r, armor, new_hitpoints_b, new_mana = timer_spells(new_mana, new_hitpoints_b, new_timer_s,
                                                                                        new_timer_p, new_timer_r)

        if new_hitpoints_b <= 0:
            results.append((new_mana_spend, True))
            continue

        new_hitpoints_p = new_hitpoints_p - max(damage_boss - armor,1)

        if new_hitpoints_p <= 0:
            results.append((new_mana_spend, False))
            continue

        fight(part,(new_mana_spend, new_mana, new_hitpoints_p, new_hitpoints_b, new_timer_s, new_timer_p, new_timer_r))


state = (0,500,50,hitpoints_boss,0,0,0)

results = []
fight(1,state)
part1 = min([cost for cost,winner in results if winner])

results = []
fight(2,state)
part2 = min([cost for cost,winner in results if winner])

print(part1, part2)