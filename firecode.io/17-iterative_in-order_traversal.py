class BinaryTree:
 
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def inorder_iterative(self):
        inorder_list = []
        
        root = self
        
        node_stack = []
        caller = None
        node_stack.append( (root, caller ) )
        while node_stack:
            
            curr_node, caller = node_stack.pop()
            
            if caller:
                inorder_list.append(caller.data)
            
            if not curr_node:
                continue
            
            right_child_called_by = curr_node
            node_stack.append( (curr_node.right_child, right_child_called_by) )
            
            node_stack.append( (curr_node.left_child, None) )
            
            
        return inorder_list 
     


    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data