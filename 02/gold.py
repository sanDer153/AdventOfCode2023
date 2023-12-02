def main():
    game_powers = []
    with open("02/input.txt") as f:
        for game in f:
            minimal_amount = {"red": 0, "green": 0, "blue": 0}
            game = game.strip().split(': ')
            game = [[tuple(color.split()) for color in draw.split(', ')]
                    for draw in game[1].split('; ')]
            for draw in game:
                for (amount, color) in draw:
                    if int(amount) > minimal_amount[color]:
                        minimal_amount[color] = int(amount)
            game_powers.append(
                minimal_amount["red"]*minimal_amount["green"]*minimal_amount["blue"])
    print(sum(game_powers))


if __name__ == "__main__":
    main()
