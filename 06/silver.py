INPUT = [(58, 434), (81, 1041), (96, 2219), (76, 1218)]


def main():
    result = 1
    for (time, record) in INPUT:
        possibilities = 0
        for time_on_button in range(time+1):
            if record < time_on_button*(time-time_on_button):
                possibilities += 1
        result *= possibilities
    print(result)


if __name__ == "__main__":
    main()
