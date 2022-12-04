file = open("input.txt")

lines = file.readlines()

# Part 1
counter = 0

for line in lines:
    intervals = line.replace(",", "-").split("-")
    if (
        int(intervals[0]) >= int(intervals[2])
        and int(intervals[1]) <= int(intervals[3])
        or int(intervals[0]) <= int(intervals[2])
        and int(intervals[1]) >= int(intervals[3])
    ):
        counter += 1

print(counter)

# Part 2
counter = 0

for line in lines:
    intervals = line.replace(",", "-").split("-")
    if (
        int(intervals[0]) <= int(intervals[2])
        and int(intervals[1]) >= int(intervals[2])
        or int(intervals[2]) <= int(intervals[0])
        and int(intervals[3]) >= int(intervals[0])
    ):
        counter += 1

print(counter)
