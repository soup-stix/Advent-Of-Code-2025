def getInput():
    with open(r"02\AOC_2_input.txt", "r") as f:
        ranges = [rangelimits.split("-") for rangelimits in f.read().split(",")]

    print(ranges)
    return ranges


def solution(ranges):
    ans = 0
    for start, end in ranges:
        for num in range(int(start), int(end)+1):
            niq = str(num)
            if len(niq)%2==0:
                print(niq, niq[0:(len(niq)//2)], niq[(len(niq)//2):])
                if niq[0:(len(niq)//2)] == niq[(len(niq)//2):]:
                    ans += num
    print(ans)

solution(getInput())
