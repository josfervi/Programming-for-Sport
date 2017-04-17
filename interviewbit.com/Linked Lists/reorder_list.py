# https://www.interviewbit.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next= None):
        self.val = x
        self.next = next
    
    def __str__(self):
        return "%s --> %s" % (self.val, self.next)

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        
        # general strategy
        #  split A in the middle into left and right
        #  reverse right
        #  interleave left and right_rev
        
        # special care must be given to whether A is even-lengthed or odd-lengthed
        #  in the case of even-lengthed A,
        #    the middle doesn't fall on a node, but between nodes and len(left) = len(right)
        #  in the case of odd_lengthed A,
        #    the middle falls on a node; turns out we can let this node be in left; in this case:
        #    len(left) = len(right) + 1
        
        a= A
        len_A= 0
        while a:
            len_A+= 1
            a= a.next
        
        if len_A <= 2: return A # note: when len_A = 0, A = None
        
        # { len_A >= 3 }
        
        m= len_A >> 1 # m denotes the 0-indexed position of the last node of left
        
        a= A
        while m>0:
            a= a.next
            m-= 1
        
        left_end=      a
        right_beg=     left_end.next
        left_end.next= None
        
        right_rev= self.reverseList(right_beg)
        
        # interleave left and right_rev
        
        left= A
        
        # note: { len(left) = len(right_rev)     if len(A) is even }
        #       {           = len(right_rev) + 1 if len(A) is odd  }
        while right_rev:
            left_tmp=       left.next
            left.next=      right_rev
            right_rev_tmp=  right_rev.next
            left=           left_tmp
            right_rev.next= left
            right_rev=      right_rev_tmp
        
        return A
    
    # from
    # https://www.interviewbit.com/problems/reverse-linked-list/
    
    # reverse a singly linked list in place, w/ constant extra memory, in one pass
    
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    # - O(n) where n = len(A) = num of nodes in Singly Linked List A
    # - O(1) extra space
    
    # after the function A points to the last element of the reversed list
    # the function res points to the first element of the the reversed list
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


# a5= ListNode(5)
# a4= ListNode(4, a5 )
# a3= ListNode(3, a4 )
# a2= ListNode(2, a3 )
# A=  ListNode(1, a2 )
# A= ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5) ) ) ) )

# sol= Solution()
# res= sol.reorderList(A)