def main():
    calibration_values = []
    with open("01/input.txt") as f:
        for line in f:
            numbers_in_line = [char for char in line if char.isnumeric()]
            calibration_values.append(
                int("".join([numbers_in_line[0], numbers_in_line[-1]])))
    print(sum(calibration_values))


if __name__ == "__main__":
    main()
