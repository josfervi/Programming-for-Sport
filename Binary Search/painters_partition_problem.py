# https://www.interviewbit.com/problems/painters-partition-problem/

from math import ceil


# k - number of painters
# n - len(L) where L is a list of board lengths
# S - sum(L)
# 
# O(n * lgS) time
# O(1)       working space

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, k, t, L):
        
        if t == 0 or len(L) == 0:
            return 0
        
        if k == 0:
            return None
        
        return (t * self.paint_(k, L)) % 10000003
    
    
    def paint_(self, k, L):
        
        num_painters= k
        num_boards=   len(L)
        
        if num_painters >= num_boards:
            return max(L)
        
        # {num_painters < num_boards}
        
        sum_= sum(L)
        max_= max(L)
        avg=  int( ceil( float(sum_)/k ) )
        
        best_conceivable_result=  max( max_, avg ) # could start at 0 instead
        worst_conceivable_result= sum_             # could start at MAX_INT instead
        
        c_min, c_max = best_conceivable_result, worst_conceivable_result
        
        best_result_so_far= worst_conceivable_result
        
        while c_min <= c_max:
            
            candidate= (c_min+c_max)/2 # candidate time
            
            if self.is_possible_to_paint(k, L, candidate):
                
                best_result_so_far= candidate
                
                c_max= candidate - 1
            
            else:
                
                c_min= candidate + 1
        
        return best_result_so_far
    
    # returns true if k painters can paint
    # the boards in L in T time
    # 
    # t, the time to paint one unit of board, is 1
    def is_possible_to_paint(self, k, L, T):
        
        num_boards= len(L)
        
        number_of_painters_used_so_far= 1
        current_painter_contrib_so_far= 0 # number_of_board_units_that_current_painter_has_painted_so_far
        
        for board_length in L:
            
            if current_painter_contrib_so_far + board_length <= T:
                # the current painter can paint the current board
                # without exceeding T to paint all his/her boards
                current_painter_contrib_so_far+= board_length
                continue
            
            # the current painter cannot paint the current board
            # without exceeding T to paint all his/her boards
            # so assign the current board to the next painter
            
            number_of_painters_used_so_far+= 1
            current_painter_contrib_so_far= board_length
            
            if number_of_painters_used_so_far > k:
                # to paint all the boards in time <= T
                # we need more than k painters so return False
                return False
        
        return True