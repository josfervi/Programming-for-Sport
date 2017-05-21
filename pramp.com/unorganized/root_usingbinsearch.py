# DONE

def root(x, n):
  
  ep = 0.001
  
  x, n = float(x), float(n)
  
  lo, hi = 0.0, max(1.0 , x)
  
  # INVARIANT:
  # y cannot be < lo
  # y cannot be > hi
  # lo <= y <= hi
  while True:
    y_p = (lo+hi)/2.0
    
    # if x ? (y_p + ep)**n and? or? x ? (y_p - ep)**n:
    if hi - lo < ep: # < cleaner, less abstract end condition
      # y must be in the interval [lo, hi]
      # y_p is also within the interval [lo, hi]
      # since the interal's size is < ep
      # y and y_p cannot differ by more than ep
      # y and y_p cannot differ by ep either
      # y and y_p differ by less than ep
      return y_p
    
    x_p = y_p**n
    
    if x_p > x:
      hi = y_p
     
    else: # x_p < x
      lo = y_p
  
  return y_p

ep = 0.001
print 1.91293118277-ep < root(7, 3) < 1.91293118277+ep
print root(7,3)
print 3.0-ep < root(9, 2) < 3.0+ep
print root(9, 2)
   
'''
  ep = 0.001
  
  y = x^1/n
  y is the real value
  
  guess y'
  
  |y-y'| < ep
  
  two cases
  
  case 1
  y     - y' < e
  x^1/n - y' < e
  x^1/n      < y' + e
  x          ? (y' + e)^n
  
  case 2:
  y' - y      < ep
  y' - x^1/n  < ep
  y' - ep     < x^1/n
  (y' - ep)^n ? x
  x           ? (y' - ep)^n
  
  x ? (y'-ep)^n
  or? and?
  x ? (y'+ep)^n
  
  
  y'^n > x:
    guess a smaller y'
  
  how do i know that my y' guess is good enough?
  without actually knowing y?  
  
  y'^n < x:
    guess a bigger y'
'''