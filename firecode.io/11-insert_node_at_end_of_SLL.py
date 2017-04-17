class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self, new_head):
        self.head = new_head
    
    #method for inserting a new node at the end of a Linked List   
    def insertAtEnd(self, data):
        
        tail = Node()
        tail.data = data
        tail.next = None
        
        if self.head is None:
            self.head = tail
            return
        
        curr = self.head
        
        while curr.next:
            curr = curr.next
        
        curr.next = tail
