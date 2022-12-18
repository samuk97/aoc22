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


directions = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]


def computeSurfaceArea(part):
    surfaceArea = 0
    for z in range(maxZ + 1):
        for y in range(maxY + 1):
            for x in range(maxX + 1):
                if droplet[z, y, x] == 1.0:
                    for dir in directions:
                        try:
                            if (
                                droplet[z + dir[2], y + dir[1], x + dir[0]] == 0.0
                                or droplet[z + dir[2], y + dir[1], x + dir[0]] == -1.0
                            ):
                                if part == 2:
                                    if (
                                        droplet[z + dir[2], y + dir[1], x + dir[0]]
                                        != -1.0
                                    ):
                                        continue
                                surfaceArea += 1
                        except:
                            surfaceArea += 1
    return surfaceArea


# Part 1
print(computeSurfaceArea(1))

# Part 2
def markNotTrapped():
    changed = True
    while changed:
        changed = False
        for z in range(maxZ + 1):
            for y in range(maxY + 1):
                for x in range(maxX + 1):
                    if droplet[z, y, x] == 0.0:
                        for dir in directions:
                            try:
                                if droplet[z + dir[2], y + dir[1], x + dir[0]] == -1.0:
                                    droplet[z, y, x] = -1.0
                                    changed = True
                                    break
                            except:
                                droplet[z, y, x] = -1.0
                                changed = True
                                break


markNotTrapped()
print(computeSurfaceArea(2))
