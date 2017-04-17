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
    def simplifyPath(self, A):
        
        A= A.strip('/').split('/')
        A= self.removeElement(A, "")
        
        # "/a/.///b/../../c/"
        #                     -[strip]->
        # "a/./b/../../c"
        #                 -[split]->
        # ["a", ".", "", "", "b", "..", "..", "c"]
        #                                          -[removeElement]->
        # ["a", ".", "b", "..", "..", "c"]
        
        stack= Stack()
        
        for a in A:
            
            if   a == ".":
                continue
            elif a == "..":
                if not stack.isEmpty():
                    stack.pop()
            else:
                stack.push(a)
        
        res= ""
        while not stack.isEmpty():
            res= "/" + stack.pop() + res # reverse order
            # res++ "\" + stack.dequeue()
        
        # return '/' + '/'.join( list(stack) )
        # e.g.
        # return '/' + '/'.join( stack.items ) # would work wonderfully <- alliteration
        
        return res if res != "" else "/"
    
    # from TWO POINTERS >> remove_element_from_array
    # passes EFICIENCY!!!
    def removeElement(self, A, B):
        
        j= 0
        
        for i,a in enumerate(A):
            if a != B:
                A[j]= A[i] # key fix
                j+= 1
        
        A= A[:j]
        # return len(A) # modified from original
        return A
    
    # fails EFFICIENCY
    def removeElement_1(self, A, B):
        i= 0
        while i < len(A):
            
            if A[i] == B:
                A[i:]= A[i+1:] # key failure
            
            else: i+= 1
        
        return len(A)
    
    # fails EFFICIENCY
    def removeElement_2(self, A, B):
        done= False
        while not done:
            try:
                A.remove(B)
            except ValueError:
                done= True
        
        return len(A)