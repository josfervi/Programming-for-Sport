# This is a copy of Math/excel_column_title.py

# START REWORKED SOLUTION AFTER MY INTERVIEWING.IO session with LOGARITHMIC THUNDER

NL = NUM_LETTERS = 26

def base_conversion(num, new_base):
    """
    Converts num from represenation that uses
      10 symbols to represent the quantities 0-9
      to a new base that uses new_base number of
      symbols to represent the quantities 1-new_base.
    """
    
    if num == 0:
        raise ValueError("No way to represent 0 in new base.")
    
    digits = []
    
    while num:
        # least significant digit
        lsd = num % new_base
        num /= new_base
        if lsd == 0:
            # We don't have a symbol for 0
            # but we have a symbol for new_base
            # so let's make a contribution of
            # new_base.
            digits.append(new_base)
            num -= 1 # borrow a 1 from the neighbor
        else:
            digits.append(lsd)
    
    return reversed(digits)

def num_to_col(num):
    
    digits = base_conversion(num, new_base=NUM_LETTERS)
    letters = map(num_to_char, digits)
    return ''.join(letters)


def num_to_char(num):
    assert 1 <= num <= NL
    return chr(ord('A')-1 + num)

def test_num_to_col():
    for i in range(1, NL):
        print num_to_col(i)
    
    for i in range(NL, NL*NL):
        print num_to_col(i)

# test_num_to_col()

# The best way to think about that I've come up with
# is that the letters A-Z represent the numbers 1-26.
# There is no symbol for 0, so to convert from a base-26 
# representation to a column name is that whereever there 
# is a zero in the base-26 representation,
# that zero must borrow from its neighbor.

# Examples

# base-26 repr => intermediate repr => ... => column name

# 10 => A0 => Z
print num_to_col(1*26)

# 100 => A00 => _Z0 => _YZ
print num_to_col(1*26**2)

# 1000 => A000 => _Z00 => _YZ0 => _YYZ
print num_to_col(1*26**3)

# 20 => B0 => AZ
print num_to_col(2*26)

# 201 => B0A => AZA
print num_to_col(2*26**2 + 1)

# 100130
# ||||||
# vvvvvv
# A00AC0
# \|||\|
#  vvv v
# _Z0ABZ
#  \||||
#   vvvv
# _YZABZ
print num_to_col(1*26**5 + 1*26**2 + 3*26)

# Rather than getting the base-26 repr and then converting
# it to a column name, we can tweak the base-10 to base-26
# converstion to get the column name directly.

# END REWORKED SOLUTION AFTER MY INTERVIEWING.IO session with LOGARITHMIC THUNDER



class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        
        str_acc= ""
        
        while A > 0:
            int_a= A % 26
            if int_a == 0:
                chr_a= 'Z'
                A= A/26 - 1
            else:
                chr_a= chr( int_a + 64 )
                A= A/26
            str_acc= chr_a + str_acc # does not equal acc + chr( ) because string concatenation is not commutative

        return str_acc