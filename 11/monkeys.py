file = open("input.txt")

lines = file.readlines()


class Monkey:
    def __init__(self, items, operation, test, trueMonkey, falseMonkey):
        self.items = items
        self.operation = lambda old: eval(operation)
        self.test = test
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey


numMonkeys = int(len(lines) / 7) + 1
monkeys = []

# Parsing
for n in range(numMonkeys):
    startIndex = n * 7 + 1
    monkeys.append(
        Monkey(
            eval("[" + lines[startIndex].split(":")[1] + "]"),
            lines[startIndex + 1].split("=")[1],
            int(lines[startIndex + 2].split()[3]),
            int(lines[startIndex + 3].split()[5]),
            int(lines[startIndex + 4].split()[5]),
        )
    )

nRounds = 20
nInspectedItems = [0] * numMonkeys
for round in range(nRounds):
    for n, monkey in enumerate(monkeys):
        for i, item in enumerate(monkey.items):
            item = monkey.operation(item)
            item = int(item / 3)
            if item % monkey.test == 0:
                monkeys[monkey.trueMonkey].items.append(item)
            else:
                monkeys[monkey.falseMonkey].items.append(item)
            nInspectedItems[n] += 1
        monkey.items = []

nInspectedItems.sort()
print(nInspectedItems[-1] * nInspectedItems[-2])
