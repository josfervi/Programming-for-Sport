# https://www.interviewbit.com/problems/maximum-consecutive-gap/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        
        N= len(A)
        
        if N < 2: return 0
        
        # characterize the input array A
        min_of_A= A[0]
        max_of_A= A[0]
        for a in A[1:]:
            min_of_A= min(min_of_A, a)
            max_of_A= max(max_of_A, a)
        
        range_of_A= max_of_A - min_of_A
        
        # having obtained the min of A and the max of A
        # we know:
        #    maximumGap(A) <= max_of_A - min_of_A
        #
        # we can also deduce the minimum possible value of maximumGap(A)
        # because it occurs when all gaps in the sorted version of A are equalised
        # this is akin to divying up range_of_A into (N-1) gaps
        #    (max_of_A - min_of_A) div (N-1) <= maximumGap(A)
        #                          div denotes floating point division
        # 
        # defining range_of_A as max_of_A - min_of_A
        #  ( / denotes integer division)
        # 
        # gap' = range_of_A / (N-1) <= range_of_A div (N-1) = gap <= maximumGap(A) <= range_of_A
        
        if   range_of_A == 0: return 0
        elif range_of_A == 1: return 1 # A.sort() == [a, a, ... a, b, b, ... b], maximumGap(A) == b-a = 1
        
        # { range_of_A >= 2}
        
        gap= float(range_of_A) / float(N-1)
        
        # we will do one more pass over the input array A,
        # this time bucketing each element into one of (N-1) buckets
        # Buckect i will catch elements in the real interval [min_of_A + i*gap, min_of_A + (i+1)*gap)
        #
        # by noting that the maximal difference between two elements in the same bucket, 
        #  = min_of_A + (i+1)*gap - epsilon - (min_of_A + i*gap)
        #  = gap-epsilon,
        # is strictly smaller than the smallest possible value of maximumGap(A), gap,
        # we deduce that the maximum gap cannot occur between two elements of the same bucket
        #
        # indeed the maximum gap must occur
        #   between the maximal element of one bucket and the minimal element of the next non-empty bucket
        
        buckets= [[None, None] for i in xrange(N-1)]
        
        min_= 0
        max_= 1
        
        for a in A:
            
            if a == max_of_A: continue
            
            i= int( (a-min_of_A)/gap )
            min_of_bucket_i= buckets[i][min_]
            max_of_bucket_i= buckets[i][max_]
            
            if min_of_bucket_i is None: buckets[i][min_]= a
            else:                       buckets[i][min_]= min(min_of_bucket_i, a)
            
            if max_of_bucket_i is None: buckets[i][max_]= a
            else:                       buckets[i][max_]= max(max_of_bucket_i, a)
            
            # programmer's note: bucket[i][min_] and bucket[i][max_] are either both None or both not None
            # this means the if statements can be combined
        
        # scan the buckets looking for the largest gap
        
        the_max_of_the_prev_non_empty_bucket= None
        max_gap= range_of_A / (N-1)
        for bucket in buckets:
            
            if the_max_of_the_prev_non_empty_bucket is None:
                the_max_of_the_prev_non_empty_bucket= bucket[max_]
                continue
            
            # the_max_of_the_prev_non_empty_bucket is not None
            elif bucket[min_] is not None:
                
                the_min_of_the_curr_bucket= bucket[min_]
                max_gap= max(max_gap, the_min_of_the_curr_bucket - the_max_of_the_prev_non_empty_bucket)
                the_max_of_the_prev_non_empty_bucket= bucket[max_]
        
        max_gap= max(max_gap, max_of_A - the_max_of_the_prev_non_empty_bucket)
        
        return max_gap
        
#sol= Solution()
#sol.maximumGap([ 1,1,2 ])