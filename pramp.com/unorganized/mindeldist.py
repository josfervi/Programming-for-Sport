'''
   v
thing
something
       ^

  _ h i t----str1
_ 0 1 2 3--0
h 1 0 1 2--1
e 2 1 2 3--2
a 3 2 3 4--3
t 4 3 4 3--4
| | | | |
| 0 1 2 3
|
s
t
r
2

if c1 == c2:
  min(1+up, 1+left, diag) 
else:
  min(1+up, 1+left, diag+2)

  v
dog
frog
   ^
'''

# O(nm) time
# O(nm) space -> can be O(min(n,m)) space
def deletionDistance(str1, str2):
  
  n, m = len(str1), len(str2)
  
  table = [ [0]*(m+1) for _ in range(n+1) ]
  
  for r in range(n+1):
    if r > 0:
      c1 = str1[r-1]
    for c in range(m+1):
      if r == 0:
        table[r][c] = c
        continue
      elif c == 0:
        table[r][c] = r
        continue
      # r > 0
      # c > 0
      c2 = str2[c-1]
      up   = table[r-1][c]
      left = table[r][c-1]
      diag = table[r-1][c-1]
      table[r][c] = min( up+1, left+1, diag+(0 if c1==c2 else 2) )
  return table[n][m]

print deletionDistance('heat', 'hit') == 3
print deletionDistance('dog', 'frog') == 3
print deletionDistance('some', 'some') == 0
print deletionDistance('release', 'real') == 5
print deletionDistance('something', 'thing') == 4