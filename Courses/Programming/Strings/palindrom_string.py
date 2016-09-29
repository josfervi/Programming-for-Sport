from re import sub

# A= sub('[^a-zA-Z0-9]', '', A)

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        
        # preprocess for the win
        
        A= sub('[^a-zA-Z0-9]', '', A) # remove non alphanumeric chars from A
        A= A.lower()                  # make A all lowercase to make ignoring case easier
        
        n= len(A)
        
        for i in xrange(n/2):
            
            if A[i] != A[n -1 -i]:
                return False
        
        return True