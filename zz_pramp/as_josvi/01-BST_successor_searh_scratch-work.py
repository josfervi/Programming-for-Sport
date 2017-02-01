Jose

#       100
#      /   \
#     50    200
#    / \   /   \
#   10 70 150 300

# for a node n, if it has a right subtree then return the smallest in the right subtree, which is the left most node in the right subtree

# if n does not have a right subtree,
# look at the parent


# if the successor was placed in the BST before node
# then

#         suc
#         /
#        a
#         \
#          b
#           \
#            n<<
         
#  anc: b < n
#     : a < n
#     : suc > n

# PRECONDITION: all nodes of the BST are unique
def findSuccessorOf(node):
   
   if node is None:
      return None
   
   if node.right:
      return findSmallestIn(node.right)
   
   # node doesn't have a right subtree
   ancestor = node.parent
   while ancestor and ancestor.val < node.val:
      ancestor = ancestor.parent
   
   if ancestor is None:
      # node does not have a successor
      return None
   
   # {ancestor is not None}
   return ancestor


#       100
#      /    \
#     50    200 
#    / \   /   \
#   10 70 150   300
   
def findSmallestIn(node):
   
   if node is None:
      # an empty tree has no smallest node
      return None
   
   while node.left:
      node = node.left
   
   return node