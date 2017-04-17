def better_fibonacci(n):
    
    if n == 0:
        return 0
    
    i = 1
    fib_i = 1
    fib_im1 = 0
    
    # INVIARIANT:
    #   at beg of while:
    #     fib_i == fib[i]
    #     fib_im1 == fib[i-1]
    while i < n:
        
        fib_im1, fib_i = fib_i, fib_im1+fib_i
        
        i += 1
    
    return fib_i