def main():
    next_rock = []
    load = []
    with open("14/input.txt") as f:
        row_idx = 0
        for row in f:
            load.append(0)
            row = list(row.rstrip())
            if len(next_rock) == 0:
                next_rock = [0]*len(row)
            for col_idx in range(len(row)):
                if row[col_idx] == "O":
                    load[next_rock[col_idx]] += 1
                    next_rock[col_idx] += 1
                elif row[col_idx] == "#":
                    next_rock[col_idx] = row_idx + 1
            row_idx += 1
    total_load = 0
    for i in range(len(load)):
        total_load += (len(load)-i) * load[i]
    print(total_load)


if __name__ == "__main__":
    main()
