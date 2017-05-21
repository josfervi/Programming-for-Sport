# problem extension:
#  try to do it in-place

# in-place
def flattenDictionary_in_place(inp_dict):
  
  for key, value in inp_dict.items():
    if isinstance(value, dict):
      nested_dict = value
      
      flattenDictionary_in_place(nested_dict)
      
      old_key = key
      for nested_key, nested_value in nested_dict.items():
        # nested_dict is flattened
        new_key = old_key + '.' + nested_key
        
        inp_dict[new_key] = nested_value
      
      # inp_dict[old_key] # points to the flattened nested dict
      del inp_dict[old_key] # does not delet the flattened nested dict
  
  outp_dict = inp_dict
  return outp_dict


# not in-place
def flattenDictionary_not_in_place(inp_dict):
  
  outp_dict = {}
  
  for key, value in inp_dict.items():
    if isinstance(value, dict):
      nested_dict = value
      
      for nested_key, nested_value in flattenDictionary_not_in_place(nested_dict).items():
        # nested_dict is flattened
        old_key = key
        new_key = old_key + '.' + nested_key
        
        outp_dict[new_key] = nested_value
    else:
      outp_dict[key] = value
  
  return outp_dict


dict3 = {'a':1, 'b':2, 'c':3}
print flattenDictionary_not_in_place(dict3)
print flattenDictionary_in_place(dict3), '# in-place'
print

dict2 = {'d':3, 'e':dict3}
print flattenDictionary_not_in_place(dict2)
print flattenDictionary_in_place(dict2), '# in-place'
print

dict1 = {'g':dict2}
print flattenDictionary_not_in_place(dict1)
print flattenDictionary_in_place(dict1), '# in=place'


'''
different dictionaries

dict1
  key1 : 1
  key2 : dict2

dict2
  a : 2
  b : 3
  c : dict3

dict3
  d : 3
  e : 1


intermidiate_res
dict2
  a : 2
  b : 3
  c.d : 3
  c.e : 1

    
res
  key1 : 1
  key2.a : 2
  key2.b : 3
  key2.c.d : 3
  key2.c.e : 1
'''