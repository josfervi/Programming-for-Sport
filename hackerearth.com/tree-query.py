# https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/tree-query/?utm_source=header&utm_medium=search&utm_campaign=he-search

# https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/tree-query/

def answer():
    ''' Reads in input and computes answer
    '''
    
    # num nodes, num edges
    n, m = map(int, raw_input().split(' '))
    
    outdeg_in_fwd_dag = [0] * n
    outdeg_in_rev_dag = [0] * n
    
    for i in range(m):
        
        # read in input
        u, v = map(int, raw_input().split(' '))
        
        # convert u, v from 1-indexed to 0-indexed
        u -= 1
        v -= 1
        
        outdeg_in_fwd_dag[u] += 1
        outdeg_in_rev_dag[v] += 1
    
    return max(
        len( filter( lambda x : x < 1, outdeg_in_fwd_dag)),
        len( filter( lambda x : x < 1, outdeg_in_rev_dag))
    )


print answer()