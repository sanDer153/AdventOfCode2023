def main():
    total_predictions = 0
    with open("09/input.txt") as f:
        measurements = [list(map(int, line.strip().split()))for line in f]
    for measurement in measurements:
        decomposition = [measurement]
        while not all(x == 0 for x in decomposition[-1]):
            decomposition.append([decomposition[-1][i] - decomposition[-1][i-1]
                                 for i in range(1, len(decomposition[-1]))])
        decomposition[-1] = [0] + decomposition[-1]
        for i in range(len(decomposition)-2, -1, -1):
            decomposition[i] = [decomposition[i][0] -
                                decomposition[i+1][0]] + decomposition[i]
        total_predictions += decomposition[0][0]

    print(total_predictions)


if __name__ == "__main__":
    main()
