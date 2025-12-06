def getInput():
    with open(r"05\AOC_5_input.txt", "r") as f:
        input_parts = f.read().split("\n\n")
        ranges = input_parts[0].splitlines()
        products = input_parts[1].splitlines()

    return ranges, products



def solution():
    ranges, products = getInput()
    ans = 0

    parsed_ranges = []
    for rng in ranges:
        s, e = rng.split("-")
        parsed_ranges.append((int(s), int(e)))

    for product in products:
        p = int(product)
        
        for s, e in parsed_ranges:
            if s <= p <= e:
                ans += 1
                break  

    print(ans)

solution()