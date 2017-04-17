class SinglyLinkedList(object):
    # head is a Node
    def __init__(self, head):
        self.head= head
    
    def __str__(self):
        return "SLL: {0}".format(self.head)
    
    # WARNING - SIDE EFFECTS:
    # 
    # has side effects on any
    # SinglyLinkedList that shares nodes with self
    # 
    # has side effects on all
    # of self's nodes
    # (except when self is an empty SLL or a one-node SLL)
    def reverse(self):        
        head= None
        rem=  self.head
        
        while rem:
            tmp= rem.next
            rem.next= head
            head= rem
            rem= tmp
        
        self.head= head

class Node(object):
    
    def __init__(self, data, next= None):
        self.data= data
        self.next= next
    
    def __str__(self):
        return "N: {0} --> {1}".format(self.data, self.next)
        
n5= Node(5, None)
n4= Node(4, n5)
n3= Node(3, n4)
# n2= Node(2, n3)
# n1= Node(1, n2)
# n0= Node(0, n1)

sll3= SinglyLinkedList(n3)
sll4= SinglyLinkedList(n4)


# when running one side effects example,
# make sure to comment out the other one

# side effects example 1

print "before"
print "sll3: ", sll3
print "sll4: ", sll4

sll3.reverse()

print "after sll3.reverse()"
print "sll3: ", sll3
print "sll4: ", sll4
#---------------------------

# side effects example 2

# print "before"
# print "sll3: ", sll3
# print "sll4: ", sll4

# sll4.reverse()

# print "after sll4.reverse()"
# print "sll3: ", sll3
# print "sll4: ", sll4
#---------------------------