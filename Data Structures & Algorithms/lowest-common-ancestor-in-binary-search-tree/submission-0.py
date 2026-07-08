# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        small_val = min(p.val, q.val)
        large_val = max(p.val, q.val)

        print(f"small value is {small_val}, large_val = {large_val}, root_val = {root.val}")

        if small_val==root.val or large_val==root.val:
            return root
        

        if small_val < root.val and large_val > root.val:
            return root

        if small_val <root.val and large_val <root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        return self.lowestCommonAncestor(root.right,p,q)
        