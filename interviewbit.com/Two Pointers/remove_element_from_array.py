# https://www.interviewbit.com/problems/remove-element-from-array/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    
    # passes EFICIENCY!!!
    def removeElement(self, A, B):
        
        j= 0
        
        for i,a in enumerate(A):
            if a != B:
                A[j]= A[i] # key fix
                j+= 1
        
        A= A[:j]
        return len(A)
    
    # fails EFFICIENCY
    def removeElement_1(self, A, B):
        i= 0
        while i < len(A):
            
            if A[i] == B:
                A[i:]= A[i+1:] # key failure
            
            else: i+= 1
        
        return len(A)
    
    # fails EFFICIENCY
    def removeElement_2(self, A, B):
        done= False
        while not done:
            try:
                A.remove(B)
            except ValueError:
                done= True
        
        return len(A)