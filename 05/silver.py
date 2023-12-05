def main():
    with open("05/input.txt") as f:
        lines = [line.rstrip() for line in f]
    seeds = list(map(int, lines[0].strip("seeds: ").split()))
    mapped = []
    for rule in lines[1:]:
        if "map:" in rule:
            continue
        elif rule == '':
            mapped.extend(seeds)
            seeds = mapped
            mapped = []
        else:
            rule = list(map(int, rule.split()))
            to_be_mapped = [seed for seed in seeds if seed -
                            rule[1] >= 0 and seed - rule[1] < rule[2]]
            not_mapped = [seed for seed in seeds if seed -
                          rule[1] < 0 or seed - rule[1] >= rule[2]]
            seeds = not_mapped
            mapped.extend(
                list(map((lambda x: x - rule[1] + rule[0]), to_be_mapped)))

    mapped.extend(seeds)
    seeds = mapped
    mapped = []

    print(min(seeds))


if __name__ == "__main__":
    main()
