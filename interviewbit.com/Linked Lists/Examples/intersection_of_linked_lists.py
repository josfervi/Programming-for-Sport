# https://www.interviewbit.com/problems/intersection-of-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x, next= None):
#         self.val = x
#         self.next = next
    
#     def __str__(self):
#         return "%s --> %s" % (self.val, self.next)

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        
        if A is None or B is None: return None
        
        m, n = 0, 0 # len(A) and len(B) respectively
        a, b = A, B
        while a is not None:
            m+= 1
            a= a.next
        while b is not None:
            n+= 1
            b= b.next
        
        swap= False
        if m < n:
            A, B = B, A
            m, n = n, m
            swap= True
        
        # { m      > n      }
        # { len(A) > len(B) }
        
        d= m - n
        a, b = A, B
        while d > 0:
            d-= 1
            a= a.next
        
        while a is not None:
            if a == b:
                if swap: A, B = B, A
                return a
            a= a.next
            b= b.next
        
        if swap: A, B = B, A
        return None

# c1= ListNode(4)
# a2= ListNode(2, c1)
# a1= ListNode(1, a2)
# b1= ListNode(3, c1)

# sol= Solution()
# print "A: ", a1
# print "B: ", b1
# print sol.getIntersectionNode(a1, b1)