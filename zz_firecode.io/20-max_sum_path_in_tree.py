class BinaryTree:
    def __init__(self, root = None):
        self.root = root
    
    def max_sum_path(self, root):
        
        _, val_of_max_path = self._val_of_max_path(root)
        
        return val_of_max_path
    
    def _val_of_max_path(self, root):
        ''' Returns a tuple:
            ( val of the maximal path
              from a leaf up to root,
              
              val of the maximal path
              from a node to another
              node in this subtree )
        '''
        
        # base case
        if not root:
            return (0, 0)
        
        # recursive case
        
        ( val_of_max_path_from_a_leaf_up_to_left_child,
          val_of_max_path_in_left_subtree ) = (
              
              self._val_of_max_path(root.left_child) )
        
        ( val_of_max_path_from_a_leaf_up_to_right_child,
          val_of_max_path_in_right_subtree ) = (
              
              self._val_of_max_path(root.right_child) )
        
        val_of_max_path_from_a_leaf_up_to_root = root.data + max(
            
            val_of_max_path_from_a_leaf_up_to_left_child,
            val_of_max_path_from_a_leaf_up_to_right_child )
        
        val_of_max_path_that_has_a_turning_point_at_root = (
            
            val_of_max_path_from_a_leaf_up_to_left_child +
            root.data +
            val_of_max_path_from_a_leaf_up_to_right_child )
        
        val_of_max_path_in_this_subtree = max(
            
            val_of_max_path_in_left_subtree,
            val_of_max_path_in_right_subtree,
            val_of_max_path_that_has_a_turning_point_at_root )
        
        return ( val_of_max_path_from_a_leaf_up_to_root,
                 val_of_max_path_in_this_subtree )
            