# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        if not root:
            return 0
        def calculate_subtree_width(root):
            nonlocal diameter
            if root ==None:
                return -1
            if root.right == None and root.left == None:
                return 0
            
            right_path = calculate_subtree_width(root.right)
            left_path = calculate_subtree_width(root.left)

            subtree_diameter = (right_path + 1)+ (left_path + 1)
            diameter = max(diameter, subtree_diameter)

            return max(right_path,left_path) +1

        calculate_subtree_width(root)

        return diameter
        