from Box import Box

BOARD_SIZE = 2
class Board:
    def __init__(self):
        self.board = list()
        for i in range(BOARD_SIZE):
            row = list()
            for j in range(BOARD_SIZE):
                box = Box()
                row.append(box)
            self.board.append(row)

    def print_board(self):
        for row in self.board:
            for box in row:
                print(box.rune, end=" ")
            print("")
