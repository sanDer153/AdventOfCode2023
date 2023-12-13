def get_row_before_mirror(pattern):
    result = 0
    for row_idx in range(1, len(pattern)):
        symm = True
        smudge_cleared = False
        dist = 0
        while row_idx + dist < len(pattern) and row_idx - dist >= 1 and symm:
            diff = pattern[row_idx+dist] ^ pattern[row_idx-1-dist]
            if diff == 0:
                dist += 1
            elif not smudge_cleared and (diff & (diff-1) == 0) and diff != 0:
                smudge_cleared = True
                dist += 1
            else:
                symm = False
        if symm and smudge_cleared:
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
                    get_row_before_mirror(
                        [int("".join(str(i) for i in bitlist), 2) for bitlist in pattern_rows])
                result += get_row_before_mirror(
                    [int("".join(str(i) for i in bitlist), 2) for bitlist in pattern_cols])
                pattern_rows, pattern_cols = [], []
            else:
                line = list(map(lambda c: toInt[c], list(line)))
                pattern_rows.append(line)
                if len(pattern_cols) == 0:
                    pattern_cols = [[i] for i in line]
                else:
                    for i in range(len(line)):
                        pattern_cols[i].append(line[i])
        result += 100 * get_row_before_mirror(
            [int("".join(str(i) for i in bitlist), 2) for bitlist in pattern_rows])
        result += get_row_before_mirror(
            [int("".join(str(i) for i in bitlist), 2) for bitlist in pattern_cols])
    print(result)


if __name__ == "__main__":
    main()
