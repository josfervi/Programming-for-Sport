# tags: invariant programming
#       communiting with vases
#       accumulator
#       equivalence of tail recurison and iteration

# exploring
#                 perf    comments
# recursive      (bad)
# tail recursive (good)   previous recursive calls need not be saved on the call stack
#                         because they pass all their info to the next recursive call via acc
# and
# iterative      (great)  zero recursive call, in fact, zero function call
#
# solutions to the power function

def pow_recursive(x, n):
    
    if n == 0: return 1
    
    if n % 2 == 0: return pow_recursive(x, n/2) ** 2
    else:          return pow_recursive(x, n-1) * x


def pow_that_calls_pow_tail_recursive(X, N):
    
    return pow_tail_recursive(1, X, N)


def pow_tail_recursive(acc, x, n):
    
    if n == 0: return acc
    
    # INVARIANT: acc * x^n is constant across recursive calls
    
    if n % 2 == 0: return pow_tail_recursive(acc,   x**2, n/2)
    else:          return pow_tail_recursive(acc*x, x,    n-1)


def pow_iterative(X, N):
    
    acc= 1
    x=   X
    n=   N
    
    # INVARIANT X^N = acc * x^n
    
    while n > 0:
        if n % 2 == 0:
            acc= acc
            x=   x**2
            n=   n/2
        else:
            acc= acc*x
            x=   x
            n=   n-1
    
    return acc