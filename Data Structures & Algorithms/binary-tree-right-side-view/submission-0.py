# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view = []

        def dfs(level, right_side_view, root):
            if not root:
                return
            if len(right_side_view) == level:
                right_side_view.append(root.val)
            if root.right:
                dfs(level+1,right_side_view,root.right)
            if root.left:
                dfs(level+1,right_side_view,root.left)
            return
        
        dfs(0,right_side_view,root)

        return right_side_view





        