import copy

def permutations(word):
    
    if not word:
        return None
    
    _permutations(list(word), l=0)

def _permutations(word, l):
    
    n = len(word)
    
    if l == n-1:
        print ''.join(word)
        return
    
    for i in range(l, n):
        # swap the lth and ith char        
        word[l], word[i] = word[i], word[l]
        
        _permutations(copy.copy(word), l+1)

permutations('abcd')
        