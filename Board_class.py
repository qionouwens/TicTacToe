class Board:
    ex = "X"
    o = "O"

    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.available = [True, True, True, True, True, True, True, True, True]
        self.whose_turn = self.ex

    def is_winner(self):
        if self.board[0] != ' ':
            # Top row
            if self.board[0] == self.board[1] == self.board[2]:
                return self.board[0]
            # Diagonal from top left to bottom right
            if self.board[0] == self.board[4] == self.board[8]:
                return self.board[0]
            # Left Column
            if self.board[0] == self.board[3] == self.board[6]:
                return self.board[0]
        if self.board[4] != ' ':
            # Middle Column
            if self.board[1] == self.board[4] == self.board[7]:
                return self.board[4]
            # Diagonal from top right to bottom left
            if self.board[2] == self.board[4] == self.board[6]:
                return self.board[4]
            # Middle row
            if self.board[3] == self.board[4] == self.board[5]:
                return self.board[4]
        if self.board[8] != ' ':
            # Bottom Row
            if self.board[6] == self.board[7] == self.board[8]:
                return self.board[8]
            # Right Column
            if self.board[2] == self.board[5] == self.board[8]:
                return self.board[8]
        if self.available == [False, False, False, False, False, False, False, False, False]:
            return "draw"
        else:
            return ""

    def print_board(self):
        print("   |   |   ")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("   |   |   ")

    def turn(self, cell):
        if self.available[cell]:
            self.board[cell] = self.whose_turn
            self.available[cell] = False
            if self.whose_turn == self.ex:
                self.whose_turn = self.o
            else:
                self.whose_turn = self.ex
            return True
        else:
            return False


