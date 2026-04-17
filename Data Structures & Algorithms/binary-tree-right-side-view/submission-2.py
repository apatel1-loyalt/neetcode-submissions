# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()

        if root:
            queue.append(root)

        if not root:
            return []

        ans = []
        ans.append(root.val)
        while queue:
            tmp = True
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right and tmp:
                    ans.append(curr.right.val)
                    tmp = False
                elif curr.left and tmp:
                    ans.append(curr.left.val)
                    tmp = False


        return ans