# letters= "a c d e g i l m n o p r s t u w".split()
# len(letters) = 16

# consider string s as a base-37 number
# but instead of using the symbols
#  
#  0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j . . .
# 
# it uses the symbols
# 
#  a c d e g i l m n o p r s t u w _ _ _ _ . . .
# 
# note that only the first 16 symbols are defined

# s[0] is the leftmost (i.e. most significant) symbol
# s[1] is second most significant symbol
# ...
# s[s.length-1] is the least significant (i.e. right most) symbol

# int64 hash(String s)
#  converts
#   the base-37 number that uses the symbols
#   a c d e g i l m n o p r s t u w
# 
#  into
#   the base-10 (decimal) number that uses the symbols
#   0 1 2 3 4 5 6 7 8 9

# I've rewritten hash in Python:

def hash(string):
    h= 7
    letters= "acdegilmnoprstuw"
    for char in string:
        h= (h*37 + letters.index(char))
    
    return h

# to undo hash,
#  simply convert the base-10 number back into
#  the base-37 number

letters= "a c d e g i l m n o p r s t u w".split()

def unhash(num):
    
    base_37_string= ""
    
    while num != 0:
        
        symbol_as_num= num % 37
        symbol_as_let= letters[symbol_as_num]
        
        base_37_string= symbol_as_let + base_37_string
        
        num/= 37
    
    return base_37_string[1:] # base_37_string[0] corresponds to 7:'m' in hash line 31, ignore this


# tests

# directed tests

print(   hash("leepadg"   ) == 680131659347)
print( unhash(680131659347) == "leepadg"   )

mystery_number= 930846109532517
print( unhash(mystery_number) == "lawnmower"   )
print(   hash("lawnmower"   ) == mystery_number)


# random tests

from random import randint

def test_hash_and_unhash_once():
    # create a random string, s,
    # which has only characters from letters
    # and then verify that
    # unhash(hash(s)) == s
    
    letters= "a c d e g i l m n o p r s t u w".split()
    n= len(letters)
    
    length= randint(5,10)
    s= ""
    for i in range(length):
        s+= letters[ randint(0,n-1) ]
    
    result= unhash(hash(s)) == s
    
    print "{0} for s = \"{1}\"".format(result, s)

number_of_tests= 250
for i in range(number_of_tests):
    test_hash_and_unhash_once()