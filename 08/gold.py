from functools import reduce
from math import lcm


STR = "LRRLRRLRRRLRLLRRRLLRRRLRLRRRLRLRRLRRRLRRRLRLRRRLRRRLRRLRRRLLLRLRRRLRRRLRRRLRLRLRRLLRRRLRLLRLRRRLRRLLRLRLRRLRRRLRRLLRLRRRLLRRLRRRLRLRRLLRRRLRRLLRRLRRRLRLRRRLRRLRRRLRRRLRRLRRRLRLRRLRRRLRRRLRRLLRLRRLRRLRRRLRLLLRRRLLRRRLRLRRRLRLRRLRRRLLLRLRRRLRLRRLRRRLRRRLRRLRLRLRRRR"
PROG = list(map((lambda x: 0 if x == "L" else 1), list(STR)))


def find_pattern(start, network):
    step = 0
    timeline = [(start, step)]
    current_node = start
    next_node = network[current_node][PROG[step % len(PROG)]]
    while (next_node, step % len(PROG)) not in timeline:
        timeline.append((next_node, step % len(PROG)))
        current_node = next_node
        step += 1
        next_node = network[current_node][PROG[step % len(PROG)]]
    period_start = timeline.index((next_node, step % len(PROG)))
    start_path = timeline[:period_start]
    period = timeline[period_start:]
    period_start_to_z = [period.index(node)
                         for node in timeline if node[0][-1] == "Z"]
    return len(start_path), len(period), period_start_to_z


def main():
    network = dict()
    with open("08/input.txt") as f:
        for line in f:
            line = line.strip().split(" = ")
            current_node = line[0]
            paths = tuple(line[1].strip(")").strip("(").split(", "))
            network[current_node] = paths
    # period_data = list(map(lambda x: find_pattern(x, network), [
        # node for node in network.keys() if node[-1] == "A"]))
    period_data = [(4, 16043, [16039]), (2, 20777, [20775]), (6, 13939, [
        13933]), (2, 18673, [18671]), (4, 11309, [11305]), (2, 17621, [17619])]
    periods = list(map(lambda x: x[1], period_data))
    steps_to_finish = list(map(lambda x: x[0] + x[2][0], period_data))
    print(lcm(16043, 20777, 13939, 18673, 11309, 17621))


if __name__ == "__main__":
    main()
