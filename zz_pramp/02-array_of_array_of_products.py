# The third question I've been asked on pramp
# https://www.pramp.com/question/7Lg1WA1nZqfoWgPbgM0M

# Given an array of integers arr, write a function that returns another array at the same length where the value at each index i is the product of all array values except arr[i].

# Solve without using division and analyze the runtime and space complexity

# Example: given the array [2, 7, 3, 4]
# your function would return: [84, 24, 56, 42] (by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3])

# O(n) time
# O(n) extra space for the result

# properties

# pre[i] = product(numbers[:i])
# pre[i] = pre[i-1] * numbers[i-1]

# post[i] = product(numbers[i+1:])
# post[i] = post[i+1] * numbers[i+1]

# res[i] = pre[i] * post[i]

def complementProducts( numbers ):
    
    N= len(numbers)
    
    result= [None]*N
    
    pre_product= 1
    
    # INVARIANT:
    #   at the beggining of each iteration
    #       { pre_product = product(numbers[:i]) }
    #   at the end of each iteration
    #       { pre_product = product(numbers[:i+1]) }
    for i in range(N):
        result[i]= pre_product
        pre_product*= numbers[i]

    post_product= 1
    
    # INVARIANT:
    #   at the beggining of each iteration
    #       { post_product = product(numbers[i+1:]) }
    #   at the end of each iteration
    #       { post_product = product(numbers[i:] }
    for i in reversed(range(N)):
        result[i]*= post_product
        post_product*= numbers[i]
    
    return result

def complementProducts_using_pre_and_post( numbers ):

  N= len(numbers)
  
  if N == 0:
      return []
  
  pre=  [None]*N
  post= [None]*N
  
  pre[0]= 1
  
  for idx in range(1, N):
      pre[idx]= pre[idx-1] * numbers[idx-1]
  
  post[N-1]= 1
  
  for idx in reversed(range(N-1)):
      post[idx]= post[idx+1] * numbers[idx+1]
  
  res= [None]*N
  
  for idx in range(N):
      res[idx]= pre[idx] * post[idx]
  
  return res

# the probably correct brute force solution
# used for testing the optimized solution
# e.g. this is the functional unit known to be correct
def complementProducts_bruteforce(numbers):
    
    N= len(numbers)
    
    result= [1]*N
    
    for i in range(N):
        for j in range(N):
            if j == i:
                continue
            result[i]*= numbers[j]
    
    return result

print complementProducts([1,2,3,4]) == [2*3*4, 1*3*4, 1*2*4, 1*2*3]
print complementProducts([1,2,3,4]) == complementProducts_bruteforce([1,2,3,4])
print complementProducts([1,2,3,4,5,6,7,8]) == complementProducts_bruteforce([1,2,3,4,5,6,7,8])
print complementProducts([8,2,0,1,9]) == complementProducts_bruteforce([8,2,0,1,9])
print complementProducts([3,6,2,0,2,1,66,3,9]) == complementProducts_bruteforce([3,6,2,0,2,1,66,3,9])