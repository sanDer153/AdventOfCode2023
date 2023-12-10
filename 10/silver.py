def get_connections(shape, pos):
    x, y = pos
    if shape == "|":
        return [(x-1, y), (x+1, y)]
    elif shape == "-":
        return [(x, y-1), (x, y+1)]
    elif shape == "L":
        return [(x-1, y), (x, y+1)]
    elif shape == "J":
        return [(x-1, y), (x, y-1)]
    elif shape == "7":
        return [(x+1, y), (x, y-1)]
    elif shape == "F":
        return [(x+1, y), (x, y+1)]


def main():
    with open("10/input.txt") as f:
        pipes_map = [list(line.strip()) for line in f]
    pos1 = ((76, 24), (77, 24))
    pos2 = ((76, 24), (76, 23))
    steps = 0
    while pos1[0] != pos2[0] or pipes_map[pos1[0][0]][pos1[0][1]] == "S":
        new_pos1_next = get_connections(
            pipes_map[pos1[1][0]][pos1[1][1]], pos1[1])
        new_pos1_next.remove(pos1[0])
        new_pos2_next = get_connections(
            pipes_map[pos2[1][0]][pos2[1][1]], pos2[1])
        new_pos2_next.remove(pos2[0])
        pos1 = (pos1[1], new_pos1_next[0])
        pos2 = (pos2[1], new_pos2_next[0])
        steps += 1
    print(steps)


if __name__ == "__main__":
    main()
