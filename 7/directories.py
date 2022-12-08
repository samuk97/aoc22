file = open("input.txt")

lines = file.readlines()


class Directory:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.content = {}


directories = []
current_dir = Directory("/")
directories.append(current_dir)

# Parsing
for line in lines[1:]:
    line = line.split()
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                current_dir = current_dir.parent
            else:
                if line[2] in current_dir.content:
                    current_dir = current_dir.content[line[2]]
                else:
                    raise KeyError("Accessing directory that has not been created.")
        else:  # line[1] == "ls"
            continue
    elif line[0] == "dir":
        assert line[1] not in current_dir.content
        newDir = Directory(line[1])
        newDir.parent = current_dir
        current_dir.content[line[1]] = newDir
        directories.append(newDir)
    else:  # file
        assert line[1] not in current_dir.content
        current_dir.content[line[1]] = int(line[0])


def directorySize(directory):
    sum = 0
    for e in directory.content.values():
        if isinstance(e, Directory):
            sum += directorySize(e)
        else:  # int
            sum += e
    return sum


def directoriesSum(condition):
    sum = 0
    for dir in directories:
        dirSize = directorySize(dir)
        if dirSize <= condition:
            sum += dirSize
    return sum


# Part 1
print(directoriesSum(100000))

# Part 2
totalSum = directorySize(directories[0])
toBeFreed = 30000000 - (70000000 - totalSum)
smallestDirSize = 70000000
for dir in directories:
    dirSize = directorySize(dir)
    if dirSize < smallestDirSize and dirSize >= toBeFreed:
        smallestDirSize = dirSize

print(smallestDirSize)
