# https://www.interviewbit.com/problems/square-root-of-integer/

# considerations:

# candidate**2 might overflow

# all three solutions are
#
# O(lg square) time
# O(1)         working space
#
# imo, sqrt_2 is the easiest to understand,
#      followed by sqrt_3
#      and sqrt is the hardest to understand

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, square):
        
        c_min, c_max= 0, square
        
        while c_min <= c_max:
            
            candidate= (c_min+c_max)/2
            
            square_of_candidate= candidate**2
            
            if square_of_candidate == square:
                return candidate
            
            if square_of_candidate < square:
                
                # in the case that
                # candidate**2 < square < (candidate+1)**2
                # you'd want to return candidate
                # i did exactly that in sqrt_1
                # but here I handle it a different way
                # 
                # say candidate = c' where c'**2 < square < (c'+1)**2
                # as stated, we'd want to eventually return c'
                # here what happens is we set c_min = c'+1
                # and in every subsequent iteration of the while loop
                # we'll be hitting the else case lns 59-61
                # so we'll be setting c_max = candidate - 1
                # eventually what happens is
                # at the beg last iteration of the while loop
                # c_max = c_min = c'+1
                # s.t. candidate = c'+1
                # we go into the else because candidate**2=(c'+1)**2 > square
                # and set c_max = candidate - 1 = c'+1 - 1 = c'
                # then we fall out of the while loop with c_max holding c'
                # and simply return c_max which again holds c' as desired
                
                # as you can see this is a clever trick,
                # but makes sqrt a lot harder to understand than sqrt_1 or sqrt_2
                
                # discard candidates <= candidate
                c_min= candidate + 1
            
            else: # square_of_candidate > square
                # discard candidates >= candidate
                c_max = candidate - 1
        
        return c_max
    
    
    def sqrt_1(self, square):
        
        c_min, c_max= 0, square
        
        while c_min <= c_max:
            
            candidate= (c_min+c_max)/2
            
            square_of_candidate= candidate**2
            
            if square_of_candidate == square:
                return candidate
            
            if square_of_candidate < square:
                
                if square < (candidate + 1)**2:
                    # { candidate**2 < square < (candidate+1)**2
                    return candidate
                
                # (candidate+1)**2 <= square
                
                # discard candidates <= candidate
                c_min= candidate + 1
            
            else: # square_of_candidate > square
                # discard candidates >= candidate
                c_max = candidate - 1
    
    
    def sqrt_2(self, square):
        
        c_min, c_max= 0, square
        
        res= 0
        
        while c_min <= c_max:
            
            candidate= (c_min+c_max)/2
            
            square_of_candidate= candidate**2
            
            if square_of_candidate == square:
                return candidate
            
            if square_of_candidate < square:
                
                res= candidate
                
                # discard candidates <= candidate
                c_min= candidate + 1
            
            else: # square_of_candidate > square
                # discard candidates >= candidate
                c_max = candidate - 1
        
        return res