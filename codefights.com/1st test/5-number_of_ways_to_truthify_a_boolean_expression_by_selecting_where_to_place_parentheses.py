def booleanParenthesization(expression):
    return num_ways_to_truthify(expression)


def num_ways_to_truthify(expression):
    return num_ways_to(True, expression)


def num_ways_to_falsify(expression):
    return num_ways_to(False, expression)


BINARY_OPERATORS = ['&', '|', '^']


TRUES  = set(['T',
              'T&T',
              'T|T',
              'T|F',
              'F|T',
              'T^F',
              'F^T'])


FALSES = set(['F',
              'T&F',
              'F&T',
              'F&F',
              'F|F',
              'T^T',
              'F^F'])



def num_ways_to(truthify, expression):
    
    # base case
    if expression in TRUES:
        return 1 if truthify else 0
    if expression in FALSES:
        return 0 if truthify else 1
    
    count = 0
        
    for i, symbol in enumerate(expression):
        
        if symbol not in BINARY_OPERATORS:
            continue
        
        left_exp = expression[:i]
        right_exp = expression[i+1:]
        
        if truthify and symbol == '&':
            
            count += ( num_ways_to(True, left_exp) *
                       num_ways_to(True, right_exp) )
            continue
        
        if not truthify and symbol == '|':
            
            count += ( num_ways_to(False, left_exp) *
                       num_ways_to(False, right_exp) )
            continue
        
        
        nwTl = num_ways_to_truthify_left_exp  = num_ways_to(True,  left_exp)
        nwTr = num_ways_to_truthify_right_exp = num_ways_to(True,  right_exp)
        nwFl = num_ways_to_falsify_left_exp   = num_ways_to(False, left_exp)
        nwFr = num_ways_to_falsify_right_exp  = num_ways_to(False, right_exp)
        
        # QUESTION:
        #   Is there a closed form for
        #     num_ways_to_truthify(exp) + num_ways_to_falsify(exp)?
        #     i.e. for the total number of ways
        #     to (meaningfully) parenthesize an expression.
        #   If so,
        #     I can use it to reduce the number of recursive calls!
        
        if not truthify and symbol == '&':
            count += ( (nwTl * nwFr) + (nwFl * nwTr) + (nwFl * nwFr) )
        
        elif truthify and symbol == '|':
            count += ( (nwTl * nwTr) + (nwTl * nwFr) + (nwFl * nwTr) )
        
        elif truthify and symbol == '^':
            count += ( (nwTl * nwFr) + (nwFl * nwTr) )
        
        elif not truthify and symbol == '^':
            count += ( (nwTl * nwTr) + (nwFl * nwFr) )
    
    return count

expression = "T|F^F&T|F^F^F^T|T&T^T|F^T^F&F"#^T|T^F"
#                                       
print booleanParenthesization(expression)