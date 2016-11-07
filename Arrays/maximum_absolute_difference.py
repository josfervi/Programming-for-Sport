class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        
        if A == []:
            return 1
                
        n= len(A)
        
        if n == 1:
            return 0
        if n == 2:
            return abs(A[0] - A[1]) + 1
        
        # Let i_star, j_star be the i,j pair that maximize f(i,j) = |Ai - Aj| + |i - j|
        #
        # Thus answer = f(i_star, j_star) = |Ai_star - Aj_star| + |i_star - j_star|
        #
        # Without loss of generality, let Ai_star >= Aj_star
        # 
        # Thus,
        #     answer = Ai_star - Aj_star + |i_star - j_star|
        #
        # We now have two cases:
        #    case 1: i_star >= j_star
        #    case 2: i_star <  j_star
        #
        # Under case 1, 
        #       answer = Ai_star - Aj_star + i_star-j_star
        #              = (Ai_star+i_star) - (Aj_star+j_star)
        #
        #       let i_prime be the i that maximizes Ai + i
        #       let j_prime be the j that minimizes Aj + j
        #       and very importantly note that
        #       i_star = i_prime
        #       j_star = j_prime
        #
        # Under case 2,
        #       answer = Ai_star - Aj_star + j_star - i_star
        #              = (Ai_star - i_star) - (Aj_star - j_star)
        #
        #       in this case,
        #       let i_prime be the i that maximizes Ai - i
        #       let j_prime be the j that minimizes Aj - j
        #       and very importantly not that
        #       i_star = i_prime
        #       j_star = j_prime
        #
        # We cannot know in advance which of case 1 and case 2 is the actual case,
        # so we proceed as follows:
        # 
        # find:
        #      maximum_Ai_plus_i
        #      minimum_Aj_plus_j
        #
        #      maximum_Ai_minus_i
        #      minimum_Aj_minus_j
        #
        # then asnwer= max( maximum_Ai_plus_i  - minimum_Aj_plus_j,
        #                   maximum_Ai_minus_i - minimum_Aj_minus_j )
        
        #i= j= 0
        minimum_Aj_plus_j=  maximum_Ai_plus_i=  A[0] + 0 # case 1
        minimum_Aj_minus_j= maximum_Ai_minus_i= A[0] - 0 # case 2
        
        for i,Ai in zip( xrange(1,n), A[1:]):
            
            j=  i
            Aj= Ai
            
            # case 1
            minimum_Aj_plus_j=  min( minimum_Aj_plus_j, Aj+j )
            maximum_Ai_plus_i=  max( maximum_Ai_plus_i, Ai+i )
            
            # case 2
            minimum_Aj_minus_j= min( minimum_Aj_minus_j, Aj-j )
            maximum_Ai_minus_i= max( maximum_Ai_minus_i, Ai-i )
        
        return max( maximum_Ai_plus_i  - minimum_Aj_plus_j,
                    maximum_Ai_minus_i - minimum_Aj_minus_j )