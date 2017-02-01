# Submission: SUCCESSFUL. Completed in: 3 hrs, 51 mins, 53 secs.

NUM_ROWS = 8
NUM_COLS = 8

# up-left indicates the move that is 2 squares up and 1 square to left.
# Likewise, left-up indicates the move that is 2 squares left and 1 square up
# And so on...

MOVE_DELTAS = [ 
                (-1, -2), # left-up
                (-2, -1), # up-left
                (-2, +1), # up-right
                (-1, +2), # right-up
                (+1, +2), # right-down
                (+2, +1), # down-right
                (+2, -1), # down-left
                (+1, -2), # left-down
                          ]

from collections import deque

''' PRECONDITION: src and dst are each in range(0, NUM_ROWS*NUM_COLS) '''
def answer(src, dst):
    
    if src == dst:
        return 0
    
    minNumMoves = Board(NUM_ROWS, NUM_COLS, None)
    # For square sq with row == r and col == c,
    #   minNumMoves[sq] == minNumMoves.board[r][c] == the min num of moves to get
    #   from the source square, srcSquare,
    #   to sq the square with coords (r, c) if that value is known.
    #
    # While that value is unknown, minNumMoves[sq] == None.
    
    srcSquare = Square.fromNum(src, board = minNumMoves)
    dstSquare = Square.fromNum(dst, board = minNumMoves)
    
    minNumMoves[srcSquare] = 0
    
    squares = deque([srcSquare]) # squares queue, notice that by the time a square, sq, is added to squares, minNumMoves[sq] is known 
    
    # We will do a BFS walk using a the squares queue.
    # This will guarantee that for every int n >= 0,
    #   all paths of n moves are explored before
    #   any path of n+1 moves is explored.
    # This means that the first path that we encounter
    # that land us on the destination square, dstSquare,
    # is guaranteed to be a shortest path.
    
    while squares:
        
        square = squares.popleft()
        min_num_moves_to_square = minNumMoves[square]
        
        for delta in MOVE_DELTAS:
            newSquare = _process(square, delta, minNumMoves, min_num_moves_to_square, squares, dstSquare)
            if newSquare == dstSquare:
                return minNumMoves[newSquare]
    
    raise ValueError("Inputs src and dst must each be in range(0, {0})".format(NUM_ROWS*NUM_COLS))

# In the future, decompose this helper function into smaller functions.
# As it is, this function does a lot!!!
def _process(square, delta, minNumMoves, min_num_moves_to_square, squares, dstSquare):
    
    newSquare = square.moveBy(delta)
    
    if newSquare.isInBoundsOf(board = minNumMoves) and minNumMoves[newSquare] is None:
        
        min_num_moves_to_newSquare = min_num_moves_to_square + 1
        minNumMoves[newSquare]     = min_num_moves_to_newSquare
        squares.append(newSquare)
    
    return newSquare

class Square(object):
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
    
    @classmethod
    def fromNum(cls, num, board):
        num_cols = board.getNumCols()
        row = num / num_cols
        col = num % num_cols
        return cls(row, col)
    
    def __eq__(self, other):
        
        if not isinstance(other, self.__class__):
            return False
        
        return self.row == other.row and self.col == other.col
    
    def getRowColPair(self):
        return (self.row, self.col)
    
    # returns new square, does not self
    def moveBy(self, delta):
        ROW, COL = 0, 1 # indeces into the delta tuple
        new_row = self.row + delta[ROW]
        new_col = self.col + delta[COL]
        return Square(new_row, new_col)
    
    def isInBoundsOf(self, board):
        num_rows, num_cols = board.getNumRowsNumColsPair()
        return 0 <= self.row < num_rows and 0 <= self.col < num_cols

class Board(object):
    
    def __init__(self, num_rows, num_cols, default_value = None):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = [ [default_value]*num_cols for _ in range(num_rows) ]
    
    def getNumRows(self):
        return self.num_rows
    
    def getNumCols(self):
        return self.num_cols
    
    def getNumRowsNumColsPair(self):
        return (self.num_rows, self.num_cols)
    
    def __getitem__(self, square):
        r, c = square.getRowColPair()
        return self.board[r][c]
    
    def __setitem__(self, square, val):
        r, c = square.getRowColPair()
        self.board[r][c] = val

# TESTS

# print answer(19,36) == 1
# print answer( 0, 1) == 3