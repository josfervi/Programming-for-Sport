class ListNode(object):
    def __init__(self, x, next= None):
        self.val = x
        self.next = next
    
    def __str__(self):
        return "%s --> %s" % (self.val, self.next)

# a3= ListNode(3)
# a2= ListNode(2, a3 )
# A=  ListNode(1,  a2)
# A= ListNode(1, ListNode(2, ListNode(3) ) )