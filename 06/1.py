import re, math

def getInput():
    with open(r"06\AOC_6_input.txt", "r") as f:
        data = f.read()
        parts = re.split(r'(\+|\*)', data, maxsplit=1)
        s = parts[0]
        numbers = s.split()
        o  = ''.join(parts[1:])
        operations = o.split()

    print(len(numbers), len(operations))

    columns = [] 
    for i in range(len(operations)):
        temp = []
        temp.append(operations[i])
        for j in range(len(numbers)//len(operations)):
            temp.append(numbers[i+(1000*j)])
        columns.append(temp)
    
    return columns



def solution():
    columns = getInput()
    ans = 0

    for column in columns:
        operator = column[0]
        numbers = column[1:]
        if operator == "+":
            ans += sum(map(int, numbers))
        if operator == "*":
            ans += math.prod(map(int, numbers))

    print(ans)

solution()