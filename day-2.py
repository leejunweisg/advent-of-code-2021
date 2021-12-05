def read_input():
    with open("input.txt") as fp:
        lines = fp.read().splitlines()
    return lines


def p1(lines):
    horizontal = 0
    depth = 0

    for line in lines:
        direction, num = tuple(line.split(" "))
        num = int(num)
        if direction == 'forward':
            horizontal += num
        elif direction == 'down':
            depth += num
        else:
            depth -= num

    return horizontal * depth


def p2(lines):
    aim = 0
    horizontal = 0
    depth = 0

    for line in lines:
        direction, num = tuple(line.split(" "))
        num = int(num)
        if direction == 'down':
            aim += num
        elif direction == 'up':
            aim -= num
        else:
            horizontal += num
            depth += (aim * num)

    return horizontal * depth


if __name__ == "__main__":
    content = read_input()
    print(p1(content))
    print(p2(content))
