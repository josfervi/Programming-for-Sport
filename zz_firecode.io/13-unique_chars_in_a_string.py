def unique_chars_in_string(input_string):
    
    return len(set(input_string)) == len(input_string)
    
def unique_chars_in_string1(input_string):
    
    chars_seen = set()
    
    for char in input_string:
        if char in chars_seen:
            return False
        
        chars_seen.add(char)
    
    return True