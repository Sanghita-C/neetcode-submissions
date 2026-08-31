# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree (self, node1, node2) :
        if node1 is None and node2 is None:
            return True
        if node1 is None:
            return False
        if node2 is None:
            return False
        
        if node1.val != node2.val:
            return False
        
        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        can we have null subroot ? No

        Algo : 

        inorder traversal on original tree
        - when val same as root of subtree - send both the nodes to to isSameTree function
        """

        if root is None:
            return False
        
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)


        