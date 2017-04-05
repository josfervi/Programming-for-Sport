import test_decomp


# Let N be the len of the compressed string.
# Let M be the len of the decompressed string.
# O(M) time
#   - the while loop does N iterations, increasing i from 0 to N
#   - most things in the while loop are O(1)
#   - the only exception is join which is linear in either
#     - the number of items being joined (MY GUESS)
#     - the number of characters in the resulting join
#   - in the worst case the we might be joining M one-character strings
# O(M) extra space 
def decomp(s):
    """
    Return the decompression of compressed string s.
    
    Let <a> := [a-zA-Z]
    Let <w> := <a>*
    Let <n> := \d+
    Let <u> := <n>\[<w>\]              (Unnested compressed unit)
    Let <r> := (<n>\[(<w><r><w>)*\])*  (Nested compressed string.
                                        Must be a finite nesting.
                                        Eventually, the nested <r>
                                        must be an empty string.)
    Let <s> := <r>*
    
    The decompression of <u> := <n>\[<w>\] is w*int(n).
    That is, the string w repeated int(n) times.
    
    For example:
    
    (In this example, disregard spaces between characters.)
    
    2[f2[2[a]z]c]0[b]4[d]10[]
         \  /    |  ||   \  /
    2[f2[ aa z]c]     dddd
       \      / \    /   /
    2[f aazaaz   c]  dddd
    |              \/   /
    faazaazcfaazaazcdddd
    """
    
    n = len(s)
    
    # The number of unmatched open brackets '[' seen so far.
    open_cnt = 0
    
    # Matched lists.
    # The final value of str_stk[i]
    #   (after doing ''.join(str_stk[i]) must appear
    #   cnt_stk[i] number of times in the result.
    cnt_stk = []
    # To avoid string concatenation, str_stk is a list of lists of strings.
    str_stk = []
    
    TOP = -1
    
    i = 0
    while i < n:
        
        char = s[i]
        
        if char is ']':
            if open_cnt == 0:
                error_msg = (
                    "There is an unmatched closing bracket ']'"
                    " in the input string at index {}."
                    " Please fix it.".format(i) )
                raise ValueError(error_msg)
            
            open_cnt -= 1
            
            cnt = cnt_stk.pop()
            unit_str = ''.join(str_stk.pop())
            
            if not str_stk:
                assert open_cnt == 0
                str_stk.append( [unit_str*cnt] )
            else:
                str_stk[TOP].append( unit_str*cnt )
        
        elif char.isdigit():
            cnt, i = get_cnt(s, i)
            cnt_stk.append(cnt)
            
            # s[i] is the last digit of cnt
            # s[i+1] must be a '['
            
            i, open_cnt = handle_opener(s, i+1, open_cnt)
            
            # s[i] is a '['
            # s[i+1] is the start of 
            
            unit_str, i = get_unit_str(s, i+1)
            str_stk.append( [unit_str] )
        
        elif char.isalpha():
            continuation_str, i = get_unit_str(s, i)
            # continuation_str is the continuation of str_stk
            str_stk[TOP].append( continuation_str )
        
        else:
            error_msg = (
                "String input may only contain letters, numbers, '['s,"
                " and ']'s. This is not the case at index {}"
                " of the string input.".format(i) )
            raise ValueError()
        
        i += 1
    
    str_stk = map(''.join, str_stk)
    return ''.join(str_stk)


def checks_boundaries(fcn):
    
    def wrapper(*args, **kw):
        s = args[0]
        i = args[1]
        
        n = len(s)
        
        if i < 0 or i >= n:
            msg_error = "Input index i == {} is out of bounds."
            if i < 0:
                clarify = "i is negative."
            else:
                clarify = (
                    "i is greater than or equal to the input"
                    " string's length == {}.".format(n) )
            msg_error += " " + clarify
            raise ValueError(msg_error)
        return fcn(*args, **kw)
    
    return wrapper


@checks_boundaries
def handle_opener(s, i, open_count):
    if s[i] is not '[':
        error_msg = (
            "Each number must be followed by an opening bracket '['."
            " This is not the case at index {}"
            " of the input string.".format(i) )
        raise ValueError(error_msg)
    open_count += 1
    return i, open_count


@checks_boundaries
def get_continuation(s, i, isthis, out_type):
    n = len(s)
    if not isthis(s[i]):
        return default_val(out_type), i-1
    h = i
    while i+1<n and isthis(s[i+1]):
        i += 1
    res = out_type(s[h:i+1])
    return res, i


def default_val(out_type):
    if out_type is str:
        return ''
    if out_type is int:
        return 0


def get_cnt(s, i):
    """
    Returns a tuple:
      - The largest numeric substring of s that starts at index i as an int.
      - The value of the index where the substring ends.
    
    For example
    
    If s[i] is not numeric,
    returns the tuple
      - 0
      - i
    
    If s[i] through s[j] are numeric,
    but j+1 == len(s) or s[j+1] is not numeric,
    returns the tuple
      - int(s[i:j+1])
      - j
    """
    return get_continuation(s, i, str.isdigit, int)


def get_unit_str(s, i):
    """
    Returns a tuple:
      - The largest alphabetic substring of s that starts at index i.
      - The value of the index where the substring ends.
    
    For example
    
    If s[i] is not alphabetic,
    returns the tuple
      - s[i:i] == ""
      - i
    
    If s[i] through s[j] are alphabetic, 
    but j+1 == len(s) or s[j+1] is not alphabetic,
    returns the tuple
      - s[i:j+1]
      - j
    """
    return get_continuation(s, i, str.isalpha, str)


# TESTS
test_decomp.test(decomp)


# get_cnt and get_unit_str TESTS
def test_get_continuation():
    #      0123456789ab
    s = 'abc123def443'
    
    cnt, i = get_cnt(s, 3)
    print cnt == 123
    print i == 5
    
    cnt, i = get_cnt(s, 4)
    print cnt == 23
    print i == 5
    
    unit_str, i = get_unit_str(s, 6)
    print unit_str == 'def'
    print i == 8