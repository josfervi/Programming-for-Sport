# https://www.interviewbit.com/problems/justified-text/

'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.

Example:

words: ["This", "is", "an", "example", "of", "text", "justification."]

L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]
 Note: Each word is guaranteed not to exceed L in length. '''

from string import split

class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        
        if A == []:
            return ""
        if len(A) == 1:
            return [A[0] + ' '*(B - len(A[0]))]
        
        words= A
        L=     B
        lines= []
        
        line= words[0]
        for word in words[1 : -1]:
            
            if len(line) + 1 + len(word) <= L:
                # the current word fits in the current line
                line+= ' ' + word
            else:
                # the current word does not fit in the current line
                # pad the current line and append it to lines
                line= self.pad(line, L)
                lines.append(line)
                line= word

        # add the last word to the current line if it fits the current line
        # if it does not fit, pad the current line, append it to lines, and
        # then append the last word to lines
        last_word= words[-1]
        if len(line) + 1 + len(last_word) <= L:
            line+= ' ' + last_word
            lines.append( line + (' '*(L - len(line))) )
        else:
            line= self.pad(line, L)
            lines.append(line)
            lines.append( last_word + (' '*(L - len(last_word))) )
        
        return lines
    
    def pad(self, line, L):
        
        words_in_the_line= split(line)
        
        if len(words_in_the_line) == 1:
            return line + ' '*(L-len(line))
        
        gaps= len(words_in_the_line) - 1
        tokens= L - (len(line) - gaps)   # number of spaces to be distributed
        if tokens % gaps == 0:
            # give each gap exactly tokens/gaps spaces
            return (' '*(tokens/gaps)).join(words_in_the_line)
        
        # give the first (tokens % gaps) gaps exactly (tokens / gaps + 1) spaces
        # give the remiaing              gaps exactly (tokens / gaps    ) spaces
        
        return (' '*(tokens/gaps+1)).join(words_in_the_line[:tokens%gaps+1]) + \
               (' '*(tokens/gaps  )) + \
               (' '*(tokens/gaps  )).join(words_in_the_line[tokens%gaps+1:])
               
# sol= Solution()
# print sol.fullJustify([ "What", "must", "be", "shall", "be." ], 12)