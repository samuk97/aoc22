import numpy as np

file = open("test.txt")

lines = file.readlines()

directions = {"R": [1, 0], "U": [0, 1], "L": [-1, 0], "D": [0, -1]}

headPos = [0, 0]
tailPos = [0, 0]
visitedPos = {}


def updateTailPos(headPos, tailPos):
    if abs(headPos[0] - tailPos[0]) > 1:
        tailPos[0] += np.sign(headPos[0] - tailPos[0])
        tailPos[1] = headPos[1]
    if abs(headPos[1] - tailPos[1]) > 1:
        tailPos[1] += np.sign(headPos[1] - tailPos[1])
        tailPos[0] = headPos[0]


# Part 1
for line in lines:
    line = line.split()
    for step in range(int(line[1])):
        headPos[0] += directions[line[0]][0]
        headPos[1] += directions[line[0]][1]
        updateTailPos(headPos, tailPos)
        visitedPos[str(tailPos)] = 1

print(len(visitedPos))
