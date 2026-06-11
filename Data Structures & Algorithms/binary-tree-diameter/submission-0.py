# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiam = 0 

        def diameterNode(root):
            nonlocal maxdiam

            if root == None:
                return -1
            
            diam_left = diameterNode(root.left)
            diam_right = diameterNode(root.right)
            node_diam = 0

            if diam_left ==-1 and diam_right ==-1:
                node_diam = 0
                maxdiam = max(maxdiam, node_diam)
            elif diam_left ==-1 or diam_right == -1:
                node_diam = 1+ max(diam_right, diam_left)
                maxdiam = max(maxdiam, node_diam)
            else:
                node_diam = 1+ max(diam_right, diam_left)
                maxdiam = max(maxdiam, 2+ diam_right + diam_left)
            
            return node_diam

        root_diam = diameterNode(root)

        return maxdiam
            
        