# O(1) time
# O(1) extra space
def is_power_of_four(num):
    # num is a power of four if its binary representation
    # (1) has exactly one set bit, AND
    # (2) the single set bit occurs at an even position
    #
    # e.g.
    #
    #  powers of four in binary
    # position: 8 7 6 5 4 3 2 1 0
    # ---------------------------
    #                           1
    #                       1 0 0
    #                   1 0 0 0 0
    #               1 0 0 0 0 0 0
    #           1 0 0 0 0 0 0 0 0
    
    if num == 0:
        return False
    
    # determine if num has exactly one set bit or not
    # and return false if not
    if not has_excatly_one_set_bit(num):
        return False
    
    # { num has exactly one set bit }
    
    # determine if the single set bit occurs at an even position or not
    # and return false if not
    if any_set_bits_occur_at_an_odd_position(num):
        return False
    
    # { num has exactly one set bit } and { the single set bit occurs at an even position }
    
    return True
    
def has_excatly_one_set_bit( num ):    
    if num == 0:
        return False
    
    # num & (num-1) zeros out the first (least significant) bit of num
    return num & (num-1) == 0

# +num+:: +at most a 32-bit number+
def any_set_bits_occur_at_an_odd_position( num ):
    return not all_set_bits_occur_at_even_positions(num)
    
# +num+:: +at most a 32-bit number+
def all_set_bits_occur_at_even_positions( num ):
    # num & 0b0101010101010101 zeros out all odd position bits of num
    return (num & 0b0101010101010101) == num