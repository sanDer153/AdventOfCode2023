NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

mirror_1 = {NORTH: EAST, EAST: NORTH, SOUTH: WEST, WEST: SOUTH}  # Mirror: /
mirror_2 = {NORTH: WEST, EAST: SOUTH, SOUTH: EAST, WEST: NORTH}  # Mirror: \


def main():
    with open("16/input.txt") as f:
        mirror_map = [list(line.rstrip()) for line in f]
    positions = [(0, 0, EAST)]
    energized_tiles = set()
    passed = set()
    while len(positions) > 0:
        (pos_x, pos_y, direction) = positions.pop()
        if pos_x < 0 or pos_y < 0 or pos_x >= len(mirror_map) or pos_y >= len(mirror_map[0]):
            continue
        passed.add((pos_x, pos_y, direction))
        energized_tiles.add((pos_x, pos_y))
        if mirror_map[pos_x][pos_y] == ".":
            new_pos = (pos_x + direction[0], pos_y + direction[1], direction)
            if new_pos not in passed:
                positions.append(new_pos)
        elif mirror_map[pos_x][pos_y] == "/":
            new_direction = mirror_1[direction]
            new_pos = (
                pos_x + new_direction[0], pos_y + new_direction[1], new_direction)
            if new_pos not in passed:
                positions.append(new_pos)
        elif mirror_map[pos_x][pos_y] == "\\":
            new_direction = mirror_2[direction]
            new_pos = (
                pos_x + new_direction[0], pos_y + new_direction[1], new_direction)
            if new_pos not in passed:
                positions.append(new_pos)
        elif mirror_map[pos_x][pos_y] == "-":
            if direction == NORTH or direction == SOUTH:
                new_pos_1 = (pos_x + EAST[0],
                             pos_y + EAST[1], EAST)
                if new_pos_1 not in passed:
                    positions.append(new_pos_1)
                new_pos_2 = (pos_x + WEST[0],
                             pos_y + WEST[1], WEST)
                if new_pos_2 not in passed:
                    positions.append(new_pos_2)
            else:
                new_pos = (pos_x + direction[0],
                           pos_y + direction[1], direction)
                if new_pos not in passed:
                    positions.append(new_pos)
        elif mirror_map[pos_x][pos_y] == "|":
            if direction == EAST or direction == WEST:
                new_pos_1 = (pos_x + NORTH[0],
                             pos_y + NORTH[1], NORTH)
                if new_pos_1 not in passed:
                    positions.append(new_pos_1)
                new_pos_2 = (pos_x + SOUTH[0],
                             pos_y + SOUTH[1], SOUTH)
                if new_pos_2 not in passed:
                    positions.append(new_pos_2)
            else:
                new_pos = (pos_x + direction[0],
                           pos_y + direction[1], direction)
                if new_pos not in passed:
                    positions.append(new_pos)
    print(len(energized_tiles))


if __name__ == "__main__":
    main()
