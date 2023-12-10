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
    pipes = {(76, 24)}
    # pos1 = ((0, 4), (0, 3))
    # pos2 = ((0, 4), (1, 4))
    # pipes = {(0, 4)}
    while pos1[0] != pos2[0] or pipes_map[pos1[0][0]][pos1[0][1]] == "S":
        new_pos1_next = get_connections(
            pipes_map[pos1[1][0]][pos1[1][1]], pos1[1])
        new_pos1_next.remove(pos1[0])
        new_pos2_next = get_connections(
            pipes_map[pos2[1][0]][pos2[1][1]], pos2[1])
        new_pos2_next.remove(pos2[0])
        pos1 = (pos1[1], new_pos1_next[0])
        pos2 = (pos2[1], new_pos2_next[0])
        pipes.add(pos1[0])
        pipes.add(pos2[0])
    pipes.add(pos1[0])

    inside = 0
    tile_inside_loop = False
    horizontal_pipe_start_shape = None
    for row in range(len(pipes_map)):
        for col in range(len(pipes_map[row])):
            if (row, col) in pipes:
                if pipes_map[row][col] == "|":
                    tile_inside_loop = not tile_inside_loop
                elif pipes_map[row][col] == "L" or pipes_map[row][col] == "F":
                    horizontal_pipe_start_shape = pipes_map[row][col]
                elif pipes_map[row][col] == "7" or pipes_map[row][col] == "J":
                    if pipes_map[row][col] == "7" and horizontal_pipe_start_shape == "L" or pipes_map[row][col] == "J" and horizontal_pipe_start_shape == "F":
                        tile_inside_loop = not tile_inside_loop

            else:
                if tile_inside_loop:
                    inside += 1
    print(inside)


if __name__ == "__main__":
    main()
