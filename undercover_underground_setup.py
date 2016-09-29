# may be incorrect
# kept for comments and solution process

from operator import mul

mem= 0
n_max= 4

def setup():
    global mem
    
    # Sets up a memo for
    # G(n,k) = the number of simple, connected graphs of n labeled vertices and k edges
    # Mne = Maximum number of edges = k_max_n = n(n-1)/2
    # mne = minimum number of edges = k_min_n =   n-1
    
               # ---Mne---       -mne-
    mem= [ [-1]*( n*(n-1)/2 + 1 - (n-1) ) for n in range(1,n_max+1) ]
    
    # once computed for a specific n,k pair,
    # G(n, k) will be stored in mem[n-1][k - (n-1)]
    
    # --the easy cases--
    print "the easy cases"
    for n in xrange(1, n_max+1):
        # G(n, k=k_min_n) = n**n-2
        mem[n-1][0]= exp_by_squaring_iterative(n, n-2)
        
        # G(n, k=k_max_n) = 1
        if mem[n-1][-1] != -1:
            print n,-1,mem[n-1][-1]
        mem[n-1][-1]= 1

    # --the not so hard cases-- when k is close to k_max(n)
    
    # When k = k_max_n, we are dealing with complete graphs.
    # G(n, k= k_max_n) = 1.
    # This means that for each n,
    #  there is only one complete graph containing n labeled vertices.
    # Call the complete graph containing n labeled vertices, compl_graph_n.
    # Each vertex in compl_graph_n has a degree of n-1.
    # Thus, the min cut of compl_graph_n is n-1.
    # This means that we can 'cut' up to (any) n-2 edges from compl_graph_n
    #  without compromising connectivity.
    
    # This is to say that
    #  from graph_compl_n, we can cut any r<n-1 edges of our choice,
    #  and the resulting graph will remain connected.
    
    # The condition of cutting up to (any) n-2 edges from compl_graph_n corresponds to:
    # k_max_n - (n-1) < k < k_max_n, or
    # k= k_max_n - r, r < n-1, where r is the number of edges cut
    # G(n, k=k_max_n - r) = k_max_n choose r
    # As before G(n, k= k_max_n - r) will be stored in mem[n-1][k-(n-1)]
    #                equivalently, this is the same as mem[n-1][-(r+1)]
    
    # When k = k_max_n - (n-1), we must remove n-1 edges from compl_graph_n.
    # We choose n-1 edges from k_max_n edges to be removed.
    # If the chosen n-1 edges share a vertex, v,
    # then after their removal, v will be isolated from all other vertices,
    # thus compromising connectivity.
    # This can happen in 1 of n ways, since there are n vertices.
    # So G(n, k=k_max_n - (n-1)) = (k_max_n choose (n-1)) - n when k = k_max_n - (n-1)
    
    print "the not so hard cases"
    for n in xrange(4, n_max+1):
        k_max_n= n*(n-1)/2
        
        # r = 1
        # invariant: k_max_choose_r= (k_max_n choose r)
        k_max_n_choose_r= k_max_n
        
        for r in xrange(1,n-1):
            # r<n-1, G(n, k_max_n - r) = k_max_n choose r
            # G(n, k_max_n - r) will be stored in mem[n-1][-(r+1)]
            mem[n-1][-(r+1)]= nCr(k_max_n, r) # k_max_n_choose_r
            #k_max_n_choose_r*= k_max_n - r
            #k_max_n_choose_r/= r+1
        
        r= n-1
        if mem[n-1][-(r+1)] != -1:
            print n,r,mem[n-1][-(r+1)]
        mem[n-1][-(r+1)]= nCr(k_max_n, r) - n # k_max_n_choose_r - n
        
        #k_max_n_choose_r*= k_max_n - r
        #k_max_n_choose_r/= r+1
        for r in xrange(n, 2*(n-2)):
            if mem[n-1][-(r+1)] != -1:
                print n,r,mem[n-1][-(r+1)]
            mem[n-1][-(r+1)]= nCr(k_max_n, r) - n*nCr(k_max_n - (n-1), r - (n-1))
            #k_max_n_choose_r - n*nCr(k_max_n - (n-1), r-(n-1))
            #k_max_n_choose_r*= k_max_n - r
            #k_max_n_choose_r/= r+1