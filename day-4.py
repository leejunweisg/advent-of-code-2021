# day 4: giant squid
# https://adventofcode.com/2021/day/4

def read_input():
    boards_list = []
    with open("input.txt") as fp:
        # read sequence (first line)
        sequence_list = list(map(int, fp.readline().strip().split(',')))

        # read and create board objects
        while fp.readline() != '':
            # read 5 rows at a time
            board = [list(map(int, fp.readline().split())) for _ in range(5)]
            # create board object
            boards_list.append(Board(board))

    return sequence_list, boards_list


class Board:
    """
    Represents a 5x5 bingo board
    """
    def __init__(self, board: []):
        self.board = board
        self.state = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.won = False  # for part 2

    def update(self, num) -> None:
        """
        Updates the state of the bingo board (marked/unmarked)
        :param num: the current number
        :return: None
        """
        for row in range(5):
            for col in range(5):
                if self.board[row][col] == num:
                    self.state[row][col] = 1

    def bingo(self) -> bool:
        """
        Checks if a BINGO is achieved
        :return: True if BINGO, else False
        """
        # horizontal
        for row in self.state:
            if sum(row) == 5:
                self.won = True
                return True
        # vertical
        for col in range(5):
            if sum([x[col] for x in self.state]) == 5:
                self.won = True
                return True
        return False

    def score(self, num) -> int:
        """
        Calculates the score of the board (sum of unmarked numbers * latest number called)
        :param num: latest number called
        :return: score
        """
        total = 0
        for row in range(5):
            for col in range(5):
                if self.state[row][col] == 0:
                    total += self.board[row][col]
        return total * num

    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += f"{row}\n"
        return board_str


def p1(sequence_list, boards_list):
    # for every number in the sequence, update each board and check for win
    for n in sequence_list:
        for b in boards_list:
            # update the board's state with the latest number called
            b.update(n)

            # check for bingo
            if b.bingo():
                # return the score of the first BINGO-ed board
                return b.score(n)


def p2(sequence_list, boards_list):
    score = -1

    # for every number in the sequence, update each board and check for win
    for n in sequence_list:
        for b in boards_list:
            # skip bingo boards that already won, as we want to get the score of the last board that wins
            if b.won:
                continue

            # update the board's state with the latest number called
            b.update(n)

            # check for bingo
            if b.bingo():
                # set score to the score of the latest winning board
                score = b.score(n)
    return score


if __name__ == "__main__":
    sequence, boards = read_input()
    print(p1(sequence, boards))
    print(p2(sequence, boards))
