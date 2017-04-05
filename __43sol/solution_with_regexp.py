import re
import test_decompress

RE = '(\d+)\[([a-zA-Z]*)\]'


def _replacement(match):
    cnt = int(match.group(1))
    unit_str = match.group(2)
    return unit_str * cnt


def decompress(s):
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
    match = re.search(RE, s)
    while match:
        s = re.sub(RE, lambda match : _replacement(match), s)
        match = re.search(RE, s)
    return s


test_decompress.test(decompress)