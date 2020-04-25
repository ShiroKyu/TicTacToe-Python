class Board:
    def __init__(self):
        self.board = [' ' for x in range(9)]

    def displayBoard(self):
        print(f'{self.board[0]}  |  {self.board[1]}  | {self.board[2]}')
        print(f'{self.board[3]}  |  {self.board[4]}  | {self.board[5]}')
        print(f'{self.board[6]}  |  {self.board[7]}  | {self.board[8]}')

    def emptySpace(self, pos):
        return self.board[pos] == ''

    def playerMove(self):
        pass

    def machineMove(self):
        pass

    def winner(self, letter):
        return ((self.board[0] == letter and self.board[1] == letter and self.board[2] == letter) or
                (self.board[3] == letter and self.board[4] == letter and self.board[5] == letter) or
                (self.board[6] == letter and self.board[7] == letter and self.board[8] == letter) or
                (self.board[0] == letter and self.board[4] == letter and self.board[8] == letter) or
                (self.board[2] == letter and self.board[4] == letter and self.board[6] == letter) or
                (self.board[0] == letter and self.board[3] == letter and self.board[6] == letter) or
                (self.board[1] == letter and self.board[4] == letter and self.board[7] == letter) or
                (self.board[2] == letter and self.board[5]
                 == letter and self.board[8] == letter))

    def insertMove(self, pos, letter):
        self.board[pos] = letter
