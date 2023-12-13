def get_row_before_mirror(pattern):
    result = 0
    for row_idx in range(1, len(pattern)):
        symm = True
        dist = 0
        while row_idx + dist < len(pattern) and row_idx - dist >= 1 and symm:
            if pattern[row_idx+dist] != pattern[row_idx-1-dist]:
                symm = False
            else:
                dist += 1
        if symm:
            result += row_idx
    return result


def main():
    toInt = {".": 0, "#": 1}
    result = 0
    with open("13/input.txt") as f:
        pattern_rows, pattern_cols = [], []
        for line in f:
            line = line.rstrip()
            if line == "":
                result += 100 * \
                    get_row_before_mirror(list(map(tuple, pattern_rows)))
                result += get_row_before_mirror(list(map(tuple, pattern_cols)))
                pattern_rows, pattern_cols = [], []
            else:
                line = list(map(lambda c: toInt[c], list(line)))
                pattern_rows.append(line)
                if len(pattern_cols) == 0:
                    pattern_cols = [[i] for i in line]
                else:
                    for i in range(len(line)):
                        pattern_cols[i].append(line[i])
        result += 100 * get_row_before_mirror(list(map(tuple, pattern_rows)))
        result += get_row_before_mirror(list(map(tuple, pattern_cols)))
    print(result)


if __name__ == "__main__":
    main()
