def getInput():
    with open(r"03\AOC_3_input.txt", "r") as f:
        lines = f.read().splitlines()

    return lines

def solution():
    ans = 0
    lines = getInput()
    for line in lines:
        jolt = []
        line = list(map(int, list(str(line))))
        start = 0
        end = 12
        while end > 0:
            jolt.append(max(line[start:len(line)-end+1]))
            start = start + line[start:].index(max(line[start:len(line)-end+1]))+1
            end -= 1

        ans += (int("".join(list(map(str,jolt)))))
    print(ans)

solution()