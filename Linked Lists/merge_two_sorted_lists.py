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
    
    # much better solution from
    # http://stackoverflow.com/questions/22507197/merging-two-sorted-linked-lists-into-one-linked-list-in-python
    def mergeTwoLists(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        
        # create dummy node to avoid additional checks in loop
        s = t = ListNode(None) 
        while head1 and head2:
            if head1.val < head2.val:
                # remember current low-node
                c = head1
                # follow ->next
                head1 = head1.next
            else:
                # remember current low-node
                c = head2
                # follow ->next
                head2 = head2.next
            
            # only mutate the node AFTER we have followed ->next
            t.next = c          
            # and make sure we also advance the temp
            t = t.next
        
        t.next = head1 or head2
        
        # return tail of dummy node
        return s.next
    
    def mergeTwoLists_hardtoread(self, A, B):
        
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
            prev_a.next = b # append the leftover of B to A
        
        # A is modified already, might as well make it the result
        A = dummy_a.next
        return dummy_a.next
    
    def insert(self, node, new_val):
        tmp= node.next
        new_node= ListNode(new_val)
        node.next= new_node
        new_node.next= tmp
        return new_node