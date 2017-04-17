# https://www.interviewbit.com/problems/max-continuous-series-of-1s/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    
    # - O( len(A) ) time complexity
    # - O( number of zeros in A ) extra space
    
    # can be:
    # - O( len(A) ) time complexity
    # - O( B ) extra space, B is usually le number of zeros in A
    # if zero_indeces is made into a Linked List
    
    # can be:
    # - O( B*len(A) ) time complexity
    # - O( B ) extra space, B is usually le number of zeros in A
    # if zero_indeces is kept at a maximum lenght of B
    # note:
    # this would require moving B-1 elements each time a new zero is encountered
    # when a new zero is encountered, do: A[:-1]= A[1:], A[-1]= i, hence O( B*len(A) ) time complexity
    def maxone(self, A, B):
        
        cnt= 0
        zero_indeces= []
        
        max_ending_here= 0
        mx_e_h_strt=     0
        max_so_far=      0
        mx_s_f_strt=     0
        mx_s_f_end=      0
        
        for i,a in enumerate(A):
            
            if cnt + (a == 0) > B:
                # { a = A[i] = 0 }
                mx_e_h_strt= zero_indeces[-B] + 1 if B != 0 else i+1
                max_ending_here= i-mx_e_h_strt +1
                zero_indeces.append(i)
                assert max_ending_here <= max_so_far
            else:
                cnt+= (a == 0)
                if a == 0: zero_indeces.append(i)
                max_ending_here+= 1
                if max_ending_here > max_so_far:
                    max_so_far=  max_ending_here
                    mx_s_f_strt= mx_e_h_strt
                    mx_s_f_end=  i
        
        return range(mx_s_f_strt, mx_s_f_end +1)