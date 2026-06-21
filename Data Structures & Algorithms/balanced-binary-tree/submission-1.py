# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        answer = True

        def sizeofTree (root) -> int:
            nonlocal answer
            if root == None:
                return 0 
            leftsize = sizeofTree(root.left)
            rightsize = sizeofTree(root.right)

            if abs(leftsize - rightsize) >1 :
                answer = False

            return max(leftsize, rightsize) + 1

        sizeofTree(root)

        return answer


        