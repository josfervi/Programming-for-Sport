# https://codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

# this is a duplicate of Bit Manipulation/single_number.py

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    
    unpaired= 0
    
    for a in A:
        
        unpaired^= a
    
    return unpaired