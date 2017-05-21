# DONE

# O(n) time
# O(n) space -> can be O(1) space
def decrypt(word):
  
  NUM_LETTERS = 26
  
  cyber_text = map(ord, word)
  
  n = len(cyber_text)
  
  text = [None]*n
  
  sum_ = 0
  for i in range(n):
    text[i] = cyber_text[i] - ( 1 + sum_ )
    
    # O(1)
    text[i] -= ord('a')
    text[i] %= NUM_LETTERS
    text[i] += ord('a')
    
    # O(?)
    # while text[i] < ord('a'):
    #   text[i] += NUM_LETTERS
    
    sum_ += text[i]
  
  text = map(chr, text)
  return ''.join(text)


print(decrypt('dnotq'))
'''
Encryption steps

s1   a     b       c         d 

s2 1+a 1+a+b 1+a+b+c 1+a+b+c+d

s3  a'    b'      c'        d'


1+a - k*26 = a'
a = a'-1 + k*26 (k == 0 or 1)

 a   a'
'a'  'b'
'b'  'c'
'c'  'd'
'd'  'e'
 .    .
 .    .
 .    .
'z'  'y'


1+a+b -k*26 = b'
b = b'-(1+a) + k*26


1+a+b+c - k*26 = c'
c = c'-(1+a+b) + k*26


1+a+b+c+d - k*26 = d'
d = d'-(1+a+b+c) + k*26


t[i] = t'[i]-(1+sum(t[:i])) + k*26

t[0] = t'[0]-(1+sum(t[:0])) + k*26
 a   =  a'  -(1           ) + k*26
'''