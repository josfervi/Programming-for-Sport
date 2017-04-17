chars= [x,y,z]

last_time_seen = [0, 2, 3]

# my solution can't handle duplicates in chars
# my solution is O(n*m) but there may be a way to decrease that:
#    i'd have to find a more efficient way to find the min of last_seen,
#    which has size m, in less then O(m) time
#
#    I have a way of finding min(last_seen) in O(1),
#    it uses a hashmap and a doubly linked list and I have written about
#    it in my paper notes
#      this will reduce the overall runtime complexity to O(n+m)

str= 'xyyzyzyx'
      |  |<--------candidate soln
      
           | |<----best soln


                 last_seen

    running      when was
    counts       the last
    for          time i 
                 saw
i    x y z       x  y  z   current     best
                           soln        solution
                                       so far
0 x  1        n [0  -  -]  -            -
1 y    1      n [0  1  -]  -            -
2 y    2      n [0  2  -]  -            -
3 z      1    4 [0, 2, 3]  [0,3]        [0,3]
4 y    3      5 [0, 4, 3]  [0,4]        [0,3]     
5 z      2    6 [0  4  5]  [0,5]        [0,3]
6 y    4      7 [0  6  5]  [0,6]        [0,3]
7 x  2        3 [7  6  5]  [5,7]        [5,7]
                            ^ ^
                            | |
                            | current_idx
                            |
                            min(last_seen)

n= size str
O(n*m) time #*m to find min(last_seen) in each iteration

but maybe I can exploit the fact that last_seen only changes at one position in each iteration
maybe i can use a heap to find min(last_seen) in O(lgm)
              

m= size chars
O(m) space