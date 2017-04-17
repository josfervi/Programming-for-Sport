arr[i] should be somewhere in i-k thru i+k inclusive

[3,1,5,2,4]

i v
0 3 should be in 0,1,2
1 1 should be in 0 1 2 3
2 5 should be in 0 1 2 3 4
3 2 should be in   1 2 3 4
4 4 should be in     2 3 4


[1,2,3,4,5]

[3,4,1,2] k=2
the min is initially k positions away from 0
in 0 through k

the min of lst = the min of lst[:k]

the second min of lst would start out k positions away from 1
so it can start out being anywhere in 0 thru k+1, but really it
should be in
cur_idx thru k+1 because the elements in lst[:cur_idx] are already where they should be

O(nk) is easy to acheive

but O(nlgk) is possible using a heap, REVIEW heap

min_up_to_here[i] =  min of lst[i:] < didn't pan out

# NEED TO STUDY HEAPS
# stuff below is stuff I don't understand fully

heap

min heap property: parent node is always less than or equal to its childre node

parent       i
children 2i+1 and 2i+2
[3,1,5,>2,>4] put into heap currindex to currindex+k using rule on ln 53

heapify
k swaps

using the heap, you can find the min of lst[curridx: curridx+k] in O(lgk) time