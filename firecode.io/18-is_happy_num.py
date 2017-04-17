def is_happy_number(num):
    
    nums_seen = set()
    
    while True:
        
        if num == 1:
            return True
        
        if num in nums_seen:
            return False
        
        nums_seen.add(num)
        
        num = compute_next_num( num)


def compute_next_num( num):
    return sum([int(d)**2 for d in str(num)])


def compute_next_num1( num):
    
    num_str = str(num)
    
    next_num = 0
    while num != 0:
        leftmost_digit = num%10
        next_num += (leftmost_digit**2)
        num /= 10
    
    return next_num