elve_calories = [0]

file = open("input.txt")
lines = file.readlines()

for line in lines:
    if line == "\n":
        elve_calories.append(0)
    else:
        elve_calories[-1] += int(line)

# Part 1
print(max(elve_calories))

# Part 2
elve_calories.sort()
print(elve_calories[-1] + elve_calories[-2] + elve_calories[-3])
