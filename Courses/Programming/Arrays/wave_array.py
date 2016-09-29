class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        
        # My solution was based on extracting a pattern.
        
        # Let the subscript indicate the relative size of an element
        # e.g. a2 is the second  smallest element in A
        #      a1 is the (first) smallest element in A
        # The pattern seems to be:
        # return [ a2, a1, a4, a3, a6, a5, ... ]
        #
        # This can be accomplished by:
        #  1. sort A,
        #  2. break A into pairs
        #  3. in each pair, swap the numbers of the pair
        
        B= sorted(A)
        
        # note: the xrange correctly handles both
        #        the case when len(A) is even, and
        #        the case when len(A) is odd
        #       thus, no need for a check inside the for loop
        for i in xrange(1, len(B), 2):
            # the pair is A[i-1], A[i]
            # swap the numbers of this pair
            B[i-1], B[i] = B[i], B[i-1]
        
        return B
