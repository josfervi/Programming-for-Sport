# my_solution-refactored-before_stackexchange_code_review.py

# INDEX
# 
# - class Board(list)
# - class Cell(tuple)
# - def answer(m)
# - def whatIfIRemovedThis(wall, m, start, end)

class Board(list):
    ''' Useful for indexing into multidimensional lists using tuples, which imo is cleaner. '''

    traversable_value    = 0
    nontraversable_value = 1
    unvisited_value      = None
    unreachable_value    = None

    def __getitem__(self, tup):
        r, c = tup
        return super(self.__class__, self).__getitem__(r).__getitem__(c)

    def __setitem__(self, tup, val):
        r, c = tup
        super(self.__class__, self).__getitem__(r).__setitem__(c, val)

from collections import deque

class Cell(tuple):
    ''' A cell on a board is represented by the cell's coordinates. '''

    def __init__(self, minDistTo = None):
        self.minDistTo = minDistTo

    def getNeighbors(self):
        ''' Yields self's neighbors in up, down, left, right order. '''

        r, c = self

        yield self.__class__( (r-1, c) ) # up
        yield self.__class__( (r+1, c) ) # down
        yield self.__class__( (r, c-1) ) # left
        yield self.__class__( (r, c+1) ) # right

    def isInside(self, board):
        r, c = self
        num_rows, num_cols = len(board), len(list(board)[0])

        return 0 <= r < num_rows and 0 <= c < num_cols

    def isTraversableIn(self, board):
        return board[self] == board.__class__.traversable_value

    def isAWallIn(self, board):
        return board[self] == board.__class__.nontraversable_value

    def hasNotBeenVisitedIn(self, board):
        return board[self] == board.__class__.unvisited_value

    def isUnreachableFrom(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.minDistTo[self] == other.minDistTo.__class__.unreachable_value # hard to understand

    # O(h*w) time complexity
    def genMinDistTo(self, m):
        ''' A BFS Single Sourse Shortest Path algorithm
            appropriate for graphs with unweighted edges*
            *or graphs with weighted edges but where every edge has the same weight'''

        if self.isAWallIn(board = m):
            return None

        h = len(m)
        w = len(list(m)[0])

        minDistTo = Board( [ [Board.unvisited_value]*w for _ in range(h) ] )

        minDistTo[self] = 1
        cells = deque([self]) # cell queue, in the cell queue, each cell is represented by its coordinate

        while cells: # h*w iterations

            cell          = cells.popleft()
            minDistToCell = minDistTo[cell]

            for neighbor in cell.getNeighbors(): # 4 iterations

                if neighbor.isInside(board = m) and \
                   neighbor.isTraversableIn(board = m) and \
                   neighbor.hasNotBeenVisitedIn(board = minDistTo):

                    minDistToNeighbor   = minDistToCell + 1
                    minDistTo[neighbor] = minDistToNeighbor # Setting minDistsTo[.] to an int also marks it as visited.

                    cells.append(neighbor) # Each cell gets appended to the cells queue only once.

        self.minDistTo = minDistTo

# O(h*w) time complexity
def answer(m):

    num_rows = h = len(m)    # height
    num_cols = w = len(m[0]) # width

    m = Board(m)

    bestConceivableResult = h + w - 1

    start = Cell( (  0,   0) )
    end   = Cell( (h-1, w-1) )

    start.genMinDistTo(m) # O(h*w) time

    if end.isUnreachableFrom(start):
        # This happens in test case 3 where it is neccesary
        # to remove a wall to have a path from start to end.
        bestResult_soFar = 2**31 - 1
    else:
        bestResult_soFar = start.minDistTo[end]

    if bestResult_soFar == bestConceivableResult:
        # We cannot do any better than this.
        return bestConceivableResult

    end.genMinDistTo(m) # O(h*w) time

    for r in range(num_rows): # h iterations
        for c in range(num_cols): # w iterations

            cell = Cell( (r, c) )

            if cell.isAWallIn(board = m):

                wall = cell

                # See if you can get a shorter path from start to end by removing this wall.

                potentiallyBetterResult = whatIfIRemovedThis(wall, m, start, end) # O(1) time

                bestResult_soFar = min(bestResult_soFar, potentiallyBetterResult)

    bestResult = bestResult_soFar

    return bestResult

# O(1) time complexity
def whatIfIRemovedThis(wall, m, start, end):
    ''' Returns the distance of the shortest start-to-end path that goes through wall
        as if wall (and only wall) had been removed and were traversable. '''

    #   u
    # l w r
    #   d
    # 
    # w := wall
    # u, d, l, r := the wall's up, down, left, right neighbors respectively
    # 
    # In the worst case there are twelve ways to "go through" the wall and each of these must be considered.
    # I will enumerate them. However symmetric 0. and 3. may seem, they must both be considered. Same goes for all other pairs.
    # 
    #  0. u -> d := from the start, you arrived at u, then went through the wall, emerged at d, and continued on to the end
    #  1. u -> l
    #  2. u -> r
    #  3. d -> u := from the start, you arrived at d, then went through the wall, emerged at u, and continued on to the end
    #  4. d -> l
    #  5. d -> r
    #  6. l -> u
    #  7. l -> d
    #  8. l -> r
    #  9. r -> u
    # 10. r -> d
    # 11. r -> l

    bestResult_soFar = 2**31 - 1

    # [up, down, left, right] = list( wall.getNeighbors() )
    for incoming in wall.getNeighbors():
        for outgoing in wall.getNeighbors():
                                             # 16 iterations
            if incoming == outgoing:
                # Such a path does not require the removal of wall and thus has already been considered.
                continue

            if not incoming.isInside(board  = m)     or not outgoing.isInside(board  = m)    or \
                   incoming.isAWallIn(board = m)     or     outgoing.isAWallIn(board = m)    or \
                   incoming.isUnreachableFrom(start) or     outgoing.isUnreachableFrom(end):
                continue

            minDistFromStartToIncoming = start.minDistTo[incoming]
            minDistFromOutgointToEnd   = end.minDistTo[outgoing]

            potentiallyBetterResult = minDistFromStartToIncoming + 1 + minDistFromOutgointToEnd

            bestResult_soFar = min(bestResult_soFar, potentiallyBetterResult)

    bestResult = bestResult_soFar

    return bestResult

# TESTING ----------------------------------------------------------------------

def run_tests():
    
    # test case 0
    m = [ [0, 1, 1, 0],
          [0, 0, 0, 1], 
          [1, 1, 0, 0],
          [1, 1, 1, 0] ]
    
    print answer(m) == 7
    
    # test case 1
    m = [ [0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0] ]
    
    print answer(m) == 11
    
    # test case 2
    m = [ [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 1, 0],
          [1, 1, 1, 1, 1, 0, 1, 1, 0],
          [1, 1, 1, 1, 1, 0, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0] ]
    
    print answer(m) == 16
    
    # test case 3
    m = [ [0],
          [1],
          [0] ]
    
    print answer(m) == 3
    
    # test case 4
    m = [ [0, 0, 0, 0],
          [1, 1, 1, 0],
          [1, 0, 1, 0],
          [1, 1, 1, 0],
          [1, 0, 0, 0],
          [1, 0, 1, 1],
          [1, 0, 0, 0] ] # m[(2,1)] is traversable but inaccessible
    
    print answer(m) == 10 # == h + w - 1 == 7 + 4 - 1 (this requires wall at (5,3) to be removed)

if __name__ == "__main__":
    
    run_tests()