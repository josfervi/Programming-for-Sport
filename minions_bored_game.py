# My solution is
# O( TN - N**2 ) time complexity
# O(N) space complexity

# solution inspired by Juan Lopes at Stack Exchange
# http://stackoverflow.com/questions/29837067/number-of-unique-sequences-of-3-digits-1-0-1-given-a-length-that-matches-a-su

# a move = a dice roll

# We are solving the problem for
# N squares and T moves

# lowercase n is a loop variable
# lowercase t is also a loop var

# THREE RESTRICTIONS on a VALID GAME
#
#  There are three restrictions placed on
#  a game (a sequence of moves) in order
#  for it to be considered valid.
#
#  Letting square 0   be the square to the  left of square 1
#      and square N+1 be the square to the right of square N,
#  we can state the restrictions as follows:
#
#  1. The token must never be on square 0.
#  2. The token must never be on square N+1.
#  3. Once the token is on square N, it must stay on square N.

# a RECURRENCE RELATION "SOLUTION"
#
#  Without these restrictions,
#  the problem would be solved by
#  the following recurrence relation:
#
#  G(1,0) = 1
#  G(n,t) = G(n-1, t-1) + G(n, t-1) + G(n+1, t-1)
#
#  where G(n,t) is the number of games
#  for a board of n squares and t moves,
#
#  since we could reach square n in t moves
#   1. by reaching square n-1 in t-1 moves and then moving right or
#   2. by reaching square n   in t-1 moves and then staying      or
#   3. by reaching square n+1 in t-1 moves and then moving left

# ADDRESSING EACH CONSTRAINT
#
#  "Recurrence relation, let me impress upon you the three constraint
#   in the following way"
#
#  Constraint 1.
#  if n = 1: 
#     G(n,t) = G(n, t-1) + G(n+1, t-1)
#     such that the token will never be on square 0
#     i.e. we can only get to square 1 from square 1 or from square 2
#
#  Constraint 2.
#  if n = N:
#     G(n,t) = G(n-1, t-1) + G(n, t-1)
#     such that the token will never be on square N+1
#     i.e. we can only get to square N from square N-1, 
#
#  Constraint 3.
#  if n = N-1:
#     G(n,t) = G(n-1, t-1) + G(n, t-1)
#     such that once the token is on square N it stays on square N
#     i.e. we can not get to square N-1 from square N,
#          we can only get to square N-1 from square N-2 or from square N-1

# CHANGE OF VARIABLES
#
#  The following change of variables is useful for doing away with
#  unnecessary computations. Ask me how.
#
#  M(n, e) is the number of valid games
#  for a board of n squares and
#  e excess moves, e = t - (n-1)
#
#  G(n, t) = M(n, t-(n-1))
#  M(n, e) = G(n, e+(n-1))
#
# Change of varialbes for the common case:
#     G(n,t)       = G(n-1, t-1)         + G(n, t-1)       + G(n+1, t-1)
#     M(n,t-(n-1)) = M(n-1, t-1-(n-1-1)) + M(n, t-1-(n-1)) + M(n+1, t-1-(n+1-1))
#     letting e=t-(n-1)
#     M(n,e)       = M(n-1, e)           + M(n, e-1)       + M(n+1, e-2)
#     M(n,e) = M(n-1, e) + M(n, e-1) + M(n+1, e-2)
#
# The entire recurrence relation becomes:
#  M(n,0) = 1
#  M(n,1) = n
#  if n = 1:
#     M(n,e) = M(n, e-1) + M(n+1, e-2)
#  if n = N-1 or n = N:
#     M(n,e) = M(n-1, e) + M(n, e-1)
#  otherwise:
#     M(n,e) = M(n-1, e) + M(n, e-1) + M(n+1, e-2)

def answer(T, N):
    # your code here
    
    if T <  N-1: return 0
    if T == N-1: return 1
    if T == N:   return N
    
    if N == 1:   return 1
    if N == 2:   return T
    
    M_prev= [None] + [1]*N          # e=0
    M_e=    [None] + range(1, N +1) # e=1
    
    E= T - (N-1)
    
    for e in xrange(2, E +1):
        
        # { M_prev[n] corresponds to M(n, e-2) for each n in [1...N] }
        # { M_e[n]    corresponds to M(n, e-1) for each n in [1...N] }
        
        M_prev, M_e = M_e, M_prev

        # { M_prev[n] corresponds to M(n, e-1) for each n in [1...N] }
        # { M_e[n]    corresponds to M(n, e-2) for each n in [1...N] }
        
        for n in xrange(1, N +1):
            
            # { M_prev[m] corresponds to M(m, e-1) for each m in [1...N  ] }
            # { M_e[m]    corresponds to M(m, e  ) for each m in [1...n-1] }
            # { M_e[m]    corresponds to M(m, e-2) for each m in [n...N  ] }

            if n == 1:
              # M(n,e)= M(n, e-1) + M(n+1, e-2)
                M_e[n]= M_prev[n] + M_e[n+1]
            elif n == N-1 or n == N:
              # M(n,e)= M(n-1, e) + M(n, e-1)
                M_e[n]= M_e[n-1]  + M_prev[n]
            else:
              # M(n,e)= M(n-1, e) + M(n, e-1) + M(n+1, e-2)
                M_e[n]= M_e[n-1]  + M_prev[n] + M_e[n+1]
            
            M_e[n]%= 123454321
            
            # { M_prev[m] corresponds to M(m, e-1) for each m in [1...N  ] }
            # { M_e[m]    corresponds to M(m, e  ) for each m in [1...n  ] }
            # { M_e[m]    corresponds to M(m, e-2) for each m in [n+1...N] }
        
        # { M_prev[n] corresponds to M(n, e-1) for each n in [1...N] }
        # { M_e[n]    corresponds to M(n, e  ) for each n in [1...N] }
    
    # { M_e[n] corresponds to M(n, E) for each n in [1...N] }
    # { G(N,T) = M(N,E) = M_e[N] so the desired result is in M_e[N] }
    
    return M_e[N] % 123454321