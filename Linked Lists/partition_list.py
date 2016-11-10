# https://www.interviewbit.com/problems/partition-list/

class ListNode(object):
    def __init__(self, x, next= None):
        self.val = x
        self.next = next
    
    def __str__(self):
        return "%s->%s" % (self.val, self.next)

# in-place, constant extra memory
# linear time in len(A)
# modifies input A into the result
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        
        dummy= ListNode(0)
        dummy.next= A
        prev= dummy
        curr= A
        
        lt_ptr= dummy
        
        while curr:
            
            if curr.val < B:
                if lt_ptr.next == curr:
                    lt_ptr= curr # = lt_ptr.next
                    prev=   curr # = prev.next
                    curr=   curr.next
                else:
                    
                    tmp1=        lt_ptr.next
                    tmp2=        curr.next
                    lt_ptr.next= curr
                    curr.next=   tmp1
                    prev.next=   tmp2
                    
                    lt_ptr= lt_ptr.next
                    curr=   prev.next
            else:
                prev= curr
                curr= curr.next
        
        return dummy.next

# a5= ListNode(5)
# a4= ListNode(4, a5 )
# a3= ListNode(3, a4 )
# a2= ListNode(2, a3 )
# A=  ListNode(1, a2 )
# A= ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5) ) ) ) )

# 1->4->3->2->5->2
# A= ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2) ) ) ) ) )

# sol= Solution()
# res= sol.partition(A, 3)
# print "computed result:", res
# print "expected result: 1->2->2->4->3->5->None"