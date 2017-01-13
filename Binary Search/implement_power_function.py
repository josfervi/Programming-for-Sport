# https://www.interviewbit.com/problems/implement-power-function/

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    
    def pow(self, X, N, M):
        
        if M == 1: return 0
        
        return self.pow_iterative(X, N, M)
    
    def pow_iterative(self, X, N, M):
        
        acc= 1
        x=   X % M
        n=   N
        
        # INVARIANT X^N = acc * x^n (ignoring mod)
        
        while n > 0:
            if n % 2 == 0:
                acc= acc
                x=   x**2 % M
                n=   n/2
            else:
                acc= acc*x % M
                x=   x
                n=   n-1
        
        return acc
    
    def pow_that_times_out(self, base, exponent, modulus):
        
        if modulus == 1: return 0
        
        acc= 1
        e_prime= 0
        
        # INVARIANT acc = base^e_prime mod modulus
        while e_prime < exponent:
            
            acc= (acc*base) % modulus
            e_prime+= 1
        
        # e_prime == exponent
        # acc == b^e_prime mod modulus = b^exponent mode modulus
        return acc
    
    def pow_recursive(self, x, n):
        
        if n == 0: return 1
        
        if n % 2 == 0: return self.pow_recursive(x, n/2) ** 2
        else:          return self.pow_recursive(x, n-1) * x
    
    
    def pow_that_calls_pow_tail_recursive(self, X, N):
        
        return pow_tail_recursive(1, X, N)
    
    def pow_tail_recursive(self, acc, x, n):
        
        if n == 0: return acc
        
        if n % 2 == 0: return pow_tail_recursive(acc,   x**2, n/2)
        else:          return pow_tail_recursive(acc*x, x,    n-1)