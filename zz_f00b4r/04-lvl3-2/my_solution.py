# Submission: SUCCESSFUL. Completed in: 11 hrs, 35 mins, 5 secs. / 4 days

# Currently supports 2D lists i.e. 2D matrices.
# 
# b[(0,1)] == b[0][1]
# 
# TODO: Add support for 3D and higher-dimensional matrices.
# BUG: b[(0)] == b[0] == b.__getitem__(0) should give back the first element of the list(b) instead of raising TypeError: 'int' object is not iterable
#      bug was triggered on ln 57 and ln 141. E.g. on ln 141, I tried to get the width (num_cols) of m by doing len(m[0])
#      got around it by doing len(list(m)[0]) instead but it's not pretty
# 
# Alternate class name: TupleIndexedList
class Board(list):
    ''' Useful for indexing into multidimensional lists using tuples, which imo is cleaner. '''
    
    traversable_value    = 0
    nontraversable_value = 1
    unvisited_value      = None
    
    def __getitem__(self, tup):
        r, c = tup
        return   super(self.__class__, self).__getitem__(r).__getitem__(c)
        # return super(type(self),     self).__getitem__(r).__getitem__(c) # I left these alternate forms in for my own future reference.
        # return super(Board,          self).__getitem__(r).__getitem__(c) # Least maintainable.
    
    def __setitem__(self, tup, val):
        r, c = tup
        super(self.__class__, self).__getitem__(r).__setitem__(c, val)


# Currently supports 2D coordinates.
# TODO: Add support for 3D and higher-dimensional coordinates.
# 
# Alternate class name: Coord
class Cell(tuple):
    ''' A cell on a board is represented by the cell's coordinates. '''
    
    def getNeighbors(self):
        ''' Yields self's neighbors in up, down, left, right order. '''

        r, c = self
        
        # up
        yield self.__class__( (r-1, c) )
        
        # down
        yield self.__class__( (r+1, c) )
        # yield type(self)(   (r+1, c) ) # Less readable alternate form.
        # yiled Cell(         (r+1, c) ) # Least maintanable.
        
        # left
        yield self.__class__( (r, c-1) )
        
        # right
        yield self.__class__( (r, c+1) )
    
    
    def isInside(self, board):
        
        r, c = self
        num_rows, num_cols = len(board), len(list(board)[0])
        
        return 0 <= r < num_rows and 0 <= c < num_cols
    
    
    def isTraversableIn(self, board):
        
        return   board[self] == board.__class__.traversable_value
        # return board[self] == 0
    
    def isAWallIn(self, board):
        
        return board[self] == board.__class__.nontraversable_value
    
    def hasNotBeenVisitedIn(self, board):
        
        return   board[self] == board.__class__.unvisited_value
        # return board[self] == None

# O(h*w) time
def answer(m):
    
    num_rows = h = len(m)    # height
    num_cols = w = len(m[0]) # width
    
    m = Board(m)
    
    bestConceivableResult = h + w - 1
    
    start = Cell( (  0,   0) )
    end   = Cell( (h-1, w-1) )
    
    minDistsFromStartTo = getMinDistsTo(m, start) # O(h*w) time
    
    if minDistsFromStartTo[end] is None:
        # There is no way to get from start to end without removing a wall.
        # The end is not accessible from the start. For an example, see test case 3.
        bestResult_soFar = 2**31 - 1 # Integer.MAX_VALUE
    else:
        # There IS a way to get from start to end without removing a wall.
        bestResult_soFar = minDistsFromStartTo[end]
    
    if bestResult_soFar == bestConceivableResult:
        # We cannot do any better than this.
        return bestConceivableResult
    
    minDistsToEndFrom = getMinDistsTo(m, end) # O(h*w) time
    
    for r in range(num_rows):
        for c in range(num_cols): # O(h*w) time
            
            cell = Cell( (r, c) )
            
            if cell.isAWallIn(board = m):
                # cell is a wall
                
                wall = cell
                
                # in O(1) time,
                # see if you can get a shorter path from start to end by removing this wall
                
                potentiallyBetterResult = whatIfIRemovedThis(wall, m, minDistsFromStartTo, minDistsToEndFrom) # O(1) time
                
                bestResult_soFar = min(bestResult_soFar, potentiallyBetterResult)
    
    bestResult = bestResult_soFar
    
    return bestResult

from collections import deque

# h - len(m)
# w - len(m[0])
# 
# O(h*w) time
# 
# m  :: matrix (list of lists) of 0's and 1's
#       where 0 indicates a traversable cell
#         and 1 indicates a non-traversable cell (a.k.a. a wall)
# start :: tuple 
#          a coordinate (r, c) representing the cell at that coordinate
def getMinDistsTo(m, start):
    ''' A BFS Single Sourse Shortest Path algorithm
        appropriate for graphs with unweighted edges*
        *or graphs with weighted edges but where every edge has the same weight'''
    
    if start.isAWallIn(board = m):
        # the start cell is not traversable in board m
        # so return None
        return None
    
    h = len(m)
    w = len(list(m)[0])
    
    minDistsTo = Board( [ [None]*w for _ in range(h) ] ) # None at coord (r, c) indicates that the cell at that coord has not been visited
    
    minDistsTo[start] = 1
    cells = deque([start]) # cell queue, in the cell queue, each cell is represented by its coordinate
    
    while cells: # h*w iterations
        
        cell          = cells.popleft()
        minDistToCell = minDistsTo[cell]
        
        for neighbor in cell.getNeighbors(): # 4 iterations
            
            if neighbor.isInside(board = m) and neighbor.isTraversableIn(board = m) and neighbor.hasNotBeenVisitedIn(board = minDistsTo):
                
                minDistToNeighbor    = minDistToCell + 1
                minDistsTo[neighbor] = minDistToNeighbor # Setting minDistsTo[.] to an int also marks it as visited.
                
                cells.append(neighbor) # Each cell gets appended to the cells queue only once.
    
    return minDistsTo

# O(1) time
# (It is also valid to say that this function is O(deg_freedom**2) time,
#  but since deg_freedom remains a constant (4) over all inputs to answer(m),
#  O(deg_freedom**2) == O(1) )
def whatIfIRemovedThis(wall, m, minDistsFromStartTo, minDistsToEndFrom):
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
    
    bestResult_soFar = 2**31 - 1 # == Integer.MAX_VALUE # I could also set it minDistsFromStartTo[end] but then the docstring would be slightly incorrect
    
    # [up, down, left, right] = list( wall.getNeighbors() )
    for incoming in wall.getNeighbors():
        for outgoing in wall.getNeighbors(): # We always have 16 O(1) iterations meaning overall O(16) == O(1) time
            
            if incoming == outgoing:
                # Such a path does not require the removal of wall and thus has already been considered.
                continue
            
            if not incoming.isInside(board = m) or incoming.isAWallIn(board = m) or \
               not outgoing.isInside(board = m) or outgoing.isAWallIn(board = m):
                continue
            
            minDistFromStartToIncoming = minDistsFromStartTo[incoming]
            minDistFromOutgointToEnd   = minDistsToEndFrom[outgoing]
            
            if minDistFromStartToIncoming is None or minDistFromOutgointToEnd is None:
                # either incoming is inaccessible from the start cell or
                #        outgoing is inaccessible form the end   cell or both
                # 
                # a cell is inaccessible when m[cell] == 0 and minDist...[cell] == None
                continue
            
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