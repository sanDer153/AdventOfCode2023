

def do_cycle(platform):
    # north
    stones = [0]*len(platform[0])
    for row_idx in range(len(platform)-1, -1, -1):
        for col_idx in range(len(platform[row_idx])):
            if platform[row_idx][col_idx] == "O":
                stones[col_idx] += 1
                platform[row_idx][col_idx] = "."
            elif platform[row_idx][col_idx] == "#":
                while stones[col_idx] > 0:
                    platform[row_idx+stones[col_idx]][col_idx] = "O"
                    stones[col_idx] -= 1
    # west
    stones = [0]*len(platform)
    for col_idx in range(len(platform[0])-1, -1, -1):
        for row_idx in range(len(platform)):
            if platform[row_idx][col_idx] == "O":
                stones[row_idx] += 1
                platform[row_idx][col_idx] = "."
            elif platform[row_idx][col_idx] == "#":
                while stones[row_idx] > 0:
                    platform[row_idx][col_idx+stones[row_idx]] = "O"
                    stones[row_idx] -= 1
    # south
    stones = [0]*len(platform[0])
    for row_idx in range(len(platform)):
        for col_idx in range(len(platform[row_idx])):
            if platform[row_idx][col_idx] == "O":
                stones[col_idx] += 1
                platform[row_idx][col_idx] = "."
            elif platform[row_idx][col_idx] == "#":
                while stones[col_idx] > 0:
                    platform[row_idx-stones[col_idx]][col_idx] = "O"
                    stones[col_idx] -= 1
    # east
    stones = [0]*len(platform)
    for col_idx in range(len(platform[0])):
        for row_idx in range(len(platform)):
            if platform[row_idx][col_idx] == "O":
                stones[row_idx] += 1
                platform[row_idx][col_idx] = "."
            elif platform[row_idx][col_idx] == "#":
                while stones[row_idx] > 0:
                    platform[row_idx][col_idx-stones[row_idx]] = "O"
                    stones[row_idx] -= 1


def to_string(platform):
    return "\n".join(["".join(line) for line in platform])


def calc_load(platform_string):
    load = 0
    platform = [list(line) for line in platform_string.split('\n')]
    for row in range(len(platform)-1, -1, -1):
        r = platform[row]
        r = platform[row].count('O')
        load += (len(platform) - row - 1) * r
    return load


def main():
    cycles = []
    with open("14/input.txt") as f:
        platform = [["#"]+list(line.rstrip())+["#"] for line in f]
        platform.append(["#"]*len(platform[0]))
        platform.insert(0, ["#"]*len(platform[0]))
    do_cycle(platform)
    platform_string = to_string(platform)
    while platform_string not in cycles:
        cycles.append(platform_string)
        do_cycle(platform)
        platform_string = to_string(platform)
    period_start = cycles.index(platform_string)
    period_len = len(cycles)-period_start
    result_cycle = cycles[((1000000000-period_start) %
                           period_len)+period_start-1]
    print(calc_load(result_cycle))

    # Kan men fout ni vinden, zie sol.py voor oplossing van internet


if __name__ == "__main__":
    main()
