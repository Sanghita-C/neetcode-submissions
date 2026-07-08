# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if not root:
            return 0
        
        max_node = root.val

        def dfs_good_nodes(root,max_node_in_path):
            nonlocal count
            if not root:
                return
            max_node_in_path = max(max_node_in_path,root.val)

            if root.val == max_node_in_path:
                count +=1 

            dfs_good_nodes(root.left,max_node_in_path)
            dfs_good_nodes(root.right,max_node_in_path)

            return

        dfs_good_nodes(root,max_node)

        return count

            
        