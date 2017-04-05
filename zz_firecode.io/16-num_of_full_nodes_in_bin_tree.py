# 2    
# Required collection modules have already been imported. 
class BinaryTree(object):
    def __init__(self, root = None):
        ''' root is a BinaryTreeNode
        '''
        self.root = root
  
    def number_of_full_nodes(self, root):
        count_soFar = 0
        
        # DFS
        node_stack = []
        node_stack.append(root)
        while node_stack:
            curr_node = node_stack.pop()
            
            if not curr_node:
                
                # curr_node is None
                continue
                
            if curr_node.left_child and curr_node.right_child:
                count_soFar += 1
            
            node_stack.append(curr_node.left_child)
            node_stack.append(curr_node.right_child)
        
        return count_soFar
