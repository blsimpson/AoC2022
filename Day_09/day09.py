import math

def process_move(lines, num_knots):
    knots = [(0,0)] * num_knots
    visited = { (0,0) }
    for line in lines:
        direction, num = line.split(' ')
        m = move[direction]
        for _ in range(int(num)):
            #move the head
            #hx, hy = hx + m[0], hy + m[1]
            knots[0] = [knots[0][0] + m[0], knots[0][1] + m[1]]
            
            # Update the tails
            for i in range(1, len(knots)):
                #dx, dy = hx - tx, hy - ty
                dx = knots[i-1][0] - knots[i][0]
                dy = knots[i-1][1] - knots[i][1]
                
                if abs(dx) > 1 or abs(dy) > 1:
                    newx, newy = knots[i][0], knots[i][1]
                    if dx:
                        newx = knots[i][0] + math.copysign(1, dx)
                    if dy:
                        newy = knots[i][1] + math.copysign(1, dy)
                    knots[i] = (newx, newy)
                    #vistited.add((tx,ty))
            visited.add(knots[-1])
    return len(visited)        
            
move = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0,1)}

with open(".\day_09\input.txt", 'r') as f:
    lines = f.readlines()

#hx, hy, tx, ty = 0, 0, 0, 0    

            
part1 = process_move(lines, 2)
print(f'Part 1: {part1}')

part2 = process_move(lines, 10)
print(f'Part 2: {part2}')