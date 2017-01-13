# https://www.pramp.com/question/L3wQBnQYAEh5K97W9ONK

#Given a package with a weight limit and an array arr of item weights, how can you most efficiently find two items with sum of weights that equals the weight limit?

# Your function should return 2 such indices of item weights or -1 if such pair doesn't exist.
# What is the runtime and space complexity of your solution?



def two_sum( numbers, target_sum ):
   
   idx_of= {}
   
   for idx, number in enumerate(numbers):
      
      complement= target_sum - number
      if complement in idx_of:
         return [ idx_of[complement], idx ]
      
      idx_of[number]= idx
   
   return -1

def two_sum_brute_force( numbers, target_sum ):
    
    N= len(numbers)
    
    for i in range(N-1):
        for j in range(1+1, N):
            if numbers[i] + numbers[j] == target_sum:
                return [i, j]
    
    return -1


# ---------- RANDOM TESTS ----------

from random import randint, shuffle

def test_two_sum_once():
    
    start=  randint(0, 10)
    length= randint(5,15)
    step=   randint(1,8)
    stop=   start + length * step
    
    numbers= range(start, stop, step)
    
    shuffle(numbers)
    
    target_sum= numbers[0] + numbers[-1]
    
    shuffle(numbers)
    
    result= two_sum( numbers, target_sum )
    if result != -1:
        i, j= result
        print numbers[i] + numbers[j] == target_sum
    else:
        print two_sum_brute_force( numbers, target_sum ) == -1

number_of_test_cases= 100

for _ in range(number_of_test_cases):
    test_two_sum_once()

# passed all 100 test cases