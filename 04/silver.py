def main():
    points = 0
    with open("04/input.txt") as f:
        for card in f:
            card = card.strip().split(": ")[1].split(" | ")
            winning = set(card[0].split())
            scratched = set(card[1].split())
            scratched_winning = winning.intersection(scratched)
            if len(scratched_winning) > 0:
                points += 2**(len(scratched_winning)-1)
    print(points)


if __name__ == "__main__":
    main()
