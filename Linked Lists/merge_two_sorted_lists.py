# https://www.interviewbit.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# space:   in-place, linear extra space in len(B)
# time:    linear in max(len(A), len(B))
# side fx: modifies A to be the result
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        
        if A is None: return B
        if B is None: return A
        
        dummy_a= ListNode(-1)
        dummy_a.next= A
        
        dummy_b= ListNode(-1)
        dummy_b.next= B
        
        prev_a= dummy_a
        a, b = A, B
        
        while a and b:
            if a.val > b.val:
                new= self.insert(prev_a, b.val) # insert a node containing b.val the prev_a and a and retrutn that node
                prev_a= new
                b= b.next
            else:
                prev_a= a
                a= a.next
        
        if b:
            # { a is None }
            # { prev_a points to the last non-null (non-None'd valued) node of A }
            prev_a.next= b # append the leftover of B to A
        
        # A is modified already, might as well make it the result
        A= dummy_a.next
        return dummy_a.next
    
    def insert(self, node, new_val):
        tmp= node.next
        new_node= ListNode(new_val)
        node.next= new_node
        new_node.next= tmp
        return new_node