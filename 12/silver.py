def complete_row(springs, pattern):
    possible = [springs]
    solutions = []
    while len(possible) > 0:
        current = possible.pop(0)
        pattern_idx = 0
        broken_len = 0
        accepted = True
        for idx in range(len(current)):
            if current[idx] == ".":
                if broken_len > 0 and broken_len < pattern[pattern_idx]:
                    accepted = False
                    break
                elif broken_len > 0 and broken_len == pattern[pattern_idx]:
                    pattern_idx += 1
                broken_len = 0
            elif current[idx] == "#":
                broken_len += 1
                if pattern_idx == len(pattern) or broken_len > pattern[pattern_idx]:
                    accepted = False
                    break
            elif current[idx] == "?":
                if broken_len > 0 and broken_len < pattern[pattern_idx]:
                    current[idx] = "#"
                    broken_len += 1
                elif broken_len > 0 and broken_len == pattern[pattern_idx]:
                    current[idx] = "."
                    pattern_idx += 1
                    broken_len = 0
                elif broken_len == 0:
                    option1 = current.copy()
                    option1[idx] = "#"
                    possible.append(option1)
                    option2 = current.copy()
                    option2[idx] = "."
                    possible.append(option2)
                    accepted = False
                    break
        if pattern_idx == len(pattern) - 1 and broken_len != pattern[pattern_idx] or pattern_idx < len(pattern) - 1:
            accepted = False
        if accepted:
            solutions.append(current)
    return solutions


def main():
    total = 0
    with open("12/input.txt") as f:
        for line in f:
            line = line.strip().split(" ")
            springs = list(line[0])
            pattern = list(map(int, line[1].split(",")))
            solutions = complete_row(springs, pattern)
            total += len(solutions)
    print(total)


if __name__ == "__main__":
    main()
