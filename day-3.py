# day 3: binary diagnostic

def read_input():
    lines = []
    with open("input.txt") as fp:
        for line in fp:
            lines.append(line.strip())
    return lines


def p1(lines):
    # initialize gamma and epsilon to lists of Nones
    n_bits = len(lines[0])
    gamma = [None] * n_bits
    epsilon = [None] * n_bits

    # count number of zeroes and ones for each position
    for pos in range(n_bits):
        n_zeroes = len([x[pos] for x in lines if x[pos] == "0"])
        n_ones = len(lines) - n_zeroes

        # set gamma and epsilon based on the number of zeroes and ones in the position
        gamma[pos] = '0' if n_zeroes > n_ones else '1'
        epsilon[pos] = '1' if n_zeroes > n_ones else '0'

    # convert binary string to integer
    gamma = int(''.join(map(str, gamma)), 2)
    epsilon = int(''.join(map(str, epsilon)), 2)

    return gamma * epsilon


def p2(lines):
    n_bits = len(lines[0])
    oxygen = lines.copy()
    co2 = lines.copy()

    # count number of zeroes and ones for each position, and filter
    for pos in range(n_bits):
        if len(oxygen) > 1:
            # count number of zeroes and ones
            n_zeroes_oxygen = len([x[pos] for x in oxygen if x[pos] == "0"])
            n_ones_oxygen = len(oxygen) - n_zeroes_oxygen

            # determine filter to use
            oxygen_filter = '1' if n_zeroes_oxygen <= n_ones_oxygen else '0'

            # filter
            oxygen = list(filter(lambda x: (x[pos] == oxygen_filter), oxygen))

        if len(co2) > 1:
            # count number of zeroes and ones
            n_zeroes_co2 = len([x[pos] for x in co2 if x[pos] == "0"])
            n_ones_co2 = len(co2) - n_zeroes_co2

            # determine filter to use
            co2_filter = '0' if n_zeroes_co2 <= n_ones_co2 else '1'

            # filter
            co2 = list(filter(lambda x: (x[pos] == co2_filter), co2))

    # convert binary string to integer
    oxygen_int = int(oxygen[0], 2)
    co2_int = int(co2[0], 2)

    return oxygen_int * co2_int


if __name__ == "__main__":
    content = read_input()
    print(p1(content))
    print(p2(content))
