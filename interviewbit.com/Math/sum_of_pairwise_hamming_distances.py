class Solution:
    # @param A : tuple of integers
    # @return an integer
    
    # O(M*N) time
    # - where N == len(nums)
    # - where M is the bit width of num in nums
    #
    # O(M) extra space
    def hammingDistance(self, nums):
        
        MOD = 1000000007
        BIT_WIDTH = 32
        
        
        num_zeros = [0]*BIT_WIDTH
        num_ones  = [0]*BIT_WIDTH
        
        for num in nums:
            
            for i in range(BIT_WIDTH):
                
                mask = 1 << i
                
                bit_is_set_at_pos_i = (num & mask) > 0
                
                if bit_is_set_at_pos_i:
                    num_ones[i] += 1
                else:
                    num_zeros[i] += 1
        
        result = 0
        for i in range(BIT_WIDTH):
            result += (num_ones[i]*num_zeros[i] % MOD)
        
        return (result << 1) % MOD
    
    
    # O(M*N**2)
    # - where N == len(nums)
    # - where M == bitlength of num in nums
    def hammingDistance_slow(self, nums):
        
        MOD = 1000000007
        
        N = len(nums)
        
        sum_o_hamming_dists = 0
        
        for i in range(N):
            
            x = nums[i]
            
            for j in range(i+1, N):
                
                y = nums[j]
                
                sum_o_hamming_dists = (sum_o_hamming_dists + self.d(x,y)) % MOD
        
        return (sum_o_hamming_dists << 1) % MOD
    
    def d(self, x, y):
        
        diff = x^y
        
        return self.count_ones(diff)
    
    # O(answer)
    # worst case O(M) where M is the bitlength of diff
    def count_ones(self, diff):
        
        count = 0
        while diff:
            diff = (diff & (diff-1))
            count += 1
        return count

# d(x,x) == 0
# d(x,y) == d(y,x)