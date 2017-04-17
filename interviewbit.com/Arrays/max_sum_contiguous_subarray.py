# Kadane's Algorithm

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_ending_here= max_so_far= A[0]
        for a in A[1:]:
            max_ending_here= max(a, a+max_ending_here)
            max_so_far=      max(max_so_far, max_ending_here)
        
        return max_so_far
        
sol= Solution()
print sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6