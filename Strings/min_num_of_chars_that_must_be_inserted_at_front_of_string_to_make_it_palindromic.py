class Solution:
    # @param A : string
    # @return an integer
    def solve(self, word):
        
        # find the lenght of the longest palindrome starts at pos 0
        l = len_of_longest_palindrome_starting_at(0, word)
        
        return len(word) - l


def len_of_longest_palindrome_starting_at(strt, word):
    
    N = len(word)
    
    if strt < 0 or strt >= N:
        raise ValueError()
    
    # try ending at N-1
    #
    # then if necessary
    #   try ending at N-2
    # 
    #   then if necessary
    #     ...
    
    end = N - 1
    while strt < end:
        if palindrome(word, strt, end):
            return end - strt + 1
        end -= 1
    
    return 1


def palindrome(word, strt, end):
    
    i, j = strt, end
    
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
        
    return True
