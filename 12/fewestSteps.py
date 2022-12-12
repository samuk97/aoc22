import sys
import copy

file = open("test.txt")

lines = file.readlines()

heightMapSize = (len(lines), len(lines[0]) - 1)
heightMap = [["" for i in range(heightMapSize[1])] for j in range(heightMapSize[0])]

# Parsing
for i, line in enumerate(lines):
    for j, c in enumerate(line[:-1]):
        heightMap[i][j] = c

# Part 1
def findStart():
    global heightMapSize, heightMap
    for i in range(heightMapSize[0]):
        for j in range(heightMapSize[1]):
            if heightMap[i][j] == "S":
                return [i, j]


def step(visited, currentPos, nextStep, numSteps):
    global heightMapSize, heightMap
    # Goal
    if heightMap[currentPos[0]][currentPos[1]] == "E":
        return numSteps
    # Invalid step
    if (
        currentPos[0] + nextStep[0] < 0
        or currentPos[1] + nextStep[1] < 0
        or currentPos[0] + nextStep[0] >= heightMapSize[0]
        or currentPos[1] + nextStep[1] >= heightMapSize[1]
        or (
            ord(heightMap[currentPos[0] + nextStep[0]][currentPos[1] + nextStep[1]])
            - ord(heightMap[currentPos[0]][currentPos[1]])
            > 1
            and heightMap[currentPos[0]][currentPos[1]] != "S"
        )
        or visited[currentPos[0] + nextStep[0]][currentPos[1] + nextStep[1]] == 1
        or (
            heightMap[currentPos[0] + nextStep[0]][currentPos[1] + nextStep[1]] == "E"
            and ord("z") - ord(heightMap[currentPos[0]][currentPos[1]]) > 1
        )
    ):
        return sys.maxsize
    newPos = [currentPos[0] + nextStep[0], currentPos[1] + nextStep[1]]
    visited[newPos[0]][newPos[1]] = 1
    numSteps += 1
    return min(
        step(copy.deepcopy(visited), newPos, (0, 1), numSteps),
        step(copy.deepcopy(visited), newPos, (1, 0), numSteps),
        step(copy.deepcopy(visited), newPos, (0, -1), numSteps),
        step(copy.deepcopy(visited), newPos, (-1, 0), numSteps),
    )


initialPos = findStart()
visited = [[0 for i in range(heightMapSize[1])] for j in range(heightMapSize[0])]
visited[initialPos[0]][initialPos[1]] = 1
print(
    min(
        step(copy.deepcopy(visited), initialPos, (0, 1), 0),
        step(copy.deepcopy(visited), initialPos, (1, 0), 0),
        step(copy.deepcopy(visited), initialPos, (0, -1), 0),
        step(copy.deepcopy(visited), initialPos, (-1, 0), 0),
    )
)
