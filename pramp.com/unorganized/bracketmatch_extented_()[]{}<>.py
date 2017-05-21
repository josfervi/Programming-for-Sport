CLOSING_to_OPENING = {')':'(', ']':'[', '}':'{', '>':'<'}
OPENING_to_CLOSING = {'(':')', '[':']', '{':'}', '<':'>'}

import collections

def bracketMatch_extended(brackets):
    
    closing_indeces = collections.defaultdict(list)
    closing_ptr = collections.defaultdict(int)
    opening_indeces = collections.defaultdict(list)
    opening_ptr = collections.defaultdict(int)
    for idx, bracket in enumerate(brackets):
        if bracket in CLOSING_to_OPENING:
            closing_indeces[bracket].append(idx)
        else:
            opening_indeces[bracket].append(idx)
    
    def helper(brackets, idx=0, count_soFar=0):
        
        if idx > len(brackets):
            return count_soFar
        
        if idx == len(brackets):
            return count_soFar
        
        bracket = brackets[idx]
        
        if bracket in OPENING_to_CLOSING:
            opening = bracket
            closing = OPENING_to_CLOSING[opening]
            
            ptr  = closing_ptr[closing]
            idxs = closing_indeces[closing]
            while ptr<len(idxs) and idxs[ptr]<idx:
                assert False
                count_soFar += 1
                ptr += 1
            
            if ptr == len(idxs):
                # there are no closing brackets in brackets[idx:]
                # close opening immediately
                # to close it we will need
                # to add a closing right after opening 
                count_soFar += 1
                # once we close opening, we can ignore it
                
                # print 'is this correct?'
                return helper(brackets, idx+1, count_soFar)
                #                       ?????
                # or should I be considering
                # brackets[:i]+brackets[i+1:]
                # ???
                # return count_soFar + bracketMatch_extended(brackets[:idx]+brackets[idx+1:])
                
                # for the first 12 tests,
                # line 42 and line 47 produce the same result
            else:
                if idxs[ptr] == idx+1:
                    
                    # we can close opening with the bracket
                    # to its right, which is a closing
                    
                    return bracketMatch_extended(brackets[:idx]+brackets[idx+2:])
                    # there might be a more efficient way
                    # if you 'zero' out brackets[i:i+2]
                    # we would be able to call
                    # helper(brackets, i+1?, count_soFar) instead
                else:
                    # there is at least one closing after opening
                    # but not immediately after opening
                    # i.e. there is at least one
                    # closing in brackets[i+2:]
                    
                    # may have ~~many~~ choices
                    
                    # choice 1:
                    #  close it immediately
                    choice1_res = count_soFar + 1 + bracketMatch_extended(brackets[:idx]+brackets[idx+1:])
                    
                    # other choices
                    #   explore
                    #   matching opening with each subsequent closing,
                    #   one at a time
                    #   and finally match it with the closing
                    #   that results in the minimum
                    best_choice_soFar = choice1_res
                    for c in idxs[ptr:]:
                        curr_choice_res = count_soFar + bracketMatch_extended(brackets[idx+1:c]) + bracketMatch_extended(brackets[:idx] + brackets[c+1:])
                        best_choice_soFar = min(best_choice_soFar, curr_choice_res)
                    return best_choice_soFar
        else:
            # bracket in CLOSING_to_OPENING
            closing = bracket
            openting = CLOSING_to_OPENING[closing]
            
            ptr = closing_ptr[closing]
            idxs = closing_indeces[closing]
            if ptr == 0:
                assert idxs[ptr] == idx
            else:
                ptr += 1
                assert idxs[ptr] == idx
            count_soFar += 1
            return count_soFar + bracketMatch_extended(brackets[:idx]+brackets[idx+1:])
    
    return helper(brackets)

# tests

# > immediately closing ( does work
# > matching ( to the first ) does work
#   matching ( to the second ) doesn't work
brackets = '(()[[[[)]]]]' # '()()[[[[()]]]]'
                          # '(())[[[[()]]]]'
print bracketMatch_extended(brackets) == 2

# > immediately closing ( doesn't work
#   matching ( to the first ) doesn't work
#   in this case you must match ( to the second )
brackets = '({{{{)}}}}[[[[)]]]]'
print bracketMatch_extended(brackets) == 3

#   immediately closing ( doesn't work
# > matching ( to the first ) doesn't work
#   in this case you must match ( to the second )
brackets = '([])[)]'
print bracketMatch_extended(brackets) == 1

#   immediately closing ( doesn't work
# > matching ( to the first ) doesn't work
#   in this case you must match ( to the second )
brackets = '([])()'
print bracketMatch_extended(brackets) == 0

#   immediately closing ( doesn't work
#   matching ( to the first ) doesn't work
# > in this case you must match ( to the second )
brackets = '([)])' # '([()])'
print bracketMatch_extended(brackets) == 1

#   immediately closing ( doesn't work
#   matching ( to the first ) doesn't work
# > in this case you must match ( to the second )
brackets = '({{(}}[[)]])' # '({{()}}[[()]])'
print bracketMatch_extended(brackets) == 2

brackets = ']['
print bracketMatch_extended(brackets) == 2

brackets = '(][)'
print bracketMatch_extended(brackets) == 2

brackets = ']{'
print bracketMatch_extended(brackets) == 2

brackets = '((([)'
print bracketMatch_extended(brackets) == 3

brackets = '(}{)'
print bracketMatch_extended(brackets) == 2

brackets = '({((([)}])))'
print bracketMatch_extended(brackets) # 4???

brackets = '[(]'
print bracketMatch_extended(brackets) == 1

'''
# (){}[]<>

#  ([ ) ]  ==  ( [ )]
#  ([]) ]  ==  ( [])]
#  ([])[]  != [( [])]
# or
#  ([ ) ]  ==  ( [ )]
#  ([() ]  ==  ( [()]
#  ([() ]) !=  ()[()]
    
# ([{(
'''