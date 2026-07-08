# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 
        min_val_for_node = -1001
        max_val_for_node = 1001

        def validate_bst_node (root, min_val_for_node, max_val_for_node):
            if not root:
                return True
            
            if root.val <= min_val_for_node or root.val >= max_val_for_node:
                return False
            
            return validate_bst_node(root.left, min_val_for_node, root.val ) and validate_bst_node(root.right, root.val, max_val_for_node )
        
        return validate_bst_node(root,min_val_for_node, max_val_for_node)





        