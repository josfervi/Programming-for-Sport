# both solutions work,
# i think titleToNumber is more readable, easier to understand
#   but it also uses an extra variable
# it's not a big deal though, both solutions are O(N)

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        acc=    0
        weight= 1
        for char in reversed(A):
                               # (ord('A') - 1) = 64
            value=   ord(char) - 64
            
            acc+=    weight * value
            
            weight*= 26
        return acc
            
    def titleToNumber2(self, A):
        # it's like a base 26 number system with a few caveats:
        # there is no symbol for zero
        # where normally in a base n system, n's represenation is 10,
        # since this system doesn't not have a zero, n is represented by z
        
        acc= 0
        for char in A:
            acc*= 26
            
            value= ord(char) - 64 # turns 'A' into 1, 'B'  into 2, 'C' into 3
            
            acc+= value
        
        return acc