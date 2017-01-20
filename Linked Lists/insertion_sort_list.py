# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next= None):
        self.val = x
        self.next = next
    
    def __str__(self):
        return "{0} -> {1}".format(self.val, self.next)

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, head):
        
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        sorted_= head
        
        unprocessed= head.next
        
        sorted_.next= None
        
        while unprocessed:
            processing= unprocessed
            unprocessed= unprocessed.next
            processing.next= None
            
            sorted_= self.insert(processing, sorted_)
            
        
        return sorted_
    
    def insert(self, new_node, ll_head):
        
        prev_node= None
        current_node= ll_head
        
        while current_node and new_node.val > current_node.val:
            prev_node= current_node
            current_node= current_node.next
        
        if prev_node is None:
            
            # new_node.val <= current_node.val == ll_head.val
            
            new_node.next= ll_head #= current_node
            # ll_head= new_node # optional
            return new_node
        
        # prev_node.val < new_node.val <= current_node.val or
        # prev_node.val < new_node.val and current_node is None
        
        prev_node.next= new_node
        new_node.next=  current_node
        return ll_head
            
n3= ListNode(97)            
n2= ListNode(12, n3)            
n1= ListNode(14, n2)            
n0= ListNode(80, n1)

sol= Solution()
sol.insertionSortList(n0)