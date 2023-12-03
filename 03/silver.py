def get_next_to(pos, dimension):
    vectors = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
               (0, 1), (1, -1), (1, 0), (1, 1)]
    (row, col) = pos
    return [(row+x, col+y) for (x, y) in vectors if (row+x >= 0 and row+x < dimension and col+y >= 0 and col+y < dimension)]


def main():
    part_numbers = []
    schematic = []
    with open("03/input.txt") as f:
        schematic = [list(row.strip()) for row in f]
    dimension = len(schematic)
    possible_positions = set([pos for row in range(dimension) for col in range(dimension) if (
        schematic[row][col] != '.' and not schematic[row][col].isnumeric()) for pos in get_next_to((row, col), dimension)])
    for row in range(dimension):
        begin_current_number = -1
        valid_number = False
        for col in range(dimension):
            if schematic[row][col].isnumeric() and begin_current_number == -1:
                begin_current_number = col
            if begin_current_number != -1 and (not schematic[row][col].isnumeric() or col == 139):
                if valid_number:
                    number = int(
                        ''.join(schematic[row][begin_current_number:col]))
                    if schematic[row][col].isnumeric() and col == 139:
                        number = int(
                            ''.join(schematic[row][begin_current_number:col+1]))
                    part_numbers.append(number)
                begin_current_number = -1
                valid_number = False
            if (row, col) in possible_positions and begin_current_number != -1:
                valid_number = True

    print(sum(part_numbers))


if __name__ == "__main__":
    main()
