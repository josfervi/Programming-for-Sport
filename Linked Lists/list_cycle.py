# https://www.interviewbit.com/problems/list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    
    
    def detectCycle(self, A):
        
        nodes= set()
        
        a= A
        
        while a:
            if id(a) in nodes: return a
            else:              nodes.add(id(a))
            a= a.next
        
        return None