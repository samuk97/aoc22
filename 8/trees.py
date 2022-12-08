import numpy as np

file = open("input.txt")

lines = file.readlines()

grid_size = (len(lines), len(lines[0]) - 1)
grid = np.zeros(grid_size)

# Parsing
for y, line in enumerate(lines):
    for x, c in enumerate(line.replace("\n", "")):
        grid[y, x] = int(c)

# Part 1
counter = 2 * grid_size[0] + 2 * (grid_size[1] - 2)
for y in range(1, grid_size[0] - 1):
    for x in range(1, grid_size[1] - 1):
        if (
            np.max(grid[y, :x]) < (grid[y, x])  # W
            or np.max(grid[y, x + 1 :]) < (grid[y, x])  # E
            or np.max(grid[:y, x]) < (grid[y, x])  # N
            or np.max(grid[y + 1 :, x]) < (grid[y, x])  # S
        ):
            counter += 1

print(counter)

# Part 2
def viewDistance(array, height):
    counter = 0
    for i in range(array.size):
        counter += 1
        if array[i] >= height:
            break
    return counter


bestScore = 0
for y in range(1, grid_size[0] - 1):
    for x in range(1, grid_size[1] - 1):
        score = (
            viewDistance(np.flip(grid[y, :x]), grid[y, x])  # W
            * viewDistance(grid[y, x + 1 :], grid[y, x])  # E
            * viewDistance(np.flip(grid[:y, x]), grid[y, x])  # N
            * viewDistance(grid[y + 1 :, x], grid[y, x])  # S
        )
        bestScore = max(bestScore, score)

print(bestScore)
