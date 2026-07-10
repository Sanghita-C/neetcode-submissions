"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

"""
What do we need to  position the node properly : 
level, parent node

[1] [3 2 4] [5 6 "", "" "" "", ""]

[1:4] [2:0, 3:2, 4:1, 5:2] [6:0, 7:1, 8:1, 9:1, 10:0] [11:1, 12:0, 13:0]
"""

from collections import deque


class Codec:

    def serialize(self, root: Node) -> str:
        if not root:
            return ""

        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            result.append(f"{node.val}:{len(node.children)}")

            for child in node.children:
                queue.append(child)

        return ",".join(result)

    def deserialize(self, data: str) -> Node:
        if not data:
            return None

        entries = data.split(",")

        root_value, root_child_count = map(int, entries[0].split(":"))
        root = Node(root_value)

        # Queue stores:
        # (node, number of children that node must receive)
        queue = deque([(root, root_child_count)])

        index = 1

        while queue:
            parent, child_count = queue.popleft()

            for _ in range(child_count):
                value, number_of_children = map(
                    int,
                    entries[index].split(":")
                )
                index += 1

                child = Node(value)
                parent.children.append(child)

                queue.append((child, number_of_children))

        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))