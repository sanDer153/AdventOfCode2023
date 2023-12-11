def expand_galaxy(galaxy_map):
    rows_to_expand = set()
    cols_to_expand = set(range(len(galaxy_map[0])))
    for row in range(len(galaxy_map)):
        galaxies = [galaxy for galaxy in range(
            len(galaxy_map[row])) if galaxy_map[row][galaxy] == "#"]
        if len(galaxies) == 0:
            rows_to_expand.add(row)
        else:
            for galaxy in galaxies:
                if galaxy in cols_to_expand:
                    cols_to_expand.remove(galaxy)
    new_galaxy_map = []
    for row in range(len(galaxy_map)):
        galaxy_row = []
        for col in range(len(galaxy_map[row])):
            galaxy_row.append(galaxy_map[row][col])
            if col in cols_to_expand:
                galaxy_row.append('.')
        new_galaxy_map.append(galaxy_row)
        if row in rows_to_expand:
            new_galaxy_map.append(galaxy_row.copy())
    return new_galaxy_map


def main():
    with open("11/input.txt") as f:
        galaxy_map = [list(line.strip()) for line in f]
    galaxy_map = expand_galaxy(galaxy_map)
    galaxies = []
    for row in range(len(galaxy_map)):
        for col in range(len(galaxy_map[row])):
            if galaxy_map[row][col] == "#":
                galaxies.append((row, col))
    total_dist = 0
    for idx in range(len(galaxies)):
        gal = galaxies[idx]
        for gal_ in galaxies[idx:]:
            total_dist += abs(gal[0]-gal_[0]) + abs(gal[1]-gal_[1])
    print(total_dist)


if __name__ == "__main__":
    main()
