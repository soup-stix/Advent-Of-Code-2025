with open(r"C:\Users\arul_\Desktop\Anand\Anand CP\AOC_1_input.txt", "r") as f:
    lines = f.readlines()

code = 50
ans = 0

for step in lines:
    dir = step[0:1]
    clicks = int(step[1:])
    zeroes = 0
    for _ in range(clicks):
        if dir == "L":
            code = (code-1)%100

        if dir == "R":
            code = (code+1)%100

        if code == 0: zeroes += 1

    ans += zeroes

print(ans)