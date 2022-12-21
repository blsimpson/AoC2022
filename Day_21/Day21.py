#!/usr/bin/env python3

import sys


def get_val(m):
    ex = monkeys[m]
    try:
        return int(ex)
    except ValueError:
        pass

    toks = ex.split(' ')
    assert len(toks) == 3

    match toks[1]:
        case '+':
            return get_val(toks[0]) + get_val(toks[2])
        case '-':
            return get_val(toks[0]) - get_val(toks[2])
        case '*':
            return get_val(toks[0]) * get_val(toks[2])
        case '/':
            return get_val(toks[0]) / get_val(toks[2])
    assert False

def get_val2(m, humn):
    if m == 'humn':
        return humn
    ex = monkeys[m]
    try:
        return int(ex)
    except ValueError:
        pass

    toks = ex.split(' ')
    assert len(toks) == 3


    if m == 'root':
        v1 = get_val2(toks[0], humn)
        v2 = get_val2(toks[2], humn)
        return (v1 == v2, v1, v2)

    if toks[1] == '+':
        return get_val2(toks[0], humn) + get_val2(toks[2], humn)
    if toks[1] == '-':
        return get_val2(toks[0], humn) - get_val2(toks[2], humn)
    if toks[1] == '*':
        return get_val2(toks[0], humn) * get_val2(toks[2], humn)
    if toks[1] == '/':
        return get_val2(toks[0], humn) / get_val2(toks[2], humn)
    assert False


with open(".\day_21\input.txt", 'r') as f:
    lines = f.readlines()

monkeys = {}
for line in lines:
    # scms: zhsc + plrj
    m, ex = line.strip().split(': ')
    monkeys[m] = ex

part1 = int(get_val('root'))
print(f'Part 1: {part1}')

lo = -1e20
hi = 1e20
mid = 0
while True:
    eq, v1, v2 = get_val2('root', mid)
    if eq:
        break
    if v1 - v2 > 0:
        lo = mid
    else:
        hi = mid
    mid = (hi + lo)//2

part2 = int(mid)
print(f'Part 2: {part2}')