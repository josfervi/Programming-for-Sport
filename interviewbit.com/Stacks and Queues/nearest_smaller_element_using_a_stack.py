# https://www.interviewbit.com/problems/nearest-smaller-element/

class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, nums):
        
        n = len(nums)
        stack = []
        res = [None]*n
        
        for i, num in enumerate(nums):
            
            while stack and stack[-1] >= num:
                stack.pop()
            
            res[i] = stack[-1] if stack else -1
            
            stack.append(num)
        
        return res
        

# corner case

#        1   2   3   4   5   4   4   3   2    1
# res   -1   1.  2.  3.  4.  3.  3.  2.  1.  -1

# stack  1   1.  1   1   1   1   1   1   1.   1
#            2   2.  2   2   2   2   2.  2    
#                3   3.  3   3.  3.  3
#                    4   4.  4   4
#                        5