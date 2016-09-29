class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        
        i= 0
        length= 0
        while i < len(A):
            
            length= 0
            while i < len(A) and A[i] != ' ':
                length+= 1
                i+= 1
            
            while i < len(A) and A[i] == ' ':
                i+= 1
        
        return length
        
# sol= Solution()
# sol.lengthOfLastWord("    Wordl   ")