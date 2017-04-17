n = 250

zeros, ones, twos, threes = [], [], [], []
for i in range(n):
    ones.append(4*i + 1)
    twos.append(4*i + 2)
    threes.append(4*i + 3)
    zeros.append(4*i + 4)

def inf_loop(pair):
    
    pairs_observed = set()
    return _inf_loop(pair, pairs_observed)

def _inf_loop(pair, pairs_observed):
    
    a, b = pair
    a, b = min(a,b), max(a,b)
    if a == b:
        return False
    if (a, b) in pairs_observed:
        return True
    pairs_observed.add( (a,b) )
    return _inf_loop( (2*a,b-a), pairs_observed )

def explore(group, group_str):
    ''' Takes zeros/ones/twos/threes as input '''
    
    n = len(group)
    
    print "Which pair of {} lead to inf loop (desired) and lead to equil?".format(group_str)
    print ""
    print "finding answer for all pairs from {}".format(group)
    print ""
    for i in range(n):
        for j in range(i+1, n):
            
            a, b =  group[i], group[j]
            pair = (a, b)
            
            if inf_loop(pair):
                outp_str = "leads to inf loop"
                
                assert not power_of_2(a+b)
                
                # assert predicting_inf_loop_based_on_group_comparison_after_reduction(a, b)
                
                correct = predicting_inf_loop_based_on_group_comparison_after_reduction(a, b)
                prediction_is_wrong = not correct
                if prediction_is_wrong:
                    reduced_pair = reduce(pair)
                    r_a, r_b = reduced_pair
                    print "prediction based on group comparison after reduction was wrong for pair ({}, {}) which reduced to {}. The groups of the reduced pair is ({}, {}) ".format(a, b, reduced_pair, group_of(r_a), group_of(r_b))
                
            else:
                outp_str = "leads to equil"
                
                # known reasons
                # - a+b is a power of 2
                # - 3*a == b as in (12, 36), therefore (a, b) = (a, 3a) -> (2a, 2a)
                
                if power_of_2(a+b) or 3*a == b or a == 3*b:
                    continue
                
                wrong = predicting_inf_loop_based_on_group_comparison_after_reduction(a, b)
                assert not wrong
                
                clarification_str = "FOR UNKNOWN REASON"
                print "the pair ({}, {}) {} + {}. Note, {} + {} = {}. Note, reduces to {}".format(
                a,
                b,
                outp_str,
                clarification_str,
                a,
                b,
                a+b,
                reduce((a,b))
                )
                
        #print ""


def predicting_inf_loop_based_on_group_comparison_after_reduction(a, b):
    
    reduced_pair = reduce((a,b))
    reduced_a, reduced_b = reduced_pair
    group_reduced_a = group_of(reduced_a)
    group_reduced_b = group_of(reduced_b)
    
    if group_reduced_a == 0:
        return group_reduced_b in [1,2,3] # we expect an inf loop when reduced_a is taken from group 0 and reduced_b is taken from any other group
    
    if group_reduced_a == 1:
        # barring a == b
        return group_reduced_b in [0,1,2] # we expect an inf loop when reduced_a is taken from group 1 and reduced_b is taken from group 0,1, or 2
    
    if group_reduced_a == 2:
        return group_reduced_b in [0,1,3] # we expect an inf loop when reduced_a is taken from group 2 and reduced_b is taken from any other group
    
    if group_reduced_a == 3:
        # barring a == b
        return group_reduced_b in [0,2,3] # we expect an inf loop when reduced_a is taken from group 3 and reduced_b is taken from group 0,2, or 3
    
    # unreachable
    raise

def group_of(a):
    return a % 4

def reduce(pair):
    
    a, b = pair
    a, b = min(a,b), max(a,b)
    
    while a % 2 == 0 and b % 2 == 0:
        a /= 2
        b /= 2
    
    return (a,b)

def power_of_2(x):
    if x == 0:
        return False
    
    return x & (x-1) == 0

explore(threes, "threes")