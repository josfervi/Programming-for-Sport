# Problem:
# Given a string, recursively compute a new string 
# where identical, adjacent characters 
# get separated with a "*".  


def insert_star_between_pairs(word):
  
  if word is None:
    return None
  
  if word == "":
      return ""
  
  word_list = list(word)
  prev_char = None
  for i, char in enumerate(word_list):
    
    if char == prev_char:
      
      word_list[i] = "*" + char
    
    prev_char = char
  
  return "".join(word_list)


# O(n) time
# O(n) extra space
def insert_star_between_pairs1(a_string):
    
    if a_string is None:
        return None
    
    if a_string == "":
        return ""
    
    res= a_string[0]
    
    for i in range(1, len(a_string)):
        if a_string[i-1] == a_string[i]:
            res+= '*'
        res+= a_string[i]
    
    return res

# O(n) time
# O(n) extra space
def insert_star_between_pairs2(a_string):
    
    if a_string is None:
        return None
    
    N= len(a_string)
    
    if N < 2:
        return a_string
    
    res= a_string[0]
    
    for i in range(1, N):
        
        if a_string[i-1] == a_string[i]:
            res+= '*'
        
        res+= a_string[i]
    
    return res