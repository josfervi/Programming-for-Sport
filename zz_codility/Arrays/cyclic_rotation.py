# https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, K):
    # write your code in Python 2.7
    
    N= len(A)
    
    if N == 0: return []
    
    K%= N
    
    return A[-K:] + A[:-K]