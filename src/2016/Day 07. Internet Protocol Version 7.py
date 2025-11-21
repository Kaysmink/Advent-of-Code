import re
import regex

Input = open("data/2016/dag 07. input.txt", "r").read().split("\n")[0:-1]

def check_tls(part, ip):
    inside = re.findall(r"\[(.*?)\]", ip)
    for ins in inside:
        ip = ip.replace(f"[{ins}]", " ")
    outside = ip.split(" ")

    if part == 1:
        outside_match = any([re.findall(r"(.)(?!\1)(.)\2\1", out) for out in outside])
        inside_match = any([re.findall(r"(.)(?!\1)(.)\2\1", ins) for ins in inside])

        return outside_match and not inside_match
    if part == 2:
        outside_match = [value for sub in [regex.findall(r"([A-Za-z])(?!\1)([A-Za-z])\1", out, overlapped=True) for out in outside] for value in sub]
        inside_match = any([f"{c2}{c1}{c2}" in ins for ins in inside for c1, c2 in outside_match])

        return inside_match


part1 = sum([check_tls(1,ip) for ip in Input])
part2 = sum([check_tls(2,ip) for ip in Input])

print(part1, part2)