"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}
        old_to_new[node] = Node(node.val)
        q = deque([node])

        while q:
            c = q.popleft()

            for i in c.neighbors:
                if i not in old_to_new:
                    old_to_new[i] = Node(i.val)
                    q.append(i)
                old_to_new[c].neighbors.append(old_to_new[i])

        return old_to_new[node]