import copy
import itertools

file = open("input.txt")

lines = file.readlines()

numStacks = 9
maxHeight = 8

containers = [[] for i in range(numStacks)]

# Parsing
for line in itertools.islice(lines, 0, maxHeight):
    index = 0
    while len(line) > 0:
        if line[0] == " ":
            index += int((len(line) - len(line.lstrip())) / 4)
            line = line.lstrip()
        else:
            containers[index].insert(0, line[1])
            line = line[4:]
            index += 1

containers2 = copy.deepcopy(containers)

# Part 1
for line in itertools.islice(lines, maxHeight + 2, len(lines)):
    command = line.split()
    for i in range(int(command[1])):
        containers[int(command[5]) - 1].append(containers[int(command[3]) - 1].pop())

print("".join([container.pop() for container in containers]))

# Part 2
for line in itertools.islice(lines, maxHeight + 2, len(lines)):
    command = line.split()
    containers2[int(command[5]) - 1].extend(
        containers2[int(command[3]) - 1][-int(command[1]) :]
    )
    containers2[int(command[3]) - 1] = containers2[int(command[3]) - 1][
        : -int(command[1])
    ]

print("".join([container.pop() for container in containers2]))
