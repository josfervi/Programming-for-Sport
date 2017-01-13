'''
Args:
    - matrix (list of lists)
      - a square matrix

Modifies:
    - arg into its transpose in-place

Returns:
    - nothing (None)

Complexity:
    - O(n^2) time
    - O(1)   extra space, in-place
'''
def transpose_matrix(matrix):
    
    if matrix is None:
        return None
    
    n= len(matrix)
    
    for i in range(n):
        for j in range(i):
            
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]