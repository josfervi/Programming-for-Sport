# G(n, k) denotes the number of simple, connected graphs
#                    with n labeled vertices and k edges.

# The following code computes G(n, k) for n,k satisfying
#                                    1 <= n <= n_max
#                                  n-1 <= k <= n(n-1)/2

# My soution is
# - optimized for performance at the sake of some readabiity
# - memoized
# - bottom-up memoized
#   - O(1) amoritized space complexity
# - not 
# - can be easily modified to compute G(n, k) for n>20,
#                             by simply changing n_max. 

# In my quest to find a solution, I learned:
# - about generating functions
# - and tangentially, how to find a closed form for the nth fibonacci,
#                                       which I think was really cool.

# complete_graph_n denotes the complete graph with n labeled vertices

# I found the problem of finding G(n, k) to fall into three difficulty cases.
# Thus my solution is three tiered to address each of these cases.
# 1) The easy   difficulty cases:
#    - When k= n-1,      G(n,k)=n**n-2 (Cayley's Formula)
#    - When k= n(n-1)/2, G(n,k)= 1     (there is only one complete_graph_n for each n)
# 2) The medium difficulty cases:
#    - When k= n(n-1)/2 - r, where r is in range(1, 2*(n-2)), the problem can be conceptualized as:
#       How many ways are there to cut r edges from complete_graph_n without severing the resulting graph's connectivity?
#       I derived simple formulas for these cases.
# 3) The hard   difficulty cases
#    - For all other k, i.e. 1 < k <= 2*(n-2), I use the reccurrence found here: http://bit.ly/2cc1Jje,
#       which comes courtesy of Marko Riedel at StackExchange:
#       http://math.stackexchange.com/questions/689526/how-many-connected-graphs-over-v-vertices-and-e-edges
#       When using the reccurrence to find G(n, k), I made certain that all neccessary values of G(.,.)
#       were computed and memoized before they were needed, thus avoiding the need for recursion. This is
#       sometimes called bottom-up memoization. This was one mayor optimization.

# Other optimizations included:
# - Doing Exponentiation by Squaring instead of by using python's built-in pow, which is faster or at worst-case as fast.
# - In three different loops in the code, using a previous binomial coefficient
#    to compute the next binomial coefficient in constant time,
#    instead of computing the next binomial coefficient from scratch in longer than constant time.
#    I used two 'exploits' for this:
#    - 'Exploit': ( n CHOOSE (r+1) ) = ( n CHOOSE r ) * (n-r) / (r+1)
#    - 'Exploit': ( n CHOOSE (r-1) ) = ( n CHOOSE r ) *  r    / (n-r+1)
#                           as long as ( n CHOOSE r ) != 0
#    This was the case with the variables:
#    - a_CHOOSE_m
#    - b_CHOOSE_p
#    - m_CHOOSE_r

from operator import mul

mem_has_been_setup = False
n_max= 20

#            -----len(mem[n])-----
mem= [ [-1]*( n*(n-1)/2 - (n-1) +1) for n in range(1, n_max +1) ]
# mem stores non-zero values of G(n, k) for
#                                       1   <= n <= n_max
#                                       n-1 <= k <= n(n-1)/2
#
# Once computed, G(n, k)   is stored in mem[n -1][k -(n-1)]
# Equivalently,  mem[i][j] stores         G(i +1, j +(n-1)),
#                                   if it has been computed.

mem_left_tally=  [0]*n_max
# mem_left_tally[i] indicates that mem[i][j]
# has been computed for all j <   mem_left_tally[i]
 
mem_right_tally= [0]*n_max
# mem_righ_tally[i] indicates that mem[i][h]
# has been computed for all h >= mem_right_tally[i]

def answer(n, k):
    
    if mem[n -1][k -(n-1)] != -1:
        # G(n, k) has been computed and memoized at mem[n-1][k- (n-1)]
        return mem[n -1][k -(n-1)]
    
    if not mem_has_been_setup:
        # print "setting up mem..."
        setup()
    
    # compute and memoize all uncomputed G(c, d) for
    #                                            1 <= c <= n-1
    #                                          c-1 <= d <= k
    
    for c in xrange( 6, n-1 +1 ):
        
        last_computed_left_d=   mem_left_tally[c -1] +(c-1) -1
        last_computed_right_d= mem_right_tally[c -1] +(c-1)
        
        for d in xrange( last_computed_left_d +1, min(last_computed_right_d, k +1) ):
            
            compute_and_memo(c, d)
    
    # now we can compute and memoize G(n, k)
    compute_and_memo(n, k)
    return mem[n -1][k -(n-1)]

def compute_and_memo(n, k):
    global mem, mem_left_tally
    
    outer_sum_over_m= 0

    # INVARIANT 1:
    # a_CHOOSE_m wil hold the qunatity (n-1 choose m)
    # as m changes, a_CHOOSE_m will change accordingly to maintain INVARIANT 1
    a= n-1
    #m = 0
    a_CHOOSE_m= 1
    
    for m in xrange(0, n-2 +1):
        
        k_max= ((m+1)*m) / 2
        
        inner_sum_over_p= 0
        
        # INVARIANT 2:
        # b_CHOOSE_p wil hold the qunatity ( (n-1-m)(n-2-m)/2 choose p)
        # as p changes, b_CHOOSE_p will change accordingly to maintain INVARIANT 2
        b= ((n-1-m)*(n-2-m)) / 2
        p= min(b, k-m)
        b_CHOOSE_p= nCr(b, p)
        
        for p in xrange(min(b, k-m), max(k-k_max -1, 0 -1), -1):
            
            # n' = m+1
            # k' = k-p
            
            # k' is in [n'-1, n'(n'-1)/2 + 1]
            # s.t. G(n', k') is non-zero
                                            # G(m+1   , k-p         )
            inner_sum_over_p+= b_CHOOSE_p * mem[m+1 -1][k-p -(m+1-1)]
            
            b_CHOOSE_p= ( b_CHOOSE_p * p ) / (b-p+1) # maintains INVARIANT 2
        
        outer_sum_over_m+= a_CHOOSE_m * inner_sum_over_p
        
        a_CHOOSE_m= ( a_CHOOSE_m * (a-m) ) / (m+1)   # maintains INVARIANT 1

    result= nCr( (n*(n-1))/2, k ) - outer_sum_over_m
    
    mem_left_tally[n -1]= k -(n-1) +1
    mem[n -1][k -(n-1)]=  result

def setup():
    global mem, mem_left_tally, mem_righ_tally, mem_has_been_setup

    mem[0][-1]= 1 # equivalently mem[0][0]= 1
    mem[1][-1]= 1 # equivalently mem[1][0]= 1
    
    for n in xrange(3, n_max +1):
        mem[n -1][ 0]= exp_by_squaring_iterative(n, n-2)
        mem[n -1][-1]= 1
        
    mem_left_tally= [1]*n_max
    
    for n in xrange(4, n_max +1):
        
        k_max_n= (n*(n-1)) / 2
        
        # cutting r edges from complete_graph_n
        #                               how many ways to
        #                               sever connectivity
        #  1)       1 <= r <    n-1      0
        #  2)            r =    n-1      n
        #  3)       n <= r < 2*(n-2)     n * nCr(m - (n-1), r - (n-1))

        # INVARIANT:
        # m_CHOOSE_r wil hold the qunatity (k_max_n choose r)
        # as r changes, m_CHOOSE_r will change accordingly to maintain the invariant
        
        m= k_max_n
        #r = 1
        m_CHOOSE_r= m
        
        # 1)
        for r in xrange(1, n-1):
            mem[n -1][-(r+1)]= m_CHOOSE_r
            m_CHOOSE_r= ( m_CHOOSE_r * (m-r) ) / (r+1)
        
        # 2)
        r= n-1
        mem[n -1][-(r+1)]=     m_CHOOSE_r - n
        m_CHOOSE_r= ( m_CHOOSE_r * (m-r) ) / (r+1)

        #r = n
        
        # 3)
        for r in xrange(n, 2*(n-2)):
            mem[n -1][-(r+1)]= m_CHOOSE_r - n * nCr(m - (n-1), r - (n-1))
            m_CHOOSE_r= ( m_CHOOSE_r * (m-r) ) / (r+1)
        
        assert r == 2*(n-2) -1

        # mem_righ_tally[i] indicates that mem[i][h] has been computed for all h >= mem_right_tally[i]
        mem_right_tally[n -1]= len(mem[n -1]) -(r+1)
        
        mem_has_been_setup= True
        
# modified from Wikipedia
def exp_by_squaring_iterative(x, n):
    if n == 0:
        return 1 if x != 0 else "error"
    
    # let X = original value of x
    # let N = original value of n
    acc= 1
    
    # INV:
    #  X**N = acc * x**n
    #
    #  if n is even
    #     acc'= acc
    #     x'= x**2
    #     n'= n/2
    #  s.t. X**N = acc * x**n = acc' * x'**n'
    #  if n is odd
    #     acc' = acc*x
    #     x'= x**2
    #     n'= (n-1)/2
    #  s.t. X**N = acc * x**n = acc' * x'**n'
    #
    # STOP when n == 1
    #  because X**N = acc * x**n = acc * x
    #  so acc*x is X**N, the answer 
    while n > 1:
        if n % 2 == 0:
            # n is even
            #acc= acc
            n= n/2 # n>>1
        else:
            # n is odd
            acc*= x # this line must execute before x= x**2
            n= (n-1)/2 # (n-1)>>1
        x= x**2

    return acc * x

# credit to dheerosaur on StackExchange
# http://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
def nCr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(mul, xrange(n, n-r, -1))
    denom = reduce(mul, xrange(1, r+1))
    return numer/denom
    
# print answer(19 +1, 135 +19-1)