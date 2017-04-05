class BinaryTree:
    def __init__(self, data, left_child=None, right_child=None):
        self.data= data
        self.left_child= left_child
        self.right_child= right_child
    
    
    def number_of_leaves(self,root):
        count_soFar = 0
        node_stack = []
        node_stack.append(root)
        while node_stack:
            
            curr_node = node_stack.pop()
            
            if not curr_node:
                continue
            
            if self.is_leaf(curr_node):
                count_soFar += 1
            
            node_stack.append(curr_node.left_child)
            node_stack.append(curr_node.right_child)
                
        return count_soFar
    
    # O(n) time where n is the number of nodes in self
    # O(depth) extra space (due to recursive call which must be saved in the call stack)
    #           where depth is the depth of self
    #                 depth is O(log(n)) if self is balanced
    #                 depth is O(n)      if self is so unbalanced that it resembles a list
    def number_of_leaves_recursive(self):
        
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

for i in xrange(1, 8+1):
    print ("bn%d.isLeave() equals:" % i), bn[i].isLeave()

# print out

# bn1.isLeave() equals: False
# bn2.isLeave() equals: False
# bn3.isLeave() equals: False
# bn4.isLeave() equals: True
# bn5.isLeave() equals: False
# bn6.isLeave() equals: True
# bn7.isLeave() equals: False
# bn8.isLeave() equals: True

for i in xrange(1, 8+1):
    print ("bn%d.number_of_leaves() equals:" % i), bn[i].number_of_leaves()

# print out

# bn1.number_of_leaves() equals: 3
# bn2.number_of_leaves() equals: 2
# bn3.number_of_leaves() equals: 1
# bn4.number_of_leaves() equals: 1
# bn5.number_of_leaves() equals: 1
# bn6.number_of_leaves() equals: 1
# bn7.number_of_leaves() equals: 1
# bn8.number_of_leaves() equals: 1