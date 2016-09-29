# from http://www.crosswordunclued.com/2010/06/roman-numerals.html
#
# On the face of it, IL and IC appear to follow the same subtractive principle
# as IV and IX, i.e. IL = L (50) - I (1) = 49.
#
# This is actually not valid.
#
# The subtractive principle for Roman numbers has these restrictions: 
# You can only subtract a power of ten, and only from the next two higher "digits",
# where the digits are {I, V, X, L, C, D, M}.

# from https://en.wikipedia.org/wiki/Roman_numerals#Roman_numeric_system
#
# Number	4	9	40	90	400	900
# Notation	IV	IX	XL	XC	CD	CM

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        
        int_num= 0
        prev_a= 'I'
        
        for a in reversed(A):
            
            if a == 'I':
                if prev_a == 'V' or prev_a == 'X':
                    int_num-= 1
                else:
                    # { prev_a is prob 'I' }
                    int_num+= 1
            elif a == 'V':
                int_num+= 5
            elif a == 'X':
                if prev_a == 'L' or prev_a == 'C':
                    int_num-= 10
                else:
                    int_num+= 10
            elif a == 'L':
                int_num+= 50
            elif a == 'C':
                if prev_a == 'D' or prev_a == 'M':
                    int_num-= 100
                else:
                    int_num+= 100
            elif a == 'D':
                int_num+= 500
            else:
                # {a = 'M'}
                int_num+= 1000
            
            prev_a= a
        
        return int_num
