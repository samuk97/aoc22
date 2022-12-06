import itertools


def existDuplicates(list):
    for e in list:
        if list.count(e) != 1:
            return True
    return False


def find_marker(num_chars):
    file = open("input.txt")

    line = list(file.readlines()[0])

    char_history = line[:num_chars]
    counter = num_chars
    for c in itertools.islice(line, num_chars, len(line)):
        if not existDuplicates(char_history):
            break
        char_history.append(c)
        char_history.pop(0)
        counter += 1

    print(counter)


if __name__ == "__main__":
    # Part 1
    find_marker(4)
    # Part 2
    find_marker(14)
