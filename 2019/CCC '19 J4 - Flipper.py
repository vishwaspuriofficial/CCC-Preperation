grid = [[1,2],[3,4]]

seq = input()

for i in seq:
    if i == "H":
        grid.append(grid[0])
        grid.pop(0)
    else:
        for j in range(len(grid)):
            grid[j] = grid[j][::-1]

for g in grid:
    print(" ".join(str(e) for e in g))
