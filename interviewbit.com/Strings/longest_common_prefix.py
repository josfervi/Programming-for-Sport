class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        
        words= A
        
        num_of_words= len(words)
    
        len_of_smallest_word= len(words[0])
        for word in words[1:]:
            if len(word) < len_of_smallest_word:
                len_of_smallest_word= len(word)
        
        # del(word) # in InterviewBit i noticed i couldn't delete a variable in Python,
                    # which is something I can do in PythonTutor.
        
        # len_of_smallest_word= len( min(key= lambda word : len(word), words) )
        
        for i in xrange(len_of_smallest_word):
            
            # i indexes letters in a word
            
            letter= words[0][i] # the ith letter of the first word
            
            for j in xrange(1, num_of_words):
                
                # j indexes words in a list of words
                 # the ith letter of the jth word
                let= words[j]
                if words[j][i]                     != letter:
                    
                    return words[0][:i] # this is the common suffix
        
        # outside the for loop
        # { i = len_smallest_word -1
        #   meaning all words have the first len_smallest_letters in common}
        
        return words[0][ : len_of_smallest_word]
        
#sol= Solution()
#print sol.longestCommonPrefix(["abc", "abce", "abd"])