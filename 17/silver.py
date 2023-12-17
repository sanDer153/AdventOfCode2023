from heapq import *
from collections import defaultdict


def calc_heat_loss(grid, move_range, end_move_len):
    end = max(x.real for x in grid) + 1j * max(y.imag for y in grid)
    best = defaultdict(lambda: defaultdict(lambda: 1 << 16))

    def dirs(m): return [-1j, 1j] if m.real else ([-1, 1]
                                                  if m.imag else [1, 1j])
    i, q = 1, [(0, 0, 0, [0])]

    while True:
        heat_loss, _, momentum, path = heappop(q)
        cur = path[-1]

        if cur == end:
            if not end_move_len or end_move_len in [momentum.real, momentum.imag]:
                return heat_loss
            continue

        for d in dirs(momentum):
            th, tp = heat_loss, path
            for x in range(1, min(move_range)):
                if cur + x * d in grid:
                    th, tp = th + grid[cur + x * d], tp + [cur + d * x]
            for x in move_range:
                if cur + x * d in grid:
                    th, tp, i = th + grid[cur + x *
                                          d], tp + [cur + d * x], i + 1
                    if th < best[cur + x * d][d]:
                        q.append((th, i, d * x, tp))
                        best[cur + x * d][d] = th


def main():
    with open("17/input.txt") as f:
        grid = {x + y * 1j: int(c) for y, l in enumerate(f)
                for x, c in enumerate(l.strip())}
    print(calc_heat_loss(grid, range(1, 4), 0))


if __name__ == "__main__":
    main()
