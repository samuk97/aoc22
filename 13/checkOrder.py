file = open("input.txt")

lines = [line for line in file.readlines() if line != "\n"]


def compare(left, right):
    if type(left) == int and type(right) == int:
        return left < right
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]
    for i in range(len(left)):
        if i >= len(right):  # right list runs out of items
            return False
        elif left[i] == right[i]:
            continue
        else:
            return compare(left[i], right[i])
    return True  # left list runs out of items


counter = 0
for pair in range(int(len(lines) / 2)):
    # Sebastian told me about "eval()"
    left, right = eval(lines[pair * 2]), eval(lines[pair * 2 + 1])
    if compare(left, right):
        counter += pair + 1

print(counter)
