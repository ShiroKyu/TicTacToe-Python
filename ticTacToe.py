from random import choice
from os import system


class Board:
    def __init__(self):
        self.board = [' ' for x in range(9)]

    def displayBoard(self):
        system('clear') or None

        print()
        print(f'{self.board[0]}  |  {self.board[1]}  | {self.board[2]}')
        print(f'{self.board[3]}  |  {self.board[4]}  | {self.board[5]}')
        print(f'{self.board[6]}  |  {self.board[7]}  | {self.board[8]}')
        print()

    def emptySpace(self, pos):
        return self.board[pos] == ' '

    def playerMove(self):
        while True:
            try:
                pos = int(input('Informe uma posição para jogar de 1-9: ')) - 1

                if pos < 0 or pos > 8:
                    print('Posição inválida.')
                    continue

                if self.emptySpace(pos):
                    self.insertMove(self.board, pos, 'X')
                    return

                else:
                    print('Posição já usada.')
                    continue

            except:
                print('Erro, valor em branco')

    def machineMove(self):
        # Movimentos possiveis
        possibleMoves = [x for x, _ in enumerate(
            self.board) if self.board[x] == ' ']

        # Se não houver movimentos possiveis, EMPATE
        if not possibleMoves:
            print('Empate.')
            return

        # Verificar se a máquina pode fazer uma jogada vencedora, se puder, o faça
        # verificar se o jogador pode fazer uma jogada vencedora, se puder, bloqueie
        for i in ['O', 'X']:
            for move in possibleMoves:
                cpyBoard = self.board[:]
                self.insertMove(cpyBoard, move, i)

                if self.winner(cpyBoard, i):
                    self.insertMove(self.board, move, 'O')
                    return

        move = choice(possibleMoves)
        self.insertMove(self.board, move, 'O')

    def winner(self, board, letter):
        return ((board[0] == letter and board[1] == letter and board[2] == letter) or
                (board[3] == letter and board[4] == letter and board[5] == letter) or
                (board[6] == letter and board[7] == letter and board[8] == letter) or
                (board[0] == letter and board[4] == letter and board[8] == letter) or
                (board[2] == letter and board[4] == letter and board[6] == letter) or
                (board[0] == letter and board[3] == letter and board[6] == letter) or
                (board[1] == letter and board[4] == letter and board[7] == letter) or
                (board[2] == letter and board[5]
                 == letter and board[8] == letter))

    def insertMove(self, board, pos, letter):
        board[pos] = letter

    def isFilled(self):
        cont = 0

        for i in range(9):
            if not self.emptySpace(i):
                cont += 1

        if cont == 9:
            return True
        return False

