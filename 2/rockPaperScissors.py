score = 0

file = open("input.txt")
lines = file.readlines()

# Part 1
results = {
    "AX": 1 + 3,
    "AY": 2 + 6,
    "AZ": 3 + 0,
    "BX": 1 + 0,
    "BY": 2 + 3,
    "BZ": 3 + 6,
    "CX": 1 + 6,
    "CY": 2 + 0,
    "CZ": 3 + 3,
}

for line in lines:
    score += results[line.translate({32: None, 10: None})]

print(score)

# Part 2
results = {
    "AX": 3 + 0,
    "AY": 1 + 3,
    "AZ": 2 + 6,
    "BX": 1 + 0,
    "BY": 2 + 3,
    "BZ": 3 + 6,
    "CX": 2 + 0,
    "CY": 3 + 3,
    "CZ": 1 + 6,
}

score = 0

for line in lines:
    score += results[line.translate({32: None, 10: None})]

print(score)
