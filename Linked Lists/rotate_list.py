# https://www.interviewbit.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, head, k):
        
        if k == 0:
            return head
        
        prev_node= None
        node= head
        length= 0
        while node:
            prev_node= node
            node= node.next
            length+= 1
        
        k%= length
        
        if k == 0:
            return head
        
        last_node= prev_node
        
        # move the length-1 - k - 1 node
        
        node= head
        i= 0
        while i < length - k - 1:
            node= node.next
            i+= 1
        
        new_head= node.next
        node.next= None
        last_node.next= head
        
        return new_head