# each num in [1...n] that is singly div by 5
#      combines with another num in [1...n] that is singly div by 2
#      to contribute one zero to n!
#
# additionally:
#
# each num in [1...n] that is doubly div by 5
#      combines with another num in [1...n] that is doubly div by 2
#      to contribute one additional zero to n!
#
# additionally:
#
# each num in [1...n] that is tripy div by 5
#      combines with another num in [1...n] that is tiply div by 2
#      to contribute one additional zero to n!
#
# etc... until you reach max div by 5

from math import log

class Solution:
    # @param A : integer
    # @return an integer
    
    def trailingZeroes(self, A):
        n= A
        
        if n == 0:
            return 0
        
        # DEFINTIONS
        #
        #   a_i := num in [1...n] that is ily div by 2
        #   b_i := num in [1...n= that is ily div by 5
        #
        #   where i=1 means singly
        #         i=2 means doulby
        #         i=3 means triply
        
        
        # The SETS
        #
        #   A_i = the set of all a_i
        #   B_i = the set of all b_i
        
        
        # CONCRETE EXAMPLE
        #
        # e.g. 2 is      singly div by 2, so 2 is     in A_1
        #      2 is not  doubly div by 2, so 2 is not in A_2
        #
        #      4 is      singly div by 2, so 4 is     in A_1
        #      4 is also doubly div by 2, so 4 is     in A_2
        #      4 is not  triply div by 2, so 4 is not in A_3
        #
        #      6 is in A_1, but not in A_2
        #      8 is in A_1, A_2, and A_3, but not in A_4
        #
        #     10 is in A_1, but not in A_2
        
        
        # SOME RULES
        #
        # note:
        #       if a is     in A_i, then a is     in A_j for all j in [1...i-1]
        #       if a is not in A_i, then a is not in A_j for all j >  i
        #
        # similarly:
        #       if b is     in B_i, then b is     in B_j for all j in [1...i-1]
        #       if b is not in B_i, then b is not in B_j for all j >  i
        #
        # summarising:
        #       if b is in B_i, but not in B_i+1
        #       then b is     in B_j for all j in [1...i]
        #       and  b is not in B_j for all j >  i
        
        
        # CARDINALITIES
        #
        #   count_[1...n]_(a_i) = |A_i| = n/2**i
        #   count_[1...n]_(b_i) = |B_i| = n/5**i
        #
        #   |B_i| < |A_i|
        #
        #   |A_i - A_i+1| = |A_i| - |A_i+1| because each elem in A_i+1 is in A_i
        #   |B_i - B_i+1| = |B_i| - |B_i+1| because each elem in B_i+1 is in B_i
        #
        #   |B_i - B_i+1| = |B_i| - |B_i+1| = n/5**i - n/5**(i+1) = 4n/5**(i+1)
        #   |A_i - A_i+1| = |A_i| - |A_i+1| = n/2**i - n/2**(i+1) =  n/2**(i+1)
        #
        #   Let P(i) be the proposition that |B_i - B_i+1| <= |A_i - A_i+1|
        # 
        #   if i+1 is even:
        #     P(i) is true when i>=1 [good]
        #   if i+1 is odd
        #     P(i) is true when i>=2 [????]
        #
        #   i=1 => i+1 is even        => P(i) is true for i=1
        #   i=2 => i+1 is odd         => P(i) is true for i=2
        #   i>2 => i+1 is even or odd => P(i) is true for i>2
        #
        #   P(i) is true for all i>=1 [!yay!]
        #
        #   What this means is that there are
        #     always enough nums singly, doubly, triply, etc. div by 2 to
        #     combine with  nums singly, doubly, triply, etc. div by 5 respectively
        
        
        # The MEANING and SIGNIFICANCE of B_i - B_i+1
        #
        #   B_1 - B_2
        #   5,10,15,20,30,35,40,45,55,60, 65, 70, 80, 85, 90, 95, 105, 110, 115, 120
        #     are each in      B_1, but not  in B_2
        #     so these nums are in
        #   B_1 - B_2
        #    note that each  num in B_1 - B_2
        #    combines with a num in A_1 - A_2 to contribute one zero to n!
        # 
        # additionally:
        #   25, 50, 75, 100
        #     are each also in B_1, but also in B_2, but not  in B_3
        #     so these nums are in
        #   B_2 - B_3
        #    note that each  num in B_2 - B_3
        #    combines with a num in A_2 - A_3 to contribute two zero to n!
        #
        # additionally:
        #   125
        #     is       also in B_1  and also in B_2, but also in B_3 but not in B_4 
        #     so this num is in
        #   B_3 - B_4
        #    note that each  num in B_3 - B_4
        #    combines with a num in A_3 - A_4 to contribute three zero to n!
        #
        #    note that each  num in B_i - B_i+1
        #    combines with a num in A_i - A_i+1 to contribute i zeros to n!
        
        m= int(log(n, 5)) # n is in [5^m...5^(m+1) -1]
        
        num_trailing_zeros= 0
        for i in xrange(1, m +1):
            
            num_trailing_zeros+= n / 5**i
        
        return num_trailing_zeros
        
    def their_trailingZeroes(self, A):
            
        n= A
        
        if n == 0: return 0
        
        num_trailing_zeros= 0
        while n != 0:
            
            num_trailing_zeros+= (n/5)
            n/= 5
            
        return num_trailing_zeros