# https://www.interviewbit.com/problems/prime-sum/

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
        #   # use bin search to determine if N-prime is in primes
        #   # make sure your implementation of bin search is not recursive because Python's function call overhead is significant
        #   # instead use an iterative implementation of bin search, this can be done because bin search is tail recursive

class Solution:
    # @param A : integer
    # @return a list of integers
    
    primes= []
    
    def generatePrimesUpTo(self, N):
        
        Solution.primes= [2, 3, 5, 7]
        
        candidate= 11
        add2= True   # using add2, candidate grows while taking on values of the form
                     # 6*i -1 or 6*i +1 only;
                     # such values are divisible by neither 2 nor 3
                     # and values not of this form are divisible by at least one of 2 or 3 (therefore they can be discarded since they are guaranteed not prime)
                     # the first few values that candidate takes on are 5,7, 11,13, 17,19, 23,25, 28,31 ...
        while candidate <= N:
            
            # if candidate is not divisible by any prime in primes[1:] intersection [5...sqrt(m)]
            # then m is prime
            
            sqrt_candidate= int(candidate**0.5)
            
            for divisor in Solution.primes[2:]:
                
                if candidate % divisor == 0:
                    # divisor divides candidate
                    # candidate is not prime
                    break
                if divisor > sqrt_candidate:
                    # if no prime <= int(sqrt(candidate)) divides candidate
                    # then candidate is prime
                    Solution.primes.append(candidate)
                    break
                
            if add2: candidate+= 2
            else:    candidate+= 4
            
            # toggle add2:
            add2^= True
    
    def primesum(self, A):
        
        N= A
        
        if N == 4:
            return [2, 2]
        
        # N > 4
        # since N is even, 2 cannot part of the answer
        
        # useful to first generate a list of primes in [3...n/2]
        # e.g. if N= 22
        #      generate primes [2,3,5,7,11]
        
        self.generatePrimesUpTo(N/2)
        
        for prime in Solution.primes:
            
            candidate= N-prime
            
            sqrt_candidate= int(candidate**0.5)
        
            for divisor in Solution.primes[1:]:
                if divisor > sqrt_candidate:
                    second_prime= candidate
                    return [prime, second_prime]
                
                if candidate % divisor == 0:
                    break
                    
            
            # if self.isPrime(N-prime):
            #     other_prime= N - prime
            #     return [prime, other_prime]
        
        return "error"
        
    def isPrime(self, candidate):
        ''' Precondition: Solution.primes contains all primes up to int(sqrt(candidate))'''
        ''' Precondition: candidate is odd '''
        
        sqrt_candidate= int(candidate**0.5)
        
        for divisor in Solution.primes[1:]:
            if divisor > sqrt_candidate: return True
            if candidate % divisor == 0: return False
    
    def is_in(self, target, sorted_lst):
        '''return target is in sorted_lst assuming sorted_lst is sorted'''
        '''impl detail: uses iterative (non-recursive) binary search for O(logN) perf; +perf'''
        
        N= len(sorted_lst)
        
        l,r = 0, N-1
        while l<=r:
            mid= (r+l)/2
            midValue= sorted_lst[mid]
            if   target   <  midValue: r= mid - 1
            elif midValue == target:   return True
            else:                      l= mid + 1
        
        return False

sol= Solution()
# print sol.primesum(10) == [3,7]
print sol.primesum(1048574) == [3, 1048571]