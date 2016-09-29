from operator import mul

n_max= 20
mem=    0
# mem stores non-zero values of G(n, k) for
#                   1   <= n <= n_max
#                                       n-1 <= k <= n(n-1)/2
#
#                 G(n, k)   is stored in mem[n-1][k - (n-1)]
# equivalently, mem[i][j] stores           G(i+1, j + (n-1))

mem_left_tally=  [0]*n_max
# mem_left_tally[i] indicates that mem[i][j] has been computed for all j <   mem_left_tally[i]
 
mem_right_tally= [0]*n_max
# mem_righ_tally[i] indicates that mem[i][h] has been computed for all h >= mem_right_tally[i]

def answer(n, k):
    setup()
    
    for c in xrange(6, n-1 +1):
        for d in xrange( m )


def setup():
    global mem
    
    mem= [ [-1]*( n*(n-1)/2 + 1 - (n-1) ) for n in range(1, n_max+1) ]

    mem[0][-1]= 1 # equivalently mem[0][0]= 1
    mem[1][-1]= 1 # equivalently mem[1][0]= 1
    
    for n in xrange(3, n_max+1):
        mem[n-1][ 0]= exp_by_squaring_iterative(n, n-2)
        mem[n-1][-1]= 1
        
    mem_left_tally= [1]*n_max
    
    for n in xrange(4, n_max+1):
        
        k_max_n= n*(n-1)/2
        
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
            mem[n-1][-(r+1)]= m_CHOOSE_r
            m_CHOOSE_r= ( m_CHOOSE_r * (m-r) ) / (r+1)
        
        # 2)
        r= n-1
        mem[n-1][-(r+1)]=     m_CHOOSE_r - n
        m_CHOOSE_r= ( m_CHOOSE_r * (m-r) ) / (r+1)

        #r = n
        
        # 3)
        for r in xrange(n, 2*(n-2)):
            mem[n-1][-(r+1)]= m_CHOOSE_r - n * nCr(m - (n-1), r - (n-1))
            m_CHOOSE_r= ( m_CHOOSE_r * (m-r) ) / (r+1)
        
        assert r == 2*(n-2) - 1

        # mem_righ_tally[i] indicates that mem[i][h] has been computed for all h >= mem_right_tally[i]
        mem_right_tally[n-1]= len(mem[n-1]) - (r+1)
        
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

setup()