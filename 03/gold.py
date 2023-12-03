def get_next_to(pos, dimension):
    vectors = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
               (0, 1), (1, -1), (1, 0), (1, 1)]
    (row, col) = pos
    return [(row+x, col+y) for (x, y) in vectors if (row+x >= 0 and row+x < dimension and col+y >= 0 and col+y < dimension)]


def get_adjacent_numbers(pos, schematic):
    start_numbers = [(row, (col, col)) for (row, col) in get_next_to(
        pos, len(schematic)) if schematic[row][col].isnumeric()]
    adjacent_numbers = set()
    for n in start_numbers:
        (n_row, (n_start, n_stop)) = n
        interval_grew = True
        while interval_grew:
            interval_grew = False
            if n_start-1 >= 0 and schematic[n_row][n_start-1].isnumeric():
                n_start -= 1
                interval_grew = True
            if n_stop + 1 < len(schematic) and schematic[n_row][n_stop+1].isnumeric():
                n_stop += 1
                interval_grew = True
        adjacent_numbers.add(int("".join(schematic[n_row][n_start:n_stop+1])))
    return list(adjacent_numbers)


def main():
    gear_ratios = []
    schematic = []
    with open("03/input.txt") as f:
        schematic = [list(row.strip()) for row in f]
    dimension = len(schematic)
    for row in range(dimension):
        for col in range(dimension):
            if schematic[row][col] == '*':
                numbers = get_adjacent_numbers((row, col), schematic)
                if len(numbers) == 2:
                    gear_ratios.append(numbers[0]*numbers[1])

    print(sum(gear_ratios))


if __name__ == "__main__":
    main()
