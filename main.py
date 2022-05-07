import chess as ch

def main():
    myBoard = ch.Board()
    print(myBoard.place(ch.Coord('a1'), ch.Pawn(ch.BLACK)))

if __name__ == '__main__': main()