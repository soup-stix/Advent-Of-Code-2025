with open(r"01\AOC_1_input.txt", "r") as f:
    lines = f.readlines()

code = 50
ans = 0

for step in lines:
    dir = step[0:1]
    clicks = int(step[1:])
    if dir == "L":
        code = (code+(-1*clicks))%100

    if dir == "R":
        code = (code+clicks)%100

    if code == 0: ans += 1

print(ans)