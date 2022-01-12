# day 7: the treachery of whales
# https://adventofcode.com/2021/day/7

def read_input():
    with open("input.txt") as fp:
        line = list(map(int, fp.readline().strip().split(',')))
    return line


def p1(positions) -> int:
    # store the lowest cost required
    lowest_cost = -1

    # iterate through each potential position
    for i in range(min(positions), max(positions)+1):

        # calculate the total cost for this position for all crabs
        cost = 0
        for crab in positions:
            cost += abs(i-crab)

        # store the current cost if it is lower than the previous lowest cost
        if cost < lowest_cost or lowest_cost == -1:
            lowest_cost = cost

    return lowest_cost


def p2(positions) -> int:
    """
    Same as P1, but cost calculation modified to sum(), and added memoization to reduce computation time
    :param positions: list of crab positions
    :return: the lowest cost
    """
    # store the lowest cost required
    lowest_cost = -1

    # iterate through each potential position
    for i in range(min(positions), max(positions)+1):
        # calculate the total cost for this position for all crabs
        cost = 0
        crab_cost = {}  # memoization
        for crab in positions:
            if crab in crab_cost:
                cost += crab_cost[crab]
            else:
                temp_cost = sum(range(1, abs(i - crab)+1))
                cost += temp_cost
                crab_cost[crab] = temp_cost

        # store the current cost if it is lower than the previous lowest cost
        if cost < lowest_cost or lowest_cost == -1:
            lowest_cost = cost

    return lowest_cost


if __name__ == "__main__":
    crabs = read_input()
    print(p1(crabs))
    print(p2(crabs))
