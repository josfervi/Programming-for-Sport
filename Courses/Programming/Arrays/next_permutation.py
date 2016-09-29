class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        if len(A) == 1:
            return A
        
        if len(A) == 2 or A[-2] < A[-1]:
            A[-2], A[-1] = A[-1], A[-2]
            return A
        
        # { len(A) > 2 }
        # { A[-2] >= A[-1] }
        
        # INVARIANT:
        # tail is in maximal ordering, meaning
        # if tail = [a1 a2 a3 ... al], then a1 >= a2 >= a3 >= ... >= al
        
        tail_strt= len(A) -2          # tail = A[tail_strt:]
        max_tail= A[tail_strt] # the largest elem of tail,
                               # since tail is in maximal ordering,
                               # max_tail = A[tail_strt]
        
        while tail_strt > 0:
            if A[tail_strt -1] >= max_tail:
                tail_strt-= 1
                max_tail= A[tail_strt]
            else:
                break
        
        # either { tail_strt == 0 s.t. tail = A and A is in maximal ordering        } or
        #        { a = A[tail_strt -1] < max_tail and tail = is in maximal ordering,
        #          meaning a + tail is not in maximal ordering                      }
        
        if tail_strt == 0:
            # A is in maximal ordering, the next permutation is the lowest ordering, i.e. sorted A
            A.reverse()
            return A
        
        # { a = A[tail_strt -1] < max_tail and tail is in maximal ordering,
        #          meaning a + tail is not in maximal ordering                }

        # Let b be the smallest element of tail that is larger than a
        #  (since a < max_tail, b exists and is at most max_tail).
        #  Noting that tail is in maximal ordering, i.e. sorted in reverse order.
        
        # Let tail' be tail with b replaced by a
                                                                  # --returns None-
        # The next ordering of a+tail is b+lowest_ordering(tail') = tail'.reverse(), b+tail'
        # which can also be accomplished by swapping a and b and then reversing tail' in place
        
        a= A[tail_strt -1]
        
        i= tail_strt
        while i < len(A):
            if A[i] > a:
                i+= 1
            else:
                break
        
        # either { i=len(A) and b=A[-1]=A[i -1] } or
        #        { i<len(A) and b=      A[i -1] }
        # { b=A[i -1] }
        
      # -------a-------  ---b---   ---b---  -------a-------
        A[tail_strt -1], A[i -1] = A[i -1], A[tail_strt -1]
        
        # reverse tail' in place
        # can't do tail'= A[tail_strt:], tail'.reverse() because that would allocate extra memory
        
        for j in xrange( ( len(A) - tail_strt ) / 2 ):
            # swap
            A[tail_strt +j], A[-1 -j] =  A[-1 -j], A[tail_strt +j]
        
        return A

sol= Solution()
sol.nextPermutation([ 701, 319, 695, 52 ])
        