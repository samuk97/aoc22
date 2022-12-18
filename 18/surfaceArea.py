import numpy as np

file = open("input.txt")

lines = file.readlines()

maxX = 0
maxY = 0
maxZ = 0

# Get bounds
for line in lines:
    line = line.split(",")
    maxX = max(maxX, int(line[0]))
    maxY = max(maxY, int(line[1]))
    maxZ = max(maxZ, int(line[2]))

droplet = np.zeros((maxZ + 1, maxY + 1, maxX + 1))

# Parsing
for line in lines:
    line = line.split(",")
    droplet[int(line[2]), int(line[1]), int(line[0])] = 1.0

# Part 1
surfaceArea = 0
directions = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
for z in range(maxZ + 1):
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            if droplet[z, y, x] == 1.0:
                for dir in directions:
                    try:
                        if droplet[z + dir[2], y + dir[1], x + dir[0]] == 0.0:
                            surfaceArea += 1
                    except:
                        surfaceArea += 1

print(surfaceArea)
