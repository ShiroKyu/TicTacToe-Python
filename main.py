from ticTacToe import Board

tab = Board()
playAgain = True

while playAgain:

    tab.displayBoard()

    tab.playerMove()
    if tab.winner(tab.board, 'X'):
        print('Você ganhou.')
        tab.displayBoard()
        break

    tab.machineMove()
    if tab.winner(tab.board, 'O'):
        print('A máquina ganhou.')
        tab.displayBoard()
        break

    if tab.isFilled():
        break
