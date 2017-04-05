F = False
def isValidNumber(s, n, c, d):
    
    if s[0] == '-':
        if not n:
            return F
        # n and s[0] == '-'
        s = s[1:]
    
    f = ""
    dc = s.count('.')
    if dc > 0:
        if not d or dc > 1:
            return F
        # d and dc == 1
        s, f = s.split('.')
    
    cc = s.count(',')
    if cc > 0:
        if not c:
            return F
        # c and cc > 0
        ts = s.split(',')
        if not 0 < len(ts[0]) < 4 or any( len(t) != 3 for t in ts[1:] ):
            return F
        s = ''.join(ts)
    
    s += f
    return s.isdigit()