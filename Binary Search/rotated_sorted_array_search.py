# https://www.interviewbit.com/problems/rotated-sorted-array-search/

# note: I think rotation is a misnomer/uncommon alias
#       To clarify, what is meant by rotation is cyclic shifting

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, lst, target):
        
        # PLAN: develop binary search that works on a sorted list that has been shifted
        #       will need to convert indexes in the shifted list to indexes in the unshifted list
        
        # lst is a sorted list, say [ a, b, c, d, e, f, g, h ]
        # that has been cyclic shifted a number of positions
        # after shifting it looks like
        #   [ e, f, g, h, a, b, c, d ]
        #     and
        #   e < f < g < h > a < b < c < d
        #     and
        #   a < b < c < d <= e
        #
        #   technically, all '<' should be '<='
        
        # find the number of positions that the sorted list was shifted
        # equivalently find the idx of the minimum in the list
        N= len(lst)
        
        l= 0
        r= N-1
        
        while l < r:
            mid_idx= (l+r) / 2
            mid_val= lst[mid_idx]
            end_val= lst[r]
            if   mid_val <= end_val: r= mid_idx
            else:                    l= mid_idx + 1
        
        assert l == r
        assert lst[l-1] >= lst[l]
        
        shift_cnt= l # l also equals the index of the min-valued elem of lst
        
        # lst[shift_cnt:] + lst[:shift_cnt] is the sorted list
        
        max_= lst[shift_cnt - 1]
        min_= lst[shift_cnt]
        end_= lst[-1]
        
        if target < min_: return -1
        elif target <= end_:
            return self.bin_search_within(lst, target, l= shift_cnt, r= N-1)
        elif target <= max_:
            return self.bin_search_within(lst, target, l= 0, r= shift_cnt-1)
        else: return -1
    
    def bin_search_within(self, lst, target, l, r):
        ''' search lst[l:r+1] for target
            if found, return its index,
            otherwise, return -1 '''
        
        while l <= r:
            mid_idx= (l+r) / 2
            mid_val= lst[mid_idx]
            
            if   target  <  mid_val:  r= mid_idx - 1
            elif mid_val == target:   return mid_idx
            else:                     l= mid_idx + 1 # target > mid_val
        
        return -1

# sol= Solution()
# sol.search([ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ], 202)
    
    def bin_search_on_shifted_list(self, lst, target, shift_cnt):
        
        N= len(lst)
        
        l, r = 0, N-1
        
        while l <= r:
            
            mid_idx= (r+l) / 2
            
            mid_idx_prime= ( mid_idx + shift_cnt ) % N
            
            mid_val= lst[mid_idx_prime]
            
            if   target  <  mid_val: r= mid_idx - 1
            elif mid_val == target:  return mid_idx_prime
            else:                    l= mid_idx + 1 # target > mid_val
        
        return -1
    
    def search_that_is_CORRECT_but_fails_EFFICIENCY(self, lst, target):
        
        # FIX: develop binary search that works on a sorted list that has been shifted
        #      will need to convert indexes in the shifted list to indexes in the unshifted list
        
        # possible bug: even though lst is not a tuple
        #               lst[:]= ...
        #               uncorrectly triggers a tuple assignment is not supported ERROR
        
        # lst is a sorted list, say [ a, b, c, d, e, f, g, h ]
        # that has been cyclic shifted a number of positions
        # after shifting it looks like
        #   [ e, f, g, h, a, b, c, d ]
        #     and
        #   e < f < g < h > a < b < c < d
        #     and
        #   a < b < c < d <= e
        #
        #   technically, all '<' should be '<='
        
        # find the number of positions that the sorted list was shifted
        prev_elem= lst[0]
        shift_cnt= 0
        for i, elem in enumerate(lst[1:]):
            
            idx= i+1 # convert from index of lst[1:] to index of lst
            
            if prev_elem > elem:
                shift_cnt= idx
                break
        
        N= len(lst)
        
        # lst[shift_cnt:] + lst[:shift_cnt] is the sorted list
        
        # in-place unshift the list, this may create temp lists due to slicing
        # so that you can bin search on it
        lst[:]= lst[shift_cnt:] + lst[:shift_cnt]
        
        idxOfTarget= self.bin_search(lst, target)
        # convert this result
        if idxOfTarget == -1:
            # target was not found, do nothing to idxOfTarget
            pass
        else:
            # target was found in sorted list, convert idxOfTarget
            # so that it corresponds to the index of Target in the shifted list
            idxOfTarget= (idxOfTarget + shift_cnt) % N
        
        # in-place reshift the list, this may create temp lists due to slicing
        # so that the function does not have lasting side effects
        lst[:]= lst[ N - shift_cnt : ] + lst[ : N - shift_cnt ]
        
        return idxOfTarget
    
    def bin_search(self, lst, target):
        
        N= len(lst)
        
        l, r = 0, N-1
        
        while l <= r:
            
            mid_idx= (r+l) / 2
            mid_val= lst[mid_idx]
            
            if   target  <  mid_val: r= mid_idx - 1
            elif mid_val == target:  return mid_idx
            else:                    l= mid_idx + 1 # target > mid_val
        
        return -1

# sol= Solution()
# print sol.search([ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ], 202)