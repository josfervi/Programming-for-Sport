# Submission: SUCCESSFUL. Completed in: 2 days, 1 hr, 11 mins, 55 secs. / 4 days

# Borrowing from "generatingfunctionology" by Herbert S. Wilf of UPenn:
# 
# "A partition of a positive integer n is a representation:
#  
#  n = r1 + r2 + ... + rk" (1 <= r1 <= r2 <= ... <= rk).
# 
# " The numbers r1,...,rk are the parts of the partition."
#
# Adding to that definition:
# 
#  A distinct partition of n i s a partition of n into
#  distinct parts, i.e. a representation:
#  
#  n = r1 + r2 + ... + rk (0 < r1 < r2 < ... < rk).
#  
#  Let p(n) denote the number of distinct partitions of n.
#  
#  Let the number of distinct partitions of n with parts
#  greater than r be denoted by p(r, n) or P[r, n].
#  p(r, n) counts partitions which have a representation:
#  
#  n = r1 + r2 + ... + rk (r < r1 < r2 < ... < rk).
#  
#  The following three statements are fact:
#  
#    1. answer(n) = p(n) - 1 for n >= 3
#    2. p(n) = p(0, n)       for n >= 3
#    3. p(r, n) = 1 + sum_from_i=r+1_to_(n-1)/2_of( p(i, n-1) ) (Recurrence relation)
#  
#  Facts 1.-3. can be used to find answer(N).
#  In fact, that is exactly what my algorithm does.
#  My algorithm also memoizes results to speed up the computation.
#  
#  In addition to the recurrence relation of fact 3., there are two other
#  recurrence relations:
#  
#    4. p(r, n) = p(r-1, n) - p(r,   n- r   )
#    5. p(r, n) = p(r+1, n) + p(r+1, n-(r+1))
#  
#  4. and 5. are, in fact, derived from 3. Under specific circumstances,
#  p(r, n) can be computed much faster by using 4. or 5. than by using 3. itself.
#  
#  Please feel free to reach me at linkedin.com/in/josfervi
#  to ask me your clarifying questions. For example, you can
#  ask me to show why facts 1.-5. are true.

P = {}

def answer(N):
    
    if N < 3:
        return 0
    
    return p(0, N) - 1

def p(r, n):
    
    global P
    
    res = 1
    
    lo, hi = r+1, (n-1)/2
    
    # base case
    if lo > hi:    # Lines 37-38 are optional.
        return res # If these two lines were omitted,
                   # we would have the same behavior.
    
    for i in range(lo, hi+1):
        
        if (i, n-i) in P:
            res += P[(i, n-i)]
            continue
        
        P[(i, n-i)] = p(i, n-i) # memoize
        res += P[(i, n-i)]
    
    return res

# TESTING ----------------------------------------------------------------------

# def main():
#     run_tests()

# def run_tests():
#     print answer(1) == 0
#     print answer(2) == 0
#     print answer(3) == 1
#     print answer(4) == 1
#     print answer(5) == 2
#     print answer(10) == 9
#     print answer(200) == 487067745

# if __name__ == "__main__":
#     main()