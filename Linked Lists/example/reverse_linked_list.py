# https://www.interviewbit.com/problems/reverse-linked-list/

# reverse a singly linked list in place, w/ constant extra memory, in one pass

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# - O(n) where n = len(A) = num of nodes in Singly Linked List A
# - O(1) extra space
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        
        head= A
        
        # h
        # |
        # v
        # 1 --> 2 --> 3 --> 4 --> None
        
        rem= head.next
        head.next= None
        
        #          h     r
        #          |     |
        #          v     v
        # None <-- 1     2 --> 3 --> 4 --> None
        
        while rem is not None:
            tmp= rem.next
            rem.next= head
            head= rem
            rem= tmp
        
        return head