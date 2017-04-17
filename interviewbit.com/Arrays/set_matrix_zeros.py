# The most interesting thing about my solution is my attempt
#     to prevent duplicate zero assignments = redundant reassignments
# e.g.to prevent assigning a zero two times to the same cell of the array (one zero assignment is enough)

# I did this with non_zero_rows= [y for y in xrange(1, num_rows) if A[y][0] != 0 ]
# I initially tried making non_zero_rows a generator,
# but generators can only be used once, this ofc lead to errors.

# the caveat about non_zero_rows is that it uses O(m) memory in the worst case (the case that every row and col must be zeroed),
#    but in that same worst case, non_zero_rows prevents m*n redundant reassignments

# this is yet another example of a memory usage vs performance tradeoff

# I read: "you shouldn't think much about performance until you've timed your code
#          and found it to be a bottleneck", then and only then improve the bottleneck

# but I have a compulsion to / care deeply about achieving the utmost performance from the get go.
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        
        # when processing the matrix,
        # a distinction must be made between
        #  1. an intial  0, i.e. one present in the input, and
        #  2. a  derived 0, i.e. one that comes into being because it is on the same row or col as an intial 0
        
        num_rows= len(A)
        num_cols= len(A[0])
        
        # r= True indicates that the first row must be zeroed
        # c= True indicates that the first col must be zeroed
        
        r= c= False # indicate that we know that the first row and the first col (respectively) must be zeroed
        
        if A[0][0] == 0:
            r= c= True # meaning we know that the first column and the first row must be zerod
        else:
            for x in xrange(1, num_cols):
                if A[0][x] == 0:
                    # A[0][0]= 0
                    r= True # meaning we know that the first row must be zeroed
                    break
            
            for y in xrange(1, num_rows):
                if A[y][0] == 0:
                    # A[0][0]= 0
                    c= True # meaning we know that the first col must be zeroed
                    break
        
        
        for y in xrange(1, num_rows):
            for x in xrange(1, num_cols):
                if A[y][x] == 0:
                    A[y][0]= 0 # meaning we know that the yth row must be zeroed
                    A[0][x]= 0 # meaning we know that the xth col must be zeroed
        
        
        # note: any '1' meant to be present in the result is already a '1' in A
        
        for y in xrange(1, num_rows):
            if A[y][0] == 0:
                # zero out the yth row
                A[y]= [0]*num_cols
        
        # I tried making non_zero_rows a generator, but generators can only be used once,
        # this ofc lead to errors.
        non_zero_rows= [y for y in xrange(1, num_rows) if A[y][0]]
        
        for x in xrange(1,num_cols):
            if A[0][x] == 0:
                # zero out the xth row
                # for y in xrange(1, num_rows):
                for y in non_zero_rows:
                    A[y][x]= 0
        
        if r:
            # zero out the first row
            A[0]= [0]*num_cols
            # ^ this will overwrite A[0][0], but we've already saved A[0][0][0] to c so we're good
        
        if c:
            # zero out the first col
            for y in xrange(num_rows):
                A[y][0]= 0
        
        return A