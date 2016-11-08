# https://www.interviewbit.com/problems/palindrome-list/

# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, x, next= None):
#         self.val = x
#         self.next = next
    
#     def __str__(self):
#         return "%s --> %s" % (self.val, self.next)

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        
        h= A
        
        n= 0
        while h is not None:
            h= h.next
            n+= 1
        
        if n == 0: return 1
        if n == 1: return 1
        
        mid= l= n/2 # r= mid+1+(n%2) # = mid+1 if n%2==0 else mid+2
        
        left= A
        while l>1:
            left= left.next
            l-= 1
        right= left.next if n%2==0 else left.next.next # right=head; while r>1: right=right.next; r-=1
        
        # e.g.
        #      left       right
        #       |           |
        #       v           v
        # 1 --> 2 --> 3 --> 2 --> 1 --> None
        
        left.next= None
        left= A
        
        # e.g.
        # left                right
        #  |                    |
        #  v                    v
        #  1 --> 2 --> None     2 --> 1 --> None
        
        # palindrome if reverse(left) equals right
        
        # left_rev= self.reverseList( left )
        h= left
        
        rem= h.next
        h.next= None
        
        while rem is not None:
            tmp= rem.next
            rem.next= h
            h= rem
            rem= tmp
        
        left_rev= h
        # left_rev= self.reverseList( left )
        
        
        # e.g.
        #           left_rev  right
        #                |     |
        #                v     v
        # None <-- 1 <-- 2     3 --> 4 --> None
        
        # return self.equals(left_rev, right)
        a, b = left_rev, right
        while a is not None:
            if a.val != b.val:
                return 0
            a= a.next
            b= b.next
                
        # { a is None } and
        # { n_a := num of nodes of a ; the frist n_a nodes of b match the nodes of a }
        # b equals a if b also has n_a nodes
        return 1 if (b is None) else 0
    
    # @param A : head node of linked list
    # @return the head node in the linked list
    # - O(n) where n = len(A) = num of nodes in Singly Linked List A
    # - O(1) extra space
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

# sol= Solution()
# a5= ListNode(1)
# a4= ListNode(2, a5)
# a3= ListNode(3, a4)
# a2= ListNode(2, a3)
# a1= ListNode(1, a2)
# print sol.lPalin(a1)