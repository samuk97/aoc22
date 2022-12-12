import sys

file = open("input.txt")

lines = file.readlines()

heightMapSize = (len(lines), len(lines[0]) - 1)
heightMap = [["" for i in range(heightMapSize[1])] for j in range(heightMapSize[0])]

# Parsing
for i, line in enumerate(lines):
    for j, c in enumerate(line[:-1]):
        heightMap[i][j] = c

# Part 1
def findChar(c):
    global heightMapSize, heightMap
    for i in range(heightMapSize[0]):
        for j in range(heightMapSize[1]):
            if heightMap[i][j] == c:
                return [i, j]


def step(currentPos, nextStep, steps):
    global heightMapSize, heightMap, numSteps
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
        or numSteps[currentPos[0] + nextStep[0]][currentPos[1] + nextStep[1]] <= steps + 1
        or (
            heightMap[currentPos[0] + nextStep[0]][currentPos[1] + nextStep[1]] == "E"
            and ord("z") - ord(heightMap[currentPos[0]][currentPos[1]]) > 1
        )
    ):
        return
    newPos = [currentPos[0] + nextStep[0], currentPos[1] + nextStep[1]]
    steps += 1
    numSteps[newPos[0]][newPos[1]] = steps
    step(newPos, (0, 1), steps)
    step(newPos, (1, 0), steps)
    step(newPos, (0, -1), steps)
    step(newPos, (-1, 0), steps)


initialPos = findChar("S")
numSteps = [[sys.maxsize for i in range(heightMapSize[1])] for j in range(heightMapSize[0])]
numSteps[initialPos[0]][initialPos[1]] = 0

sys.setrecursionlimit(10000)
step(initialPos, (0, 1), 0),
step(initialPos, (1, 0), 0),
step(initialPos, (0, -1), 0),
step(initialPos, (-1, 0), 0),

endPos = findChar("E")
print(numSteps[endPos[0]][endPos[1]])
