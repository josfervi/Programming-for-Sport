# uses 'yield from' which requires Python 3
#
# changed 'yield from gen'
# to      for node in gen:
#             yield node
# so that it works in Python 2

class BinaryTree:
    def __init__(self, data, left_child=None, right_child=None):
        self.data= data
        self.left_child= left_child
        self.right_child= right_child
    
    # O(n) time where n is the number of nodes in self
    # O(depth) extra space (due to recursive call which must be saved in the call stack)
    #           where depth is the depth of self
    #                 depth is O(log(n)) if self is balanced
    #                 depth is O(n)      if self is so unbalanced that it resembles a list
    def number_of_leaves(self):
        
        tree= self
        
        if tree is None:
            return 0
        
        if tree.isLeave():
            return 1
        
        left, right = tree.left_child, tree.right_child
        return ( left.number_of_leaves() if left  else 0) + \
               (right.number_of_leaves() if right else 0)
    
    def isLeave(self):
        
        tree= self
        
        if tree is None:
            return False
        
        return ( tree.left_child is None ) and ( tree.right_child is None )
    
    def data_in_preorder_order(self):
        res= []
        for node in self.preorder_traverse():
            res.append( node.data )
        return res
    
    def preorder_traverse(self):
        yield self
        left, right = self.left_child, self.right_child
        if left:
            for node in left.preorder_traverse():
                yield node
            # yield from left.preorder_traverse() # replaces previous two lines,
                                                  # but not supported in Python 2.7
        if right:
            for node in right.preorder_traverse():
                yield node
            # yield from right.preorder_traverse() # replaces previous two lines,
                                                   # but not supported in Python 2.7


#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
#      /
#     7
#      \
#       8

bn= [None]*(8+1)

#                 d  left   right
bn[8]= BinaryTree(8)
bn[7]= BinaryTree(7, None,  bn[8])
bn[6]= BinaryTree(6)
bn[5]= BinaryTree(5, bn[7])
bn[4]= BinaryTree(4)
bn[3]= BinaryTree(3, None,  bn[6])
bn[2]= BinaryTree(2, bn[4], bn[5])
bn[1]= BinaryTree(1, bn[2], bn[3])

for i in range(1, 8+1):
    print( "bn{0}.data_in_preorder_order() equals: {1}".format( i, bn[i].data_in_preorder_order() ) )

# print out

# bn1.data_in_preorder_order() equals: [1, 2, 4, 5, 7, 8, 3, 6]
# bn2.data_in_preorder_order() equals: [2, 4, 5, 7, 8]
# bn3.data_in_preorder_order() equals: [3, 6]
# bn4.data_in_preorder_order() equals: [4]
# bn5.data_in_preorder_order() equals: [5, 7, 8]
# bn6.data_in_preorder_order() equals: [6]
# bn7.data_in_preorder_order() equals: [7, 8]
# bn8.data_in_preorder_order() equals: [8]