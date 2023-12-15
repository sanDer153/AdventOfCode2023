def HASH(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def HASHMAP(instructions):
    boxes = [[] for i in range(256)]
    for instr in instructions:
        box = HASH(instr[0])
        if instr[1] == "-":
            idx = [boxes[box].index((label, focal))
                   for (label, focal) in boxes[box] if label == instr[0]]
            if len(idx) != 0:
                boxes[box].pop(idx[0])
        elif instr[1] == "=":
            idx = [boxes[box].index((label, focal))
                   for (label, focal) in boxes[box] if label == instr[0]]
            if len(idx) != 0:
                boxes[box][idx[0]] = (instr[0], instr[2])
            else:
                boxes[box].append((instr[0], instr[2]))
    return boxes


def main():
    solution = 0
    with open("15/input.txt") as f:
        instructions = list(
            map(lambda s: (s[:-2], s[-2], int(s[-1])) if s[-1] != "-" else (s[:-1], s[-1], 0), f.readlines()[0].split(',')))
    boxes = HASHMAP(instructions)

    for box_idx in range(len(boxes)):
        for lens_idx in range(len(boxes[box_idx])):
            solution += (box_idx+1) * (lens_idx+1) * \
                boxes[box_idx][lens_idx][1]

    print(solution)


if __name__ == "__main__":
    main()
