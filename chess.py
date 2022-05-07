from __future__ import annotations
from enum import Enum, auto

class Color(Enum):
    BLACK = auto()
    WHITE = auto()

class PieceType(Enum):
    PAWN   = auto()
    KNIGHT = auto()
    BISHOP = auto()
    ROOK   = auto()
    QUEEN  = auto()
    KING   = auto()

BLACK  = Color.BLACK
WHITE  = Color.WHITE

PAWN   = PieceType.PAWN
KNIGHT = PieceType.KNIGHT
BISHOP = PieceType.BISHOP
ROOK   = PieceType.ROOK
QUEEN  = PieceType.QUEEN
KING   = PieceType.KING

class Piece:
    def __init__(self, piece: PieceType, color: Color) -> None:
        self.piece = piece
        self.color = color
    
    def __repr__(self):
        return f'{self.color.name} {self.piece.name}'

class Pawn(Piece):
    def __init__(self, color: Color):
        super().__init__(self, PAWN, color)

class Knight(Piece):
    def __init__(self, color: Color):
        super().__init__(self, KNIGHT, color)

class Bishop(Piece):
    def __init__(self, color: Color):
        super().__init__(self, BISHOP, color)

class Rook(Piece):
    def __init__(self, color: Color):
        super().__init__(self, ROOK, color)

class Queen(Piece):
    def __init__(self, color: Color):
        super().__init__(self, QUEEN, color)

class King(Piece):
    def __init__(self, color: Color):
        super().__init__(self, KING, color)

class Coord:
    def __init__(self, coord: str) -> None:
        if len(coord) != 2:            raise ValueError('invalid coord length')
        if coord[0] not in 'abcdefgh': raise ValueError('invalid file')
        if coord[1] not in '12345678': raise ValueError('invalid rank')
    
        self.coord = (coord[0], coord[1])
        self.file, self.rank = self.coord

class Board:
    def __init__(self) -> None:
        self._board = {file: {rank: None for rank in '12345678'} for file in 'abcdefgh'}
        
    def place(self, coord: Coord, piece: Piece) -> Board:
        file, rank = coord.coord
        self._board[file][rank] = piece
        return self
    
    def __repr__(self) -> str:
        return str(self._board)
