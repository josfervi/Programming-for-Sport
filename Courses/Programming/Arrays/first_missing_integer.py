# my solution is not very readable

# i don't understand the provided python solution

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in xrange(len(A)):
            if A[i] < 1 or A[i] > len(A):
                A[i]= 0
        
        i= 0
        while i < len(A):
             # A[i] == -1 or A[i] == 0:
            if A[i] < 1:
                i+= 1
            elif A[i] == i +1:
                A[i]= -1
                i+= 1
                
            # {A[i   ] != i +1}
            # {A[j -1] != j   }
            elif A[ A[i] -1] > 0:
               # A[ A[i] -1] != -1 and
               # A[ A[i] -1] !=  0
                a= A[i]
              # -a--  -----b-----   -----b-----  -1
                A[i], A[ a -1] = A[ a -1], -1
            else:
               # { A[ A[i] -1] == -1 or
               #   A[ A[i] -1] ==  0    }
               A[ A[i] -1]= -1
               A[i]= 0
               i+= 1
        
        i= 0
        while i < len(A):
            if A[i] == 0:
                return i +1
            i+= 1

        return len(A) +1
        
sol= Solution()
sol.firstMissingPositive([9,8,7,4,5,1])