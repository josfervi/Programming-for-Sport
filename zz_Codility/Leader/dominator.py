# https://codility.com/programmers/lessons/8-leader/dominator/

# simpler variant of Arrays/ n/3 repeat number

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    
    N= len(A)
    
    if N == 0: return -1
    
    candidate=     A[0]
    candidate_idx= 0
    candidate_cnt= 1
    
    for i,a in enumerate(A[1:]):
        
        i= i+1 # convert index of A[1:] to index of A
        
        if candidate_cnt == 0:
            candidate= a
            candidate_idx= i
            candidate_cnt= 1
        elif a == candidate: candidate_cnt+= 1
        else:                candidate_cnt-= 1
    
    if candidate_cnt > N/2: return candidate_idx
    
    candidate_cnt= 0
    for a in A:
        if a == candidate: candidate_cnt+= 1
    
    return candidate_idx if candidate_cnt > N/2 else -1