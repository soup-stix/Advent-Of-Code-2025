neighbours = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))

def getInput():
    with open(r"04\AOC_4_input.txt", "r") as f:
        lines = f.read().splitlines()

    return lines

def check_nearby(rows, x, y):
    count_nearby = 0
    max_y = len(rows)
    max_x = len(rows[0])

    for dx, dy in neighbours:  
        nx, ny = x + dx, y + dy 
        if 0 <= nx < max_x and 0 <= ny < max_y: 
            count_nearby += rows[ny][nx] == "@"
                 

    return count_nearby

def solution():
    rows = getInput()
    ans = 0

    for y, row in enumerate(rows):
        for x, item in enumerate(row):
            if item != "@":
                continue

            nearby = check_nearby(rows, x, y)
            print(f"{nearby=}, ({x}, {y})")

            if nearby <= 3:
                ans += 1

    print(ans)

solution()