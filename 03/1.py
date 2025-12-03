
def getInput():
    with open(r"03\AOC_3_input.txt", "r") as f:
        lines = f.read().splitlines()

    return lines

def solution():
    ans = 0
    lines = getInput()
    for line in lines:
        line = list(map(int, list(str(line))))
        tens = max(line)
        if(line.index(tens) != len(line)-1):
            ones = max(line[line.index(tens)+1:])
        else:
            tens = max(line[:-1])
            ones = line[-1]
        ans += ((tens*10)+ones)

    print(ans)

solution()