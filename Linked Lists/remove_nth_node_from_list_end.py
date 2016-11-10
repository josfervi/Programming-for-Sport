# https://www.interviewbit.com/problems/remove-nth-node-from-list-end/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        
        # get linked list length
        len_A= 0
        curr= A
        while curr:
            len_A+= 1
            curr= curr.next
        
        if B >  len_A: return A.next # does not modify A
        if B == 0    : B= 1 # from seeing expected output, caller expects same behavior for B=0 and B=1, namely to remove the last node
        
        pos= len_A - B # the 0-indexed position of the node to be removed, 0 indicating the first node, len_A-a indicating the last node
        
        # remove posth node
        if pos == 0: return A.next # does not modify A
        
        curr= A
        
        prev= curr
        curr= A.next
        pos-= 1
        while pos>0:
            prev= curr
            curr= curr.next
            pos-= 1
        
        prev.next= curr.next # modifies A
        
        return A