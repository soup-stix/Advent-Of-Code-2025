import re

def getInput():
    with open(r"02\AOC_2_input.txt", "r") as f:
        ranges = [rangelimits.split("-") for rangelimits in f.read().split(",")]

    print(ranges)
    return ranges


def solution(ranges):
    ans = 0
    re_match = re.compile(r'^(\d+)\1+$')
    for start, end in ranges:
        for num in range(int(start), int(end)+1):
            if re_match.fullmatch(str(num)):
                ans += num
    print(ans)

solution(getInput())
