# day 6: lanternfish
# https://adventofcode.com/2021/day/6

def read_input():
    with open("input.txt") as fp:
        line = list(map(int, fp.readline().strip().split(',')))
    return line


def p1(lantern_fishes):
    for _ in range(80):
        n = len(lantern_fishes)
        for i in range(n):
            # decrement timer
            lantern_fishes[i] -= 1
            # if -1 reached, reset to 6 and spawn a new lantern fish
            if lantern_fishes[i] == -1:
                lantern_fishes[i] = 6
                lantern_fishes.append(8)
    return len(lantern_fishes)


def p2(lantern_fishes):
    """
    The solution used for part 1 is no longer fast enough for 256 days.
    Here, another approach is used instead of decrementing each timer in the list one by one
    :param lantern_fishes: a list of current internal timers for every lantern fish
    :return: the number of lantern fishes after 256 days
    """

    # stores the counts of lantern fishes with each internal timer value
    # key -> internal timer number; value -> the number of fishes
    counts = dict.fromkeys([0, 1, 2, 3, 4, 5, 6, 7, 8])

    # populate dict from puzzle input
    for k in counts.keys():
        counts[k] = lantern_fishes.count(k)

    # simulate 256 days
    for _ in range(256):
        # the number of lantern fish that will be spawned
        spawned_count = counts[0]

        # decrement internal timer by shifting the counts to a lower key
        for k in range(1, 8+1):
            counts[k-1] = counts[k]

        # reset internal timer to 6 for fishes that just gave birth
        counts[6] += spawned_count

        # add new lantern fishes with internal timer of 8
        counts[8] = spawned_count

    return sum(counts.values())


if __name__ == "__main__":
    all_fishes = read_input()
    print(p1(all_fishes))
    print(p2(all_fishes))
