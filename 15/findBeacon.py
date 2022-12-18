import sys
import copy

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


# Part 1
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

# Part 2
sizeOfInterest = 4000000
coordinatesOfInterest = []

for s in sensors:
    sPos = s[0]
    distance = s[1]
    coord = [sPos[0] - distance - 1, sPos[1]]
    directions = [[1, -1], [1, 1], [-1, 1], [-1, -1]]
    for dir in range(4):
        for n in range(distance + 1):
            if (
                coord[0] + minY >= 0
                and coord[1] + minX >= 0
                and coord[0] + minY <= sizeOfInterest
                and coord[1] + minX <= sizeOfInterest
            ):
                coordinatesOfInterest.append(copy.deepcopy(coord))
            coord[0] += directions[dir][0]
            coord[1] += directions[dir][1]

for c in coordinatesOfInterest:
    y = c[0]
    x = c[1]
    distressBeacon = True
    for s in sensors:
        distance = s[1]
        if abs(y - s[0][0]) + abs(x - s[0][1]) <= distance:
            distressBeacon = False
    if distressBeacon:
        print(x + minX, y + minY)
        print((x + minX) * 4000000 + (y + minY))
        exit()
