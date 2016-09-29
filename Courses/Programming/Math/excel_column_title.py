class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        
        str_acc= ""
        
        while A > 0:
            int_a= A % 26
            if int_a == 0:
                chr_a= 'Z'
                A= A/26 - 1
            else:
                chr_a= chr( int_a + 64 )
                A= A/26
            str_acc= chr_a + str_acc # does not equal acc + chr( ) because string concatenation is not commutative

        return str_acc