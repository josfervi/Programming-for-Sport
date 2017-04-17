def longestIncreasingSubsequence(sequence):
    
    # dp[i] means that we can achieve
    # a strictly increasing subsequence
    # (hereby subseq) of lenght i with
    # a tail of dp[i]
    
    dp = [None]
    
    for num in sequence:
        
        l,r = bin_search(dp, num)
        
        #          r l
        # [ <num    | >=num ]
        
        # dp[r] means we can achieve a
        # subseq of length r with a tail
        # of dp[r] < num
        # 
        # dp[l] means we can achieve a
        # subseq of length l=r+1 with
        # a tail of dp[l] >= num
        # 
        # if dp[l] == num:
        #   then dp[l] = num
        # if dp[l] > num:
        #   then we can do better
        #   dp[l] = num
        if l >= len(dp):
            dp.append(num)
            continue
        dp[l] = num
    
    return len(dp)-1

def bin_search(nums, target):
    
    #     r l
    # [ <t | >=t ]
    
    l, r = 1, len(nums)-1
    
    while l<=r:
        
        mid_idx = (l+r)/2
        mid_val = nums[mid_idx]
        
        if mid_val < target:
            l = mid_idx + 1
        else:
            r = mid_idx-1
    
    return l,r
