# https://www.pramp.com/question/gKQ5zA52mySBOA5GALj9

# Given an array of numbers arr and a number S, find 4 different numbers in arr that sum up to S.

# Write a function that gets arr and S and returns an array with 4 indices of such numbers in arr, or null if no such combination exists.
# Explain and code the most efficient solution possible, and analyze its runtime and space complexity.

def quad_comb( numbers, target_quad_sum ):
    
    N= len(numbers)
    
    if N < 4:
        return None
    
    pair_sums= {}
    for i in range(N-1):
        for j in range(i+1, N):
            pair_sum= numbers[i] + numbers[j]
            
            if not pair_sum in pair_sums:
                pair_sums[pair_sum]= []
            pair_sums[pair_sum].append( (i,j) )
    
    for pair_sum in pair_sums:
        target_pair_sum= target_quad_sum - pair_sum
        if target_pair_sum in pair_sums:
            pair_indeces= pair_sums[pair_sum]
            target_pair_indeces= pair_sums[target_pair_sum]
            
            candidate_result= find_two_unique_pairs( pair_indeces, target_pair_indeces )
            if candidate_result:
                return candidate_result
    
    return None

'''
    Given two lists of pairs,
    find four unique numbers,
    two of those numbers being a pair in one list
    and the other two numbers being a pair in the other list
'''
def find_two_unique_pairs( pairs, other_pairs ):
    
    for pair in pairs:
        for other_pair in other_pairs:
            
            i,j= pair
            k,l= other_pair
            
            if i != k and i != l and j != k and j != l:
                return [i,j,k,l]
    
    return None

def quad_comb_brute_force( numbers, target_quad_sum ):
    
    N= len(numbers)
    
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                for l in range(k+1,N):
                    if numbers[i] + numbers[j] + numbers[k] + numbers[l] == target_quad_sum:
                        return [i,j,k,l]
    
    return None



# ---------- RANDOM TESTS ----------

from random import randint, shuffle

def test_quad_comb_once():
    
    start= randint(0,30)
    step=  randint(1,8)
    length= randint(10,15)
    stop=  start +  length * step
    
    nums= range(start, stop, step)
    shuffle(nums)
    
    targ_sum= nums[0] + nums[1] + nums[5] + nums[-1]
    
    shuffle(nums)
    
    print "nums: ", nums
    print "targ_sum: ", targ_sum
    print "---------------------"
    result= quad_comb(nums,targ_sum)
    print "computed: ", result
    if result:
        res_sum= 0
        for idx in result:
            res_sum+= nums[idx]
        print "correct: ", (res_sum == targ_sum)
    else:
        print "correct: ", (quad_comb_brute_force(nums,targ_sum) is None)
    print
    print

number_of_test_cases= 100
for i in range(number_of_test_cases):
    test_quad_comb_once()

# passed all 100 random tests