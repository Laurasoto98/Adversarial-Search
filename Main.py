import Square
from MiniMax import MiniMax
from TicTacToeAction import TicTacToeAction
from TicTacToeState import TicTacToeState

if __name__ == '__main__':
    print("\nWelcome to Tic Tac Toe!")
    print("The squares are numbered as follows:")
    print(" ---+---+---\n| 1 | 2 | 3 |\n ---+---+---\n| 4 | 5 | 6 |\n ---+---+---\n| 7 | 8 | 9 |\n ---+---+---\n")
    mark=False
    print("What algorithm do you want to use? ")
    print("MiniMax = 1 | AlphaBetaSearch = 2")
    use=(int)(input())
    if use == 2:
        mark=True
    print("Who should start?")
    print("You = 1 | Computer = 2 ")
    temp =(int)(input())
    s = TicTacToeState()
    s.player = Square.X
    if (temp == 1):
        s.playerToMove = Square.O
    else :
        s.playerToMove = Square.X
    while (True):
        if (s.playerToMove == Square.X):
            minimax=MiniMax()
            print('Computer Player:')
            s = s.getResult(minimax.MinimaxDecision(s, mark))
        else :
            print("Which square do you want to set? (1--9) ", end=' ')
            while (True):
                temp = (int)(input())
                if  temp >= 1 & temp <= 9 :
                     break
            a = TicTacToeAction(Square.O, temp - 1)
            s = s.getResult(a)
            print('Human Player:')
        s.printresult()
        if  s.isTerminal():
            break
    if s.getUtility()==-1:
        print("Congratulation the Winner is: \nHuman Player!")
    elif s.getUtility()==1 :
        print("Congratulation the Winner is: \nComputer Player!")
    else:
        print("It's a tie!")
