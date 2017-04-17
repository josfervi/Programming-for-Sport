# https://www.interviewbit.com/problems/longest-palindromic-substring/

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        
        n= len(A)
        
        if n == 0:
            return ""
        
        longest_palindrome_centered_here= A[0]
        (l_i, l_j) = (0, 0)
        l_length=    1      # l indicates longest palindrom so far
        
        for m in xrange(1, n):
            (i, j) = self.find_longest_palindrome_of_centered_at(A, m)
            
            length = j - i + 1
            if length > l_length:
                (l_i, l_j) = (i, j)
                l_length=    length
        
        return A[l_i:l_j+1]
    
    def find_longest_palindrome_of_centered_at(self, A, m):
        
        n= len(A)
        
        d= 1 # displacement
        while m-d >= 0 and m+d < n and A[m-d] == A[m+d]:
            d+= 1
        
        (o_i, o_j) = ( m-d +1 , m+d -1 ) # start and end indeces of longest odd lengthed palindrome of A centered at m
                                         # i.e. a palindrome centered on a character
        
        ml= m-1 # m left
        mr= m   # m right
        
        d= 0
        while ml-d >= 0 and mr+d < n and A[ml-d] == A[mr+d]:
            d+= 1
        
        (e_i, e_j) = ( ml-d +1, mr+d -1 ) # start and end indeces of longest even lengthed palindrome of A centered at m
                                          # i.e. a palindrome centered on a space between characters
        
        
        o_length= o_j - o_i + 1
        e_length= e_j - e_i + 1
        
        if o_length > e_length:
            return (o_i, o_j)
        
        return (e_i, e_j)