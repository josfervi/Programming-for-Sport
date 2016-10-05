class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        
        primes= [2,3,5,7]
        
        candidate= 11
        add2=      True
        while candidate <= A:
            
            # if candidate is not divisible by any prime <= sqrt(candidate) then candidate is     prime
            # if candidate is     divisible by any prime <= sqrt(candidate) then candidate is not prime
            
            sqrt_= int(candidate**0.5)
            j= 2
            prime= primes[j] # 5 # note: candidates are generated in such a way that
                                 #       that guarantees they are not multiples of 2 or 3
            candidate_is_prime= True # remains True if candidate is prime
                                     # otherwise becomes False once candidate is known to not be prime
            while prime <= sqrt_:
                if candidate % prime == 0:
                    candidate_is_prime= False
                    break
                j+= 1
                prime= primes[j]
            
            if candidate_is_prime:
                primes.append(candidate)
            
            if add2:
                candidate+= 2
                add2= False
            else:
                candidate+= 4
                add2= True
        
        return primes
