# https://www.interviewbit.com/problems/swap-list-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# in place, linear time, constant extra time
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        
        # for each pair, a,a.next, starting on an even 'indexed' node b
        #
        # _ --> a --> b --> c
        # becomes
        # _ --> b --> a --> c
        
        a= A
        if a is None: return A
        else:         b= a.next
        if b is None: return A
        else:         c= b.next
        
        A= b
        b.next= a
        a.next= c
        
        _= a
        a= c
        if a is None: return A
        else:         b= a.next
        while a is not None and b is not None:
            c= b.next
            
            _.next= b
            b.next= a
            a.next= c
            
            _= a
            a= c
            if a is None: return A
            else:         b= a.next
        
        return A