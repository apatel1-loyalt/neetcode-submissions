# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative Solution
        stack = []

        while root or stack:
            # Go left
            while root:
                stack.append(root)
                root = root.left
            
            # Go back one stap
            root = stack.pop()
            k -= 1
            
            if k == 0:
                return root.val

            # Go right
            root = root.right