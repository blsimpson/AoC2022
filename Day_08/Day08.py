grid = [list(map(int, line)) for line in open(".\day_08\input.txt", "r").read().splitlines()]

def part_one(grid):
    t = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            k = grid[r][c]
            if all(grid[r][x] < k for x in range(c)) or all(grid[r][x] < k for x in range(c + 1, len(grid[r]))) or all(grid[x][c] < k for x in range(r)) or all(grid[x][c] < k for x in range(r + 1, len(grid))):
                t += 1
    return t

def part_two(grid):
    t = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            k = grid[r][c]
            L = U = R = D = 0
            for x in range(c - 1, -1, -1):
                L += 1
                if grid[r][x] >= k:
                    break
            for x in range(c + 1, len(grid[r])):
                R += 1
                if grid[r][x] >= k:
                    break
            for x in range(r - 1, -1, -1):
                U += 1
                if grid[x][c] >= k:
                    break
            for x in range(r + 1, len(grid[r])):
                D += 1
                if grid[x][c] >= k:
                    break
            t = max(t, U * D * L * R)
    return t
            
print(part_one(grid))
print(part_two(grid))