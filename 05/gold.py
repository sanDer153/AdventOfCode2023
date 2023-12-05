def main():
    with open("05/input.txt") as f:
        lines = [line.rstrip() for line in f]
    seeds_pre = list(map(int, lines[0].strip("seeds: ").split()))
    seeds = [(seeds_pre[i], seeds_pre[i]+seeds_pre[i+1])
             for i in range(0, len(seeds_pre), 2)]
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
            to_be_mapped = [(max(seed[0], rule[1]), min(seed[1], rule[1]+rule[2])) for seed in seeds if (
                rule[1] <= seed[0] and seed[0] < rule[1]+rule[2]) or (rule[1] < seed[1] and seed[1] <= rule[1]+rule[2])]
            not_mapped_left = [(seed[0], min(rule[1], seed[1]))
                               for seed in seeds if rule[1] > seed[0]]
            not_mapped_right = [(max(seed[0], rule[1]+rule[2]), seed[1])
                                for seed in seeds if rule[1]+rule[2] < seed[1]]
            seeds = not_mapped_left + not_mapped_right
            mapped.extend(
                list(map((lambda x: (x[0] - rule[1] + rule[0], x[1] - rule[1] + rule[0])), to_be_mapped)))

    mapped.extend(seeds)
    seeds = mapped
    mapped = []

    print(min([x for (x, y) in seeds]))


if __name__ == "__main__":
    main()
