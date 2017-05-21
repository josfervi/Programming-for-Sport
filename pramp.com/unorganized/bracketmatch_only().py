# the current number of unmatched open brackets

def bracketMatch(text):
    count = 0
    
    num_un = 0
    
    for bracket in text:
       
        if bracket == '(':
            num_un += 1
        else:
           # bracket == ')'
            if num_un == 0:
                count += 1
            else:
                num_un -= 1
    return count + num_un


# tests

print bracketMatch(')(') == 2
print bracketMatch('(((()))())') == 0