import numpy as np

file = open("input.txt")

lines = file.readlines()

directions = {"R": [1, 0], "U": [0, 1], "L": [-1, 0], "D": [0, -1]}

headPos = [0, 0]
tailPos = [0, 0]
visitedPos = {}


def updateTailPos(headPos, tailPos):
    if abs(headPos[0] - tailPos[0]) > 1:
        tailPos[0] += np.sign(headPos[0] - tailPos[0])
        if headPos[1] != tailPos[1]:
            tailPos[1] += np.sign(headPos[1] - tailPos[1])
    if abs(headPos[1] - tailPos[1]) > 1:
        tailPos[1] += np.sign(headPos[1] - tailPos[1])
        if headPos[0] != tailPos[0]:
            tailPos[0] += np.sign(headPos[0] - tailPos[0])


# Part 1
for line in lines:
    line = line.split()
    for step in range(int(line[1])):
        headPos[0] += directions[line[0]][0]
        headPos[1] += directions[line[0]][1]
        updateTailPos(headPos, tailPos)
        visitedPos[str(tailPos)] = 1

print(len(visitedPos))

# Part 2
def visualize(ropePos):
    maxValue = 0
    for r in ropePos:
        maxValue = max(maxValue, max(r[0], r[1]))
    array = np.zeros((maxValue + 1, maxValue + 1))
    for r in ropePos:
        array[r[1], r[0]] = 1
    print(np.flip(array, axis=0))


visitedPos = {}
ropeSize = 10
ropePos = [[0, 0] for i in range(ropeSize)]
for line in lines:
    line = line.split()
    for step in range(int(line[1])):
        ropePos[0][0] += directions[line[0]][0]
        ropePos[0][1] += directions[line[0]][1]
        for i in range(ropeSize - 1):
            updateTailPos(ropePos[i], ropePos[i + 1])
        visitedPos[str(ropePos[-1])] = 1

print(len(visitedPos))
