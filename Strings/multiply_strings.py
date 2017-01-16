# https://www.interviewbit.com/problems/multiply-strings/

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        
        res_digits= []
        
        A_num= int(A)
        B_lst= reversed( map(lambda c : int(c), list(B))) # assume B has no leading 0's
        
        sum_of_partial_prods_so_far= 0 # truncated sum
        
        for b in B_lst:
            
            partial_prod= A_num * b
            
            sum_of_partial_prods_so_far+= partial_prod
            
            res_digit= sum_of_partial_prods_so_far % 10
            res_digits.append( res_digit )
            
            sum_of_partial_prods_so_far/= 10 # truncate it
        
        left_most_digits=      sum_of_partial_prods_so_far
        right_most_digits_str= "".join(reversed( map(lambda i : str(i), res_digits) ))
        
        if left_most_digits == 0:
            return right_most_digits_str
            
        return str(left_most_digits) + right_most_digits_str