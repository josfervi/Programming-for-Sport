# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    
    
    # in-place, constant extra space
    # linear time in len(A)
    
    # PRECONDITION: 1 ≤ m ≤ n ≤ length of list
    def reverseBetween(self, A, m, n):
        
        if A is None: return None #= A
        if m == n:    return A
        
        # { A is not None } and { m != n }
        
        a= A
        len_A= 0
        while a:
            len_A+= 1
            a= a.next
        
        # { A is not None } => { len_A >= 1 }
        
        if len_A == 1: return A
        if len_A == 2:
            # { m = 1 } and { n = 2 } since { m != n } and PRECONDITION
            return self.reverseList(A)
        if m == 1 and n == len_A: # <- this if condition actually covers the if condition of the if on ln 30 too!!!
            return self.reverseList(A)
        
        # { len_A >= 3 } 
        
        dummy= ListNode(0)
        dummy.next= A
        bef_rev= dummy # bef_rev starts out being a dummy node, necessary for m=1
        a= A
        while a and m>1:
            m-= 1
            n-= 1
            bef_rev= a # = bef_rev.next
            a= a.next
        
        bef_rev.next= None
        rev_strt= a
        
        while a and n>1:
            n-= 1
            a= a.next
        
        # { a is not None } since { n <= len_A }
        
        rev_end= a
        aft_rev= rev_end.next # is None if n = len_A
        rev_end.next= None
        
        #             A                 bef_rev              rev_strt           rev_end                aft_rev
        #             |                    |                    |                  |                      |
        #             v                    v                    v                  v                      v
        # dummy -> 1th_node -> ... -> m-1th_node -> None  |  mth_node -> ... -> nth_node -> None  |  nth+1_node -> ... -> len_Ath_node -> None
        
        rev= self.reverseList(rev_strt)
        rev_strt, rev_end = rev_end, rev_strt
        
        #                                                                                rev
        #             A                 bef_rev                     rev_end            rev_strt       aft_rev
        #             |                    |                           |                  |              |
        #             v                    v                           v                  v              v
        # dummy -> 1th_node -> ... -> m-1th_node -> None |  None <- mth_node <= ... <- nth_node  |  nth+1_node -> ... -> len_Ath_node -> None
        
        bef_rev.next= rev # = rev_strt
        rev_end.next= aft_rev
        
        return dummy.next


    # modified from:
    
    # https://www.interviewbit.com/problems/reverse-linked-list/

    # reverse a singly linked list in place, w/ constant extra memory, in one pass

    # - O(n) where n = len(A) = num of nodes in Singly Linked List A
    # - O(1) extra space

    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        
        head= A
        
        # h
        # |
        # v
        # 1 --> 2 --> 3 --> 4 --> None
        
        rem= head.next  if head else None
        if head: head.next= None
        
        #          h     r
        #          |     |
        #          v     v
        # None <-- 1     2 --> 3 --> 4 --> None
        
        while rem:
            tmp= rem.next
            rem.next= head
            head= rem
            rem= tmp
        
        return head