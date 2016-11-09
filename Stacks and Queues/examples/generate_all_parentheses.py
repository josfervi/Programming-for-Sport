# https://www.interviewbit.com/problems/generate-all-parentheses/

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
    # @return an integer
    def isValid(self, A):
        
        stack= Stack()
        
        # iterate through A
        # push opening symbols into stack as they are encountered
        # when a closing symbol is encountered, this closing symbol
        #  must close the opening symbol at the top of the stack
        
        for a in A:
            if a == '(' or a == '[' or a == '{':
                stack.push(a) # push opening symbol into stack
            
            # a is a closing symbol
            
            elif not stack.isEmpty():
                opener= stack.pop()
                if opener == '(' and a != ')' or \
                   opener == '[' and a != ']' or \
                   opener == '{' and a != '}':
                       return 0
            else: # stack is empty
                return 0
        
        return 1 if stack.isEmpty() else 0