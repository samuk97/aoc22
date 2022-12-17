import sys

file = open("input.txt")

lines = file.readlines()

minX = sys.maxsize
maxX = 0
minY = sys.maxsize
maxY = 0


def updateBounds(x, y):
    global minX, maxX, minY, maxY
    minX = min(minX, x)
    maxX = max(maxX, x)
    minY = min(minY, y)
    maxY = max(maxY, y)


for line in lines:
    line = line.split()
    updateBounds(int(line[2][2:-1]) - int(line[8][2:-1]), int(line[3][2:-1]))
    updateBounds(int(line[2][2:-1]) + int(line[8][2:-1]), int(line[3][2:-1]))
    updateBounds(int(line[2][2:-1]), int(line[3][2:-1]) - int(line[9][2:]))
    updateBounds(int(line[2][2:-1]), int(line[3][2:-1]) + int(line[9][2:]))

sensors = []
beaconPos = []
for line in lines:
    line = line.split()
    posS = [int(line[3][2:-1]) - minY, int(line[2][2:-1]) - minX]
    posB = [int(line[9][2:]) - minY, int(line[8][2:-1]) - minX]
    distance = abs(posS[0] - posB[0]) + abs(posS[1] - posB[1])
    sensors.append([posS, distance])
    beaconPos.append(posB)


counter = 0
rowOfInterest = 2000000
y = rowOfInterest - minY
for x in range(maxX - minX):
    for i in range(len(sensors)):
        distance = sensors[i][1]
        if (
            abs(y - sensors[i][0][0]) + abs(x - sensors[i][0][1]) <= distance
            and [y, x] not in beaconPos
        ):
            counter += 1
            break

print(counter)
