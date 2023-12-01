map_dict = {"one": "o1e", "two": "t2o", "three": "th3ee", "four": "fo4r",
            "five": "fi5e", "six": "si6", "seven": "se7en", "eight": "ei8ht", "nine": "n9ne"}


def main():
    calibration_values = []
    with open("01/input.txt") as f:
        for line in f:
            for original, replaced in map_dict.items():
                line = line.replace(original, replaced)
            numbers_in_line = [char for char in line if char.isnumeric()]
            calibration_values.append(
                int("".join([numbers_in_line[0], numbers_in_line[-1]])))
    print(sum(calibration_values))


if __name__ == "__main__":
    main()
