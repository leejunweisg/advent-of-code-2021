# day 5: hydrothermal venture
# https://adventofcode.com/2021/day/5

def read_input():
    lines = []
    with open("input.txt") as fp:
        for line in fp:
            lines.append(line.strip())
    return lines


class OceanFloor:
    def __init__(self):
        self.danger_areas = {}

    def process_line(self, line: str, ignore_diagonal=True) -> None:
        start, end = line.split(" -> ")
        x1, y1 = tuple(map(int, start.split(',')))
        x2, y2 = tuple(map(int, end.split(',')))

        # determine type of line (straight or diagonal)
        # straight
        if (x1 == x2) or (y1 == y2):
            self.process_straight(x1, y1, x2, y2)
        # diagonal
        elif not ignore_diagonal:
            self.process_diagonal(x1, y1, x2, y2)

    def process_straight(self, x1, y1, x2, y2):
        # swap the two points if start point is larger than end point
        if x2 < x1 or y2 < y1:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        # mark points
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.mark_point(x, y)

    def process_diagonal(self, x1, y1, x2, y2):
        x, y = x1, y1

        while True:
            # mark point
            self.mark_point(x, y)

            # break when all points marked
            if x == x2 and y == y2:
                break

            # increment or decrement based on direction of line
            if x1 < x2:  # left to right
                x += 1
            else:  # right to left
                x -= 1
            if y1 < y2:  # down to up
                y += 1
            else:  # up to down
                y -= 1

    def mark_point(self, x: int, y: int) -> None:
        # get str representation of point
        point_str = f"{x},{y}"

        # add key if point does not exist yet
        if point_str not in self.danger_areas:
            self.danger_areas[point_str] = 0

        # increment danger by 1
        self.danger_areas[point_str] += 1

    def count_danger(self, threshold=2) -> int:
        count = 0
        for v in self.danger_areas.values():
            if v >= threshold:
                count += 1
        return count


def p1(lines):
    # create ocean floor object
    of = OceanFloor()

    # process each danger line, ignoring diagonal lines
    for line in lines:
        of.process_line(line)

    # return number of danger areas with at least 2 overlap
    return of.count_danger(threshold=2)


def p2(lines):
    # create ocean floor object
    of = OceanFloor()

    # process each danger line
    for line in lines:
        of.process_line(line, ignore_diagonal=False)

    # return number of danger areas with at least 2 overlap
    return of.count_danger(threshold=2)


if __name__ == "__main__":
    content = read_input()
    print(p1(content))
    print(p2(content))
