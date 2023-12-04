def main():
    cards_amount = []
    with open("04/input.txt") as f:
        cards_amount = [1]*202
        for card in f:
            card = card.strip().split(": ")
            card_idx = int(card[0].strip("Card").strip()) - 1
            result = card[1].split(" | ")
            winning = set(result[0].split())
            scratched = set(result[1].split())

            scratched_winning = winning.intersection(scratched)
            amount_won = len(scratched_winning)
            for i in range(1, min(amount_won+1, len(cards_amount)-card_idx)):
                cards_amount[card_idx+i] += cards_amount[card_idx]
    print(sum(cards_amount))


if __name__ == "__main__":
    main()
