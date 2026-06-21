# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sizeofTree (self, root) -> int:
        if root == None:
            return 0 
        leftsize = self.sizeofTree(root.left)
        rightsize = self.sizeofTree(root.right)

        return max(leftsize, rightsize) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        left_size = self.sizeofTree(root.left)
        right_size = self.sizeofTree(root.right) 

        if abs(left_size - right_size) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

        