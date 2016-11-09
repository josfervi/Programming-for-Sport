# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    
    # in place, constant extra space
    # linear time in len(A)
    def deleteDuplicates(self, A):
        
        dummy= ListNode(0)
        dummy.next= A
        a= dummy
        while a:
            
            if a.next and a.next.next and a.next.val == a.next.next.val:
                
                d= a.next # a remains pointing to the node before the duplicates
                
                while d.next.next and d.next.val == d.next.next.val:
                    d= d.next
                
                # { duplicates run from a.next to d.next }
                
                if d.next.next: a.next= d.next.next
                else:
                    a.next= None
                    return dummy.next
            
            else:
                a= a.next
        
        return dummy.next