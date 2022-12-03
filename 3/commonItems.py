file = open("input.txt")

lines = file.readlines()

# Part 1
priority = 0

for line in lines:
    left = line[: int(len(line) / 2)]
    right = line[int(len(line) / 2) :]
    common_char = "".join(set(left).intersection(right))
    if common_char.isupper():
        priority += ord(common_char) - 38
    else:
        priority += ord(common_char) - 96

print(priority)

# Part 2
priority = 0

for i in range(int(len(lines) / 3)):
    common_char = "".join(
        set(lines[i * 3]).intersection(lines[i * 3 + 1]).intersection(lines[i * 3 + 2])
    ).replace("\n", "")
    if common_char.isupper():
        priority += ord(common_char) - 38
    else:
        priority += ord(common_char) - 96

print(priority)
