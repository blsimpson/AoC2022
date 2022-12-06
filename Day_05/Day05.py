from copy import deepcopy
import re

inputfile = open(".\day_05\input.txt", 'r')

stack, moves = inputfile.read().split("\n\n")

stacks = [[] for _ in range(10)]

for line in stack.split("\n"):
    for i in range(0, len(line), 4):
        c = line[i:i + 4]
        if '[' in c:
            stacks[i//4].append(c[1])

print("before:", stacks)

for i in range(len(stacks)):
    stacks[i] = stacks[i][::-1]
    
print("rev:", stacks)

orig_stacks = deepcopy(stacks)
for move in moves.split("\n"):
    count, fromi, toj = [int(x) for x in re.findall(r'\d+', move)]
    fromi -= 1
    toj -=1
    
    while count and stacks[fromi]:
        stacks[toj].append(stacks[fromi].pop())
        count -= 1

print("after:", stacks)

top = ""
for s in stacks:
    if s:
        top += s[-1]

print("Tops:", top)

#part 2:

for move in moves.split("\n"):
    count, fromi, toj = [int(x) for x in re.findall(r'\d+', move)]
    fromi -= 1
    toj -=1
    n = len(orig_stacks[fromi])
    orig_stacks[toj] += orig_stacks[fromi][n - count:]
    orig_stacks[fromi] = orig_stacks[fromi][:n - count]
    
top = ""
for s in orig_stacks:
    if s:
        top += s[-1]

print("Tops:", top)