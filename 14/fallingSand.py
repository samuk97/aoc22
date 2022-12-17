import numpy as np
import sys

file = open("input.txt")

lines = file.readlines()

# Parsing
minX = sys.maxsize
maxX = 0
maxY = 0
for line in lines:
    coordinates = line.split("->")
    for coordinate in coordinates:
        coordinate = coordinate.split(",")
        minX = min(minX, int(coordinate[0]))
        maxX = max(maxX, int(coordinate[0]))
        maxY = max(maxY, int(coordinate[1]))

cave = np.zeros((maxY + 1, maxX - minX + 1))

for line in lines:
    coordinates = line.split("->")
    for i in range(len(coordinates) - 1):
        point0 = coordinates[i].split(",")
        point1 = coordinates[i + 1].split(",")
        if int(point0[0]) < int(point1[0]) or int(point0[1]) < int(point1[1]):
            cave[
                int(point0[1]) : int(point1[1]) + 1,
                int(point0[0]) - minX : int(point1[0]) - minX + 1,
            ] = 1.0
        else:
            cave[
                int(point1[1]) : int(point0[1]) + 1,
                int(point1[0]) - minX : int(point0[0]) - minX + 1,
            ] = 1.0

# Part 1
def produceSand(cave):
    global minX
    sandPos = [500 - minX, 0]
    while True:
        if (
            cave[sandPos[1] + 1, sandPos[0]] != 1
            and cave[sandPos[1] + 1, sandPos[0]] != 2
        ):
            sandPos[1] += 1
        elif (
            cave[sandPos[1] + 1, sandPos[0] - 1] != 1
            and cave[sandPos[1] + 1, sandPos[0] - 1] != 2
        ):
            sandPos[0] -= 1
            sandPos[1] += 1
        elif (
            cave[sandPos[1] + 1, sandPos[0] + 1] != 1
            and cave[sandPos[1] + 1, sandPos[0] + 1] != 2
        ):
            sandPos[0] += 1
            sandPos[1] += 1
        else:
            break

    cave[sandPos[1], sandPos[0]] = 2


counter = 0

while True:
    try:
        produceSand(cave)
        counter += 1
    except:
        break

print(counter)

# Part 2
maxY += 2
minX = min(minX, 500 - (maxY + 1))
maxX = max(maxX, 500 + (maxY + 1))
cave2 = np.zeros((maxY + 1, maxX - minX + 1))
cave2[-1::] = 1

for line in lines:
    coordinates = line.split("->")
    for i in range(len(coordinates) - 1):
        point0 = coordinates[i].split(",")
        point1 = coordinates[i + 1].split(",")
        if int(point0[0]) < int(point1[0]) or int(point0[1]) < int(point1[1]):
            cave2[
                int(point0[1]) : int(point1[1]) + 1,
                int(point0[0]) - minX : int(point1[0]) - minX + 1,
            ] = 1.0
        else:
            cave2[
                int(point1[1]) : int(point0[1]) + 1,
                int(point1[0]) - minX : int(point0[0]) - minX + 1,
            ] = 1.0


def produceSand2(cave):
    global minX
    sandPos = [500 - minX, 0]
    while True:
        if (
            cave[sandPos[1] + 1, sandPos[0]] != 1
            and cave[sandPos[1] + 1, sandPos[0]] != 2
        ):
            sandPos[1] += 1
        elif (
            cave[sandPos[1] + 1, sandPos[0] - 1] != 1
            and cave[sandPos[1] + 1, sandPos[0] - 1] != 2
        ):
            sandPos[0] -= 1
            sandPos[1] += 1
        elif (
            cave[sandPos[1] + 1, sandPos[0] + 1] != 1
            and cave[sandPos[1] + 1, sandPos[0] + 1] != 2
        ):
            sandPos[0] += 1
            sandPos[1] += 1
        else:
            break
    if sandPos == [500 - minX, 0]:
        raise ValueError()
    cave[sandPos[1], sandPos[0]] = 2


counter = 0

while True:
    try:
        produceSand2(cave2)
        counter += 1
    except:
        break

print(counter + 1)
