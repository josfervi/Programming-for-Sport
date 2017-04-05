class BinaryTree:
    
    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
    
    # Helper Method    
    def size(self, root):
        if root == None:
            return 0
        else:
            return (self.size(root.left_child) + 1 + self.size(root.right_child)) 
        
    def find_kth_smallest(self, root, k):
        # Return element should be of Type TreeNode
        
        this_node = root
        
        if not this_node:
            return None
        
        s_left = self.size(this_node.left_child)
        
        if s_left == k-1:
            return this_node
        
        if s_left < k-1:
            return self.find_kth_smallest(this_node.right_child, k-(s_left+1))
        
        else:
            return self.find_kth_smallest(this_node.left_child, k)