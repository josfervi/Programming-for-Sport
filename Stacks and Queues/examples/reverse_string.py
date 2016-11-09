# https://www.interviewbit.com/problems/reverse-string/

class Stack(object):
    ''' Implementation detail: the back of the list is the top of the stack for efficiency considerations '''
    
    def __init__(self):
        self.items= []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        
        stack= Stack()
        
        for a in A:
            stack.push(a)
        
        A= "" # does not modify A
        while not stack.isEmpty():
            A+= stack.pop()
        
        return A