def HASH(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def main():
    solution = 0
    with open("15/input.txt") as f:
        for s in f.readlines()[0].split(','):
            solution += HASH(s)

    print(solution)


if __name__ == "__main__":
    main()
