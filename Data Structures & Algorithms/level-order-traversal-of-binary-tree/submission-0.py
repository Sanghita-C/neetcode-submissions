# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)

        level_nodes = 1
        next_level_nodes = 0
        answer = []
        level_list = []

        while queue:
            node = queue.popleft()
            level_nodes -=1
            level_list.append(node.val)
            if node.left:
                queue.append(node.left)
                next_level_nodes +=1

            if node.right:
                queue.append(node.right)
                next_level_nodes +=1
            """
            print(f" processing node {node.val}")
            print(f" current level list {level_list}")
            print(f" current level nodes left to be processed {level_nodes}")
            print(f" current number of child nodes added = {next_level_nodes}")
            """

            if level_nodes == 0:
                #print(f"current level processed")
                level_nodes = next_level_nodes
                next_level_nodes = 0
                answer.append(level_list)
                level_list = []
        
        return answer