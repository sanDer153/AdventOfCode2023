max_cubes = {"red": 12, "green": 13, "blue": 14}


def main():
    possible_games = []
    with open("02/input.txt") as f:
        for game in f:
            possible = True
            game = game.strip().split(': ')
            game_number = int(game[0].strip("Game "))
            game = [[tuple(color.split()) for color in draw.split(', ')]
                    for draw in game[1].split('; ')]
            for draw in game:
                for (amount, color) in draw:
                    if int(amount) > max_cubes[color]:
                        possible = False
            if possible:
                possible_games.append(game_number)
    print(sum(possible_games))


if __name__ == "__main__":
    main()
