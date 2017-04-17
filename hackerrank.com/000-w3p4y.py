# MY only unfixed error may have been capitalizing deque
# UHHHHHHHHHHHHHHHHHHHHHHHH
# may not work


# Complete the function below.

# CONSTANTS
WATER_CHAR = '.'
ISLAND_CHAR = '#'

# TODO: replace hardcoded instances of '.', '#' with
#       WATER_CHAR, ISLAND_CHAR respectively.

# TODO: multiline conditionals should use brackets
#       instead of \ in accordance to Style Guide

# Let N = num_rows
# Let M = num_cols

def  verify(puzzle):
    '''Takes a 2d array representing a solved
       Nurikabe puzzle and returns True if the puzzle
       is correctly solved and False otherwise.
    '''
    
    # As outlined in the problem statement, a
    # corretly solved Nurikabe puzzle must satisfy
    # five seemengly independent conditions.
    
    # Condition 5:
    # Only '.', '#', and number characters appear in
    # the solved puzzle.
    # QUESTION:
    # It is unclear whether number must be a single
    # digit number or if it can be a multiple digit
    # number. I am assuming the latter.
    if not all_chars_valid(puzzle):
        return False
    
    # Condition 4:
    # There are no 2x2 blocks of water ('.') anywhere
    # in the puzzle.
    if _2x2_water_block_exists(puzzle):
        return False
    
    # Condition 3:
    # All of the water squares are connected to each
    # other.
    if not all_water_squares_connected(puzzle):
        return False
    
    # Condition 2 and 1:
    # 2 Each number is within a connected component of
    #   island squares that, including the number square
    #   itself, contains exactly that many squares.
    # 1 Each connected group of island squares contains
    #   exactly one numbered square
    # I will combine these two condition checks into one
    # function. After more thought it may be possible to
    # combine other sets of conditions, but that's not a
    # priority right now.
    if not condition2_and_condition1_satisfied(puzzle):
        return False
    
    # All conditions satisfied.
    return True
    
def all_chars_valid(puzzle):
    
    num_rows = len(puzzle)
    num_cols = len(puzzle[0])
    
    for r in range(num_rows):
        for c in range(num_cols):
            char = puzzle[r][c]
            if (char == WATER_CHAR or
                char == ISLAND_CHAR or
                char.isdigit()):
                continue
            # char is not a valid character
            return False
    
    return True

def _2x2_water_block_exists(puzzle):
    '''Returns True if a 2x2 water ('.') block exists
           in puzzle, False otherwise.
    '''
    
    # Will drag a 2x2 window along puzzle and return
    # false if all the characters that lie on the
    # window are water characters '.'
    
    num_rows = len(puzzle)
    num_cols = len(puzzle[0])
    
    p = puzzle
    
    for r in range(1, num_rows):
        for c in range(1, num_cols):
            
            # there's a lot of redundant work here
            # TODO: reduce redundat work if necessary
            
            up_left, up = p[r-1][c-1], p[r-1][c]
            left,    me = p[ r ][c-1], p[ r ][c]
            
            if (up_left == WATER_CHAR and
                up      == WATER_CHAR and
                left    == WATER_CHAR and
                me      == WATER_CHAR):
                return True
    return False
    
def all_water_squares_connected(puzzle):
    '''Returns True if each water square is
       reachable from every other water square.
       Otherwise, False.
    '''
    # I have two options, I can use O(N*M) extra
    # space and and save some time. Here is the
    # option that uses O(1) extra space at cost of
    # some additional time.
    
    # Will find the position of a WATER_CHAR. Will
    # do BFS from this position, relabeling each
    # encoutered WATER_CHAR as 'j'. Once BFS is
    # done, if there are any unrelabed WATER_CHARS,
    # then I return False because not all water
    # squares are connected to all other water
    # squares. Otherwise, I return True.
    
    num_rows = len(puzzle)
    num_cols = len(puzzle[0])
    
    p = puzzle
    
    # find position of a water square
    r = 0
    while r < num_rows:
        c = 0
        while c < num_cols:
            if p[r][c] == WATER_CHAR:
                break
            c += 1
        r += 1
    
    # QUESTION:
    # What if there were no water squares?
    # Technically this function should return True,
    # but is the overall puzzle still correct/valid?
    if r == num_rows and c == num_cols:
        return True
    
    # Barring that posibility, we can do BFS from
    # position (r,c)
    new_label = 'j'
    _relabel_connected_squares(puzzle,
                               (r,c),
                               WATER_CHAR,
                               new_label)
    
    # Now, look for any unrelabeled water squares
    r = 0
    while r < num_rows:
        c = 0
        while c < num_cols:
            if p[r][c] == WATER_CHAR:
                # this water square is not connected to 
                # the relabeled water squares
                return False
            c += 1
        r += 1
    
    # Now, undo the relabeling (this is the additional
    # time mentioned above).
    for r in range(num_rows):
        for c in range(num_cols):
            if p[r][c] == new_label:
                p[r][c] == WATER_CHAR
    
    return True

from collections import deque
# use append for enqueue
# use popleft for dequeue
    
def _relabel_connected_squares(puzzle,
                                     pos,
                                     sq_type,
                                     new_label):
    '''Modifies puzzle. Every square connected
           to the square at position pos that is of
           type sq_type is relabeled with new_label.
    '''
    
    num_rows = len(puzzle)
    num_cols = len(puzzle[0])
    
    p = puzzle
    
    r, c = pos
    
    # if p[r][c] != sq_type:
    #     # something went wrong
    #     # TODO: consider throwing input error
    #     # but for now just return False
    #    return False
    
    queue = deque([])
    p[r][c] = new_label
    queue.append(pos)
    
    while queue:
        r, c = queue.popleft()
        
        # up
        if r-1 > 0 and p[r-1][c] == sq_type:
            p[r-1][c] == new_label
            queue.append((r-1, c))
        # down
        if r+1 < num_rows and p[r+1][c] == sq_type:
            p[r+1][c] == new_label
            queue.append((r+1, c))
        
        # left
        if c-1 > 0 and p[r][c-1] == sq_type:
            p[r][c-1] == new_label
            queue.append((r, c-1))
        
        # right
        if c+1 < num_cols and p[r][c+1] == sq_type:
            p[r][c+1] == new_label
            queue.append((r, c+1))

# TODO: come up with more descriptive fcn name.
def condition2_and_condition1_satisfied(puzzle):
    
    num_rows = len(puzzle)
    num_cols = len(puzzle[0])
    
    p = puzzle
    
    # Will scan puzzle. When I land on a number, I will
    # relabel each island square connected to that
    # number with a unique negative number.
    # At the end each island will be labeled with a
    # unique negative number and along the way I will
    # check if condition 1 and condition 2 are ever not
    # satisfied.
    
    current_label = -1
    
    for r in range(num_rows):
        for c in range(num_cols):
            
            square = p[r][c]
            if square.isdigit():
                pos = (r,c)
                
                expected_cnt = square
                
                (cond2_met, actual_cnt) = _relabel_connected_squares_cond12(puzzle,
                                           pos, 
                                           ISLAND_CHAR,
                                           current_label)
                
                if not cond2_met:
                    return False
                if actual_cnt == expected_cnt:
                    return True

# modified version of _relabel_connected_squares
# refactor if have time
def _relabel_connected_squares_cond12(puzzle,
                                      pos,
                                      sq_type,
                                      new_label):
    '''Modifies puzzle. Every square connected
           to the square at position pos that is of
           type sq_type is relabeled with new_label.
    '''
    
    num_rows = len(puzzle)
    num_cols = len(puzzle[0])
    
    p = puzzle
    
    r, c = pos
    
    # if p[r][c] != sq_type:
    #     # something went wrong
    #     # TODO: consider throwing input error
    #     # but for now just return False
    #    return False
    
    queue = deque([])
    p[r][c] = new_label
    queue.append(pos)
    
    count = 1
    
    while queue:
        r, c = queue.popleft()
        count += 1
        
        # up
        if r-1 > 0:
            if p[r-1][c] == sq_type:
                p[r-1][c] == new_label
                queue.append((r-1, c))
            elif p[r-1][c].isdigit():
                # condition2 not met
                return (False, -1)
        # down
        if r+1 < num_rows:
            if p[r+1][c] == sq_type:
                p[r+1][c] == new_label
                queue.append((r+1, c))
            elif p[r+1][c].isdigit():
                # condition2 not met
                return (False, -1)
        
        # left
        if c-1 > 0:
            if p[r][c-1] == sq_type:
                p[r][c-1] == new_label
                queue.append((r, c-1))
            elif p[r][c-1].isdigit():
                # condition2 not met
                return (False, -1)
        
        # right
        if c+1 < num_cols:
            if p[r][c+1] == sq_type:
                p[r][c+1] == new_label
                queue.append((r, c+1)) 
            elif p[r][c+1].isdigit():
                # condition2 not met
                return (False, -1)
        
    # Condition2 met so return True and the count
    return (True, count)
    