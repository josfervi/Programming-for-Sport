# https://codility.com/programmers/lessons/1-iterations/binary_gap/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7
        
    prev_bit= 0
    
    flag= False
    
    gap_len= 0 # probably optional
    
    max_= 0
    
    while N != 0:
        bit= N%2
        
        transition= bit - prev_bit
        
        if flag:
            if transition == -1:
                # HI to LO transiton
                gap_len= 1
            elif transition == 0 and bit == 0:
                gap_len+= 1
            else:
                # LO to HI transition
                max_= max(max_, gap_len)
                gap_len= 0
        
        flag= flag or bit # same as 'if bit: flag= True'
        
        N/= 2
    
    return max_