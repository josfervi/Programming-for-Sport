# reverseWords1 is a one liner
# reverseWords  just does one iteration through A and uses less mem than ^

class Solution:
    # @param A : string
    # @return string
    
    def reverseWords(self, A):
        
        acc= ""
        i= 0
        while i < len(A) and A[i] == ' ':
            i+= 1
        
        while i < len(A):
            
            word= ""
            while i < len(A) and A[i] != ' ':
                word+= A[i]
                i+= 1
            
            acc= word + ' ' + acc
            
            while i < len(A) and A[i] == ' ':
                i+= 1
        
        return acc[ : -1] # ignore the last space
    
    def reverseWords1(self, A):
        
        return ' '.join(reversed(A.split())) # no need to A.strip()
                                             # i.e. to remove leading and trailing white space
                                             # because A.split() does this already
        
        # words= A.split() # performs a split at each location in A where there one or more white space
        # return ' '.join(reversed(words))
        
        # words= A.split
        # words.reverse()
        # return ' '.join(reversed(words))
