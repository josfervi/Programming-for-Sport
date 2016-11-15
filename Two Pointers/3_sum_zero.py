# https://www.interviewbit.com/problems/3-sum-zero/

# can't remove duplicates, some answers will contain duplicates, e.g. 0,0,0 sum up to 0

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        
        if len(A) < 3: return []
        
        A.sort() # sort A in place, O(nlogn)
        
        # can't remove duplicates, some answers will contain duplicates, e.g. 0,0,0 sum up to 0
        
        res= set() # use a set to avoid duplicates
        
        for first_idx in xrange(len(A) -2):
            
            second_idx= first_idx +1
            third_idx=  len(A)    -1
            
            first= A[first_idx]
            
            target= -first
            
            while True:
                if second_idx >= third_idx: break
                
                second, third = A[second_idx], A[third_idx]
                
                if   second+third < target: second_idx+= 1
                elif second+third > target:  third_idx-= 1
                else: # first+second+third = 0
                    res.add( (first, second, third) ) # first,second,third are in non-decreasing order
                    second_idx+= 1
                    third_idx-=  1
        
        return list(res)