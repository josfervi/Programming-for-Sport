# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    
    # no need for a dummy ( se with_dummy_deleteDuplicates below )
    #
    # space  : in-place, constant extra space
    # time   : linear in len(A)
    # side fx: modifies A to be the result
    def deleteDuplicates(self, A):
        
        if A is None: return None # = A
        
        prev= A
        curr= A.next
        
        # {prev.val != curr.val)
        
        while curr:
            
            if prev.val == curr.val:
                unique= prev     # this op is the reason for keeping prev
                val=    prev.val # = curr.val
                
                # prev= curr
                curr= curr.next
                
                while curr and curr.val == val:
                    # rev= curr
                    curr= curr.next
                
                # { unique.val = val = prev.val != curr.val } or { curr is None }
                unique.next= curr
                if curr is None:
                    return A
                prev= curr
                curr= curr.next
                
            else:
                prev= curr
                curr= curr.next
        
        return A
        
    
    # no need for a dummy
    def with_dummy_deleteDuplicates(self, A):
        
        if A is None: return None # = A
        
        # dummy= ListNode(-1)
        # dummy.next= A
        
        prev= A
        curr= A.next
        
        # {prev.val != curr.val)
        
        while curr:
            
            if prev.val == curr.val:
                unique= prev     # this op is the reason for keeping prev
                val=    prev.val # = curr.val
                
                # prev= curr
                curr= curr.next
                
                while curr and curr.val == val:
                    # rev= curr
                    curr= curr.next
                
                # { unique.val = val = prev.val != curr.val } or { curr is None }
                unique.next= curr
                if curr is None:
                    # assert A == dummy.next # True
                    return A # dummy.next # = A
                prev= curr
                curr= curr.next
                
            else:
                prev= curr
                curr= curr.next
        
        # assert A == dummy.next # True
        return A # dummy.next # = A