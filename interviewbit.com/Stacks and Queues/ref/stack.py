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