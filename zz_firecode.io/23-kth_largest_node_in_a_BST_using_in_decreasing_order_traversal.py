class BinaryTree:
    
    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
    
    # Helper Method    
    def size(self,root):
        if root == None:
            return 0
        else:
            return (self.size(root.left_child) + 1 + self.size(root.right_child)) 
        
    def find_kth_largest(self, tree, k):
        
        if not tree:
            return None
        
        return self.in_decreasing_order_traversal(tree, k)
    
    # another way to do it is by using the length of the right subtree
        
    def in_decreasing_order_traversal(self, tree, k):
        
        # base case
        if not tree:
            return k
        
        k = self.in_decreasing_order_traversal(tree.right_child, k)
        if type(k) is not int:
            result = k
            return result
        
        k -= 1
        if k == 0:
            result = tree
            return result
        
        k = self.in_decreasing_order_traversal(tree.left_child, k)
        
        return k