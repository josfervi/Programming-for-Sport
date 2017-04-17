# https://codility.com/demo/results/training2JXGRU-7ZA/#

OPEN =   "({["
CLOSED = ")}]"

def solution(s):
    
    open_braces = []
    
    for brace in s:
        
        if brace in OPEN:
            # brace is on of ({[
            open_brace = brace
            open_braces.append(brace)
            continue
            
        if not brace in CLOSED:
            # brace is not one of (){}[]
            return 0
        
        # brace is one of )}]
        
        closed_brace = brace
        
        if len(open_braces) == 0:
            # there are no open braces to match closed_brace
            return 0
        
        open_brace = open_braces.pop()
        
        if not matched(open_brace, closed_brace):
            # open_brace does not match closed_brace
            return 0
    
    if len(open_braces) != 0:
        # at least one open brace was not matched
        return 0
    else:
        # all open braces were matched
        return 1

def matched(open_brace, closed_brace):
    try:
        return OPEN.index(open_brace) == CLOSED.index(closed_brace)
    except:
        return False