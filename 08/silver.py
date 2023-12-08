STR = "LRRLRRLRRRLRLLRRRLLRRRLRLRRRLRLRRLRRRLRRRLRLRRRLRRRLRRLRRRLLLRLRRRLRRRLRRRLRLRLRRLLRRRLRLLRLRRRLRRLLRLRLRRLRRRLRRLLRLRRRLLRRLRRRLRLRRLLRRRLRRLLRRLRRRLRLRRRLRRLRRRLRRRLRRLRRRLRLRRLRRRLRRRLRRLLRLRRLRRLRRRLRLLLRRRLLRRRLRLRRRLRLRRLRRRLLLRLRRRLRLRRLRRRLRRRLRRLRLRLRRRR"
PROG = list(map((lambda x: 0 if x == "L" else 1), list(STR)))


def main():
    network = dict()
    with open("08/input.txt") as f:
        for line in f:
            line = line.strip().split(" = ")
            current_node = line[0]
            paths = tuple(line[1].strip(")").strip("(").split(", "))
            network[current_node] = paths
    step = 0
    current_node = "AAA"
    while current_node != "ZZZ":
        current_node = network[current_node][PROG[step % len(PROG)]]
        step += 1
    print(step)


if __name__ == "__main__":
    main()
