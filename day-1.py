# day 1: sonar sweep

def read_input():
    lines = []
    with open("input.txt") as fp:
        for line in fp:
            lines.append(line.strip())

    lines = list(map(int, lines))
    return lines


def p1(lines):
    increased = 0
    for i in range(len(lines) - 1):
        if int(lines[i + 1]) > int(lines[i]):
            increased += 1
    return increased


def p2(lines):
    increased = 0
    for i in range(len(lines) - 3):
        window1 = lines[i:i + 3]
        window2 = lines[i + 1:i + 4]
        if sum(window2) > sum(window1):
            increased += 1
    return increased


if __name__ == "__main__":
    content = read_input()
    print(p1(content))
    print(p2(content))
