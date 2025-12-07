import re, math

def getInput():
    with open(r"06\AOC_6_input.txt", "r") as f:
        data = f.read().strip("\n").split("\n")

    return data

def regroup_and_int(list_to_group: list[tuple[str, ...]]) -> list[tuple[int]]:
    groups = []
    current_grp = []

    for item in list_to_group:
        combined = "".join(item).strip()
        if combined:
            current_grp.append(int(combined))
        else: 
            groups.append(tuple(current_grp))
            current_grp = []

    groups.append(tuple(current_grp)) 
    return groups


def simplify_to_dict(
    operators: list[str], gropued_values: list[list[int]]
) -> dict[tuple[int, ...], str]:
    assert len(operators) == len(gropued_values)
    return {group: op for group, op in zip(gropued_values, operators)}


def calc_nums(nums: tuple[int], op: str) -> int:
    assert op in ["+", "*"]

    if op == "+":
        return sum(nums)

    product = 1
    for k in nums:
        product *= k
    return product


def solution():
    input_list = getInput()
    *rows, op_row = input_list
    ans = 0
    operators = list(op_row[::-1].replace(" ", ""))
    transposed = [f for f in zip(*rows, strict=True)]

    grouped = regroup_and_int(transposed[::-1])
    simplified = simplify_to_dict(operators, grouped)

    for i in simplified.items():
        ans += calc_nums(*i)

    print(ans)

solution()