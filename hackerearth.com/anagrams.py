def anagrams(A, B):
    """Returns true if A is an anagram of B.
           Otherwise, returns false.
    """
    
    # Python Peculiarity: sorting strings
    #   A.sort() throws AttributeError: 'str' object has no attribute 'sort'
    #   list(A).sort() is valid
    #   but you'd have to do
    #     A = list(A)
    #     A.sort()
    #   
    #   sorted(A) works without having to turn A into a list
    
    A = sorted(A)
    B = sorted(B)
    
    return A == B

N = raw_input()
A = raw_input()
B = raw_input()

result = "YES" if anagrams(A, B) else "NO"
print result