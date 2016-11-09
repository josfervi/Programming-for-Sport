# https://www.interviewbit.com/problems/add-two-numbers-as-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    
    # in place, mutates A and B, 
    def addTwoNumbers(self, A, B):
        
        a= A
        b= B
        
        c_out= 0 # carry in
        while a and b:
            
            c_in= c_out # carry out of the previous iteration is the carry in of this iteration
            
            _=     (a.val + b.val + c_in)
            s=     _ % 10
            c_out= _ / 10
            
            a.val= s
            b.val= s
            
            a_prev= a
            a= a.next
            b= b.next
        
        # { one or both of a, b is None }
        
        if a is None and b is None:
            if c_out: a_prev.next= ListNode(c_out)
            return A
        
        # { only one of a, b is None }
        
        swapped= False
        if a is None:
            a, b = b, a
            swapped= True
        
        # { a is not None and b is None }
        
        while a:
            
            c_in= c_out
            
            _=     (a.val + c_in)
            s=     _ % 10
            c_out= _ / 10
            
            a.val= s
            
            a_prev= a
            a= a.next
        
        # { a is None }
        
        if c_out: a_prev.next= ListNode(c_out)
        return B if swapped else A