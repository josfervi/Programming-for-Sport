def solution(A):
    """Given a non-empty array, A, of N integers,
           find the maximum difference between
           two parts of the array.
           (See problem statement.)
    """
    
    N = len(A)
    
    # Precompute premax and postmax in O(N) time using O(N) extra space.
    
     
    # premax[k] = max(A[:k+1]) = max(A[0], A[1], ..., A[k])
    #
    #   premax[k+1] = max(premax[k], A[k+1])
    #   
    #   premax[k] = A[k] = A[0],            k == 0
    #   premax[k] = max(premax[k-1], A[k]), 0 <  k < N-1    
    premax = [None] * (N-1) # allocate space for premax
    premax[0] = A[0]
    for k in range(1, N-1):
        premax[k] = max(premax[k-1], A[k])
    
    
    # postmax[k] = max(A[k+1:]) = max(A[k+1], A[k+2], ..., A[N-1])
    # 
    #   postmax[k-1] = max(A[k:]) = max(A[k], A[k+1], ..., A[N-1]) = max(A[k], postmax[k])
    #
    #   postmax[k] = A[k+1] = A[N-1],           k == N-2
    #   postmax[k] = max(A[k+1], postmax[k+1]), 0 <= k   < N-2
    postmax = [None] * (N-1)
    postmax[N-2] = A[N-1]
    for k in reversed(range(0, N-2)):
        postmax[k] = max(A[k+1], postmax[k+1])
    
    
    # Find the maximum difference in O(N) time using premax and postmax.
    
    max_difference_soFar = 0 # the smallest possible difference
    
    for k in range(0, N-1):
        
        current_difference = abs(postmax[k] - premax[k])
        max_difference_soFar = max(max_difference_soFar, current_difference)
    
    max_difference = max_difference_soFar
    return max_difference
