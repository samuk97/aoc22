import numpy as np

file = open("input.txt")

lines = file.readlines()

relevantCycles = [20, 60, 100, 140, 180, 220]
X = 1
cyclesCompleted = 0
signalStrengthSum = 0

# Part 1
def signalStrengthCheck():
    global relevantCycles, X, cyclesCompleted, signalStrengthSum
    if cyclesCompleted in relevantCycles:
        signalStrengthSum += cyclesCompleted * X
        print(cyclesCompleted, X, cyclesCompleted * X)


for line in lines:
    line = line.split()
    if line[0] == "noop":
        cyclesCompleted += 1
        signalStrengthCheck()
    else:  # addx
        cyclesCompleted += 1
        signalStrengthCheck()
        cyclesCompleted += 1
        signalStrengthCheck()
        X += int(line[1])

print(signalStrengthSum)

# Part 2
screenSize = (6, 40)
screen = [["" for i in range(screenSize[1])] for j in range(screenSize[0])]
cyclesCompleted = 0
spritePosition = 1


def draw():
    global spritePosition, cyclesCompleted, screenSize
    if abs(spritePosition - cyclesCompleted % screenSize[1]) < 2:
        screen[int(cyclesCompleted / screenSize[1])][
            cyclesCompleted % screenSize[1]
        ] = "#"
    else:
        screen[int(cyclesCompleted / screenSize[1])][
            cyclesCompleted % screenSize[1]
        ] = "."


for line in lines:
    line = line.split()
    if line[0] == "noop":
        draw()
        cyclesCompleted += 1
    else:  # addx
        draw()
        cyclesCompleted += 1
        draw()
        cyclesCompleted += 1
        spritePosition += int(line[1])

for i in range(screenSize[0]):
    for j in range(screenSize[1]):
        print(screen[i][j], end="")
    print("")
