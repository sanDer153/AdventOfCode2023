from math import ceil, floor, sqrt

INPUT = (58819676, 434104122191218)
# INPUT = (71530, 940200)


def main():
    time, record = INPUT
    lower = ceil((-1*time+sqrt(time**2-4*record))/-2)
    upper = floor((-1*time-sqrt(time**2-4*record))/-2)
    print(upper - lower + 1)


if __name__ == "__main__":
    main()
