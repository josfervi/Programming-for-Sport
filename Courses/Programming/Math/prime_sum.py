# correct afaik, but doesn't pass submission because it times out
# it takes really long
# must implement in Java or C++ or C

        # a note about membership testing
        
        # version 1:
        #   n-prime in primes       # list membership testing is too slow
        # version 2:
        #   primes_set= set(primes) # creating a set out of primes list and then
        #   n-prime in primes_set   # testing set membership is also too slow
        # version 3:
        #   primes_set= frozenset(primes) # creating a frozenset of out primes list
        #   n-prime in primes_set         # and then testing frozenset  membership
        #                                 # is also too slow
        # version 4:
        #   # exploiting the fact that primes is an ordered list,
        #   # use bin search to determine if n-prime is in primes
        #   self.bin_search_is_in(n-prime, primes) # still too slow
        # suggesting the bottleneck may not be here after all

from math import sqrt
from bisect import bisect_left

class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        
        n= A
        
        if n == 4:
            return [2, 2]
        
        # useful to first generate a list of primes in [3...n/2]
        # e.g. if n= 22
        #      generate primes= [3,5,7,11]
        
        primes= [3]
        
        m= 5
        add2= True # if add2 is True  at the begining of this iteration of the while loop
                   #    then at the end of this iteration
                   #       m becomes m+2 and
                   #       add2 becomes False
                   # if add2 is False at the begining of this iteration of the while loop
                   #    then at the end of this iteration
                   #       m becomes m+4 and
                   #       add2 becomes True
        while m <= n:
            
            # if m is not divisible by any prime in primes[1:] intersection [5...sqrt(m)]
            # then m is prime
            
            sqrt_m= int(sqrt(m))
            m_is_prime= True # set to False if m is found to not be prime
                             # else remains True
            for prime in primes[1:]:
                
                if prime > sqrt_m:
                    # if no prime <= int(sqrt(m)) divides m
                    # then m is prime
                    # m_is_prime is already True
                    break
                
                if m % prime == 0:
                    # m is not prime
                    m_is_prime= False
                    break
            
            if m_is_prime:
                primes.append(m)
            
            if add2:
                m+= 2
                add2= False
            else:
                m+= 4
                add2= True
        
        # a note about membership testing
        
        # version 1:
        #   n-prime in primes       # list membership testing is too slow
        # version 2:
        #   primes_set= set(primes) # creating a set out of primes list and then
        #   n-prime in primes_set   # testing set membership is also too slow
        # version 3:
        #   primes_set= frozenset(primes) # creating a frozenset of out primes list
        #   n-prime in primes_set         # and then testing frozenset  membership
        #                                 # is also too slow
        # version 4:
        #   # exploiting the fact that primes is an ordered list,
        #   # use bin search to determine if n-prime is in primes
        #   self.bin_search_is_in(n-prime, primes) # still too slow
        # suggesting the bottleneck may not be here after all
        
        for prime in primes:
            assert prime <= n/2
            if self.bin_search_is_in(n-prime, primes):
                return [prime, n - prime]
        
        return "error"
    
    # binary search modified from
    # https://docs.python.org/2/library/bisect.html
    # section 8.5.1
    def bin_search_is_in(self, x, a):
        'return x is in a assuming a is sorted, using binary search for +perf'
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return True
        return False

sol= Solution()
print sol.primesum(1048574) == [3, 1048571]