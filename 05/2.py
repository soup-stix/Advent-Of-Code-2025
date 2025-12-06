def getInput():
    with open(r"05\AOC_5_input.txt", "r") as f:
        data = f.read().strip()

    ranges, products = data.split("\n\n")
    int_ranges = []
    for line in ranges.split("\n"):
        low, high = map(int, line.split("-"))
        int_ranges.append((low, high))

    products = [int(x) for x in products.split("\n")]
    return int_ranges, products



def solution():
    ranges, products = getInput()
    ans = 0

    ranges = sorted(ranges) 

    current_low, current_high = ranges[0]
    new = []

    for rng in ranges[1:]:
        low, high = rng  
        if current_high >= low:
            current_high = max(current_high, high)
        else:  
            new.append((current_low, current_high))
            current_low, current_high = low, high

    new.append((current_low, current_high))
        
    ans = sum(e - s + 1 for s, e in new)
    
    print(ans)

solution()