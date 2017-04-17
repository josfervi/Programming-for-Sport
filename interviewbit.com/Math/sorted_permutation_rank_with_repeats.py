# https://www.interviewbit.com/problems/sorted-permutation-rank-with-repeats/

from math import factorial

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        # finds the lexicographical rank of string A amongsts its permutations
        
        # LET'S FOLLOW ALONG WITH ONE CANONICAL EXAMPLE: A= "ebabcdfcec"
        
        chars_of_A_in_sorted_order= sorted(A) # the charater of A in lexicographical order
                                              # CANONICAL EXAMPLE: "abbcccdeef"
        
        # count and record the number of occurrences of each character in A
        num_of_occurrences_of_char= {}
        
        for char in chars_of_A_in_sorted_order:
            if char in num_of_occurrences_of_char: num_of_occurrences_of_char[char]+= 1
            else:                                  num_of_occurrences_of_char[char]=  1
        
        # CANONICAL EXAMPLE: num_of_occurrences_of_char = {'a':1, 'b':2, 'c':3, 'd':1, 'e':2, 'f':1}
        
        unique_chars_of_A_in_sorted_order= sorted(num_of_occurrences_of_char.keys()) # CANONICAL EXAMPLE: "abcdef"
        
        
        rank= 0
        
        while A != "":
            
            first_char= A[0] # CANONICAL EXAMPLE: first_iteration: 'e'
            
            # Q: which permutations precede the first permutation that starts with first_char, CE: first_iteration: "eabbcccdef",
            # A: any permutation whose first char is less than first_char
            
            # Q: how many such permutations are there?
            
            idx_of_first_char= unique_chars_of_A_in_sorted_order.index( first_char ) # CE: f_i: 4
            chars_less_than_first_char= unique_chars_of_A_in_sorted_order[ : idx_of_first_char] # CE: f_i: ['a', 'b', 'c', 'd']
            
            
            for char in chars_less_than_first_char:
                rank+= self.computeNumOfPermutationsOfAThatStartWithChar( char, A, num_of_occurrences_of_char) % 1000003 # uses num_of_occurrences_of_char, instead of recomputing it
            
            A= A[1:] # remove first_char, in the next iteration rank will be refined further
            
            # update num_of_occurrences_of_char so that it is correct w.r.t to the new A and update unique_chars_of_A_in_sorted_order if neccesary
            num_of_occurrences_of_char[first_char]-= 1
            if num_of_occurrences_of_char[first_char] == 0:
                unique_chars_of_A_in_sorted_order.remove(first_char)
                num_of_occurrences_of_char.pop(first_char, None) # remove the entry whose key is first_char
        
        return (rank + 1) % 1000003 # convert rank from 0-indexed to 1-indexed
    
    def computeNumOfPermutationsOfAThatStartWithChar(self, starting_char, A, num_of_occurrences_of_char):
        
        N= len(A)
        
        product= 1
        for char, num_of_occurrences_of_char in num_of_occurrences_of_char.items():
            if char == starting_char: num_of_occurrences_of_char-= 1
            product*= factorial(num_of_occurrences_of_char)
        
        return factorial(N-1)/product