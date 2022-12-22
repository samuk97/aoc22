file = open("input.txt")

lines = [line for line in file.readlines() if line != "\n"]


def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        if left > right:
            return False
        return None
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]
    for i in range(max(len(left), len(right))):
        if i >= len(right):  # right list runs out of items
            return False
        if i >= len(left):  # left list runs out of items
            return True
        if compare(left[i], right[i]) == True:
            return True
        if compare(left[i], right[i]) == False:
            return False
        continue
    return None  #


# Part 1
counter = 0
for pair in range(int(len(lines) / 2)):
    # Sebastian told me about "eval()"
    left, right = eval(lines[pair * 2]), eval(lines[pair * 2 + 1])
    if compare(left, right):
        counter += pair + 1

print(counter)

# Part 2
packets = []
for line in lines:
    if line != "\n":
        packets.append(eval(line))

divider0 = [[2]]
divider1 = [[6]]
packets.append(divider0)
packets.append(divider1)

changed = True
while changed:
    changed = False
    for i in range(len(packets) - 1):
        if not compare(packets[i], packets[i + 1]):
            first = packets.pop(i)
            second = packets.pop(i)
            packets.insert(i, second)
            packets.insert(i + 1, first)
            changed = True

print((packets.index(divider0) + 1) * (packets.index(divider1) + 1))
